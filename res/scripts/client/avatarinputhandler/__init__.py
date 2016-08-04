# 2016.08.04 19:48:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/AvatarInputHandler/__init__.py
import functools
import math
from functools import partial
import BattleReplay
import DynamicCameras.ArcadeCamera
import DynamicCameras.SniperCamera
import DynamicCameras.StrategicCamera
import FalloutDeathMode
import GUI
import Keys
import MapCaseMode
import Math
import ResMgr
import cameras
import constants
import control_modes
from AvatarInputHandler.AimingSystems.SniperAimingSystem import SniperAimingSystem
from Event import Event
from avatar_helpers import aim_global_binding
from constants import ARENA_PERIOD, AIMING_MODE
from control_modes import _ARCADE_CAM_PIVOT_POS
from debug_utils import *
from gui import g_guiResetters, GUI_CTRL_MODE_FLAG
from gui.app_loader import g_appLoader, settings
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from gui.battle_control.battle_constants import GUN_RELOADING_VALUE_TYPE
from helpers.CallbackDelayer import CallbackDelayer
from post_processing.post_effect_controllers import g_postProcessingEvents

def _getAmmoGuiCtrl():
    from gui.battle_control import g_sessionProvider
    return g_sessionProvider.shared.ammo


_INPUT_HANDLER_CFG = 'gui/avatar_input_handler.xml'

class _CTRL_TYPE():
    USUAL = 0
    OPTIONAL = 1
    DEVELOPMENT = 2


_CTRL_MODE = aim_global_binding.CTRL_MODE_NAME
_CTRLS_FIRST = _CTRL_MODE.DEFAULT
_CTRLS_DESC_MAP = {_CTRL_MODE.ARCADE: ('ArcadeControlMode', 'arcadeMode', _CTRL_TYPE.USUAL),
 _CTRL_MODE.STRATEGIC: ('StrategicControlMode', 'strategicMode', _CTRL_TYPE.USUAL),
 _CTRL_MODE.SNIPER: ('SniperControlMode', 'sniperMode', _CTRL_TYPE.USUAL),
 _CTRL_MODE.POSTMORTEM: ('PostMortemControlMode', 'postMortemMode', _CTRL_TYPE.USUAL),
 _CTRL_MODE.DEBUG: ('DebugControlMode', None, _CTRL_TYPE.DEVELOPMENT),
 _CTRL_MODE.CAT: ('CatControlMode', None, _CTRL_TYPE.DEVELOPMENT),
 _CTRL_MODE.VIDEO: ('VideoCameraControlMode', 'videoMode', _CTRL_TYPE.OPTIONAL),
 _CTRL_MODE.MAP_CASE: ('MapCaseControlMode', 'strategicMode', _CTRL_TYPE.USUAL),
 _CTRL_MODE.FALLOUT_DEATH: ('FalloutDeathMode', 'postMortemMode', _CTRL_TYPE.USUAL)}
_DYNAMIC_CAMERAS = (DynamicCameras.ArcadeCamera.ArcadeCamera, DynamicCameras.SniperCamera.SniperCamera, DynamicCameras.StrategicCamera.StrategicCamera)

class ShakeReason():
    OWN_SHOT = 0
    OWN_SHOT_DELAYED = 1
    HIT = 2
    HIT_NO_DAMAGE = 3
    SPLASH = 4


class DynamicCameraSettings(object):
    settings = property(lambda self: self.__dynamic)

    def __init__(self, dataSec):
        self.__dynamic = {'caliberImpulses': [],
         'massSensitivity': []}
        caliberSettings = dataSec['caliberImpulses']
        if caliberSettings is not None:
            self.__dynamic['caliberImpulses'] = self.__readRange(caliberSettings)
        else:
            LOG_ERROR('<caliberImpulses> dataSection is not found!')
        sensitivitySettings = dataSec['massSensitivity']
        if sensitivitySettings is not None:
            self.__dynamic['massSensitivity'] = self.__readRange(sensitivitySettings)
        else:
            LOG_ERROR('<massSensitivity> dataSection is not found!')
        self.__dynamic['collisionSpeedToImpulseRatio'] = cameras.readFloat(dataSec, 'collisionSpeedToImpulseRatio', 0, 1000, 1.0)
        self.__dynamic['minCollisionSpeed'] = cameras.readFloat(dataSec, 'minCollisionSpeed', 0, 1000, 1.0)
        self.__dynamic['zeroDamageHitSensitivity'] = cameras.readFloat(dataSec, 'zeroDamageHitSensitivity', 0, 1000, 1.0)
        self.__dynamic['ownShotImpulseDelay'] = cameras.readFloat(dataSec, 'ownShotImpulseDelay', 0.0, 1000, 0.0)
        return

    def getGunImpulse(self, caliber):
        impulseMagnitude = 0.0
        for minCaliber, magnitude in self.__dynamic['caliberImpulses']:
            if caliber < minCaliber:
                break
            impulseMagnitude = magnitude

        return impulseMagnitude

    def getSensitivityToImpulse(self, vehicleMass):
        sensitivity = 0.0
        for mass, sense in self.__dynamic['massSensitivity']:
            if vehicleMass < mass:
                break
            sensitivity = sense

        return sensitivity

    def __readRange(self, dataSec):
        ranges = []
        for rangeSec in dataSec.values():
            val = rangeSec.asVector2
            ranges.append((val.x, val.y))

        ranges.sort(key=lambda val: val[0])
        return ranges


class AvatarInputHandler(CallbackDelayer):
    ctrl = property(lambda self: self.__curCtrl)
    ctrls = property(lambda self: self.__ctrls)
    isSPG = property(lambda self: self.__isSPG)
    isATSPG = property(lambda self: self.__isATSPG)
    isFlashBangAllowed = property(lambda self: self.__ctrls['video'] != self.__curCtrl)
    isDetached = property(lambda self: self.__isDetached)
    isGuiVisible = property(lambda self: self.__isGUIVisible)
    ctrlModeName = aim_global_binding.bind(aim_global_binding.BINDING_ID.CTRL_MODE_NAME)
    __aimOffset = aim_global_binding.bind(aim_global_binding.BINDING_ID.AIM_OFFSET)
    __gunMarkerPosition = aim_global_binding.bind(aim_global_binding.BINDING_ID.GUN_MARKER_POSITION)
    _DYNAMIC_CAMERAS_ENABLED_KEY = 'global/dynamicCameraEnabled'

    @staticmethod
    def enableDynamicCamera(enable, useHorizontalStabilizer = True):
        for dynamicCameraClass in _DYNAMIC_CAMERAS:
            dynamicCameraClass.enableDynamicCamera(enable)

        SniperAimingSystem.setStabilizerSettings(useHorizontalStabilizer, True)

    @staticmethod
    def isCameraDynamic():
        for dynamicCameraClass in _DYNAMIC_CAMERAS:
            if not dynamicCameraClass.isCameraDynamic():
                return False

        return True

    @staticmethod
    def isSniperStabilized():
        return SniperAimingSystem.getStabilizerSettings()

    def __init__(self):
        CallbackDelayer.__init__(self)
        self.__alwaysShowAimKey = None
        self.__showMarkersKey = None
        sec = self._readCfg()
        self.onCameraChanged = Event()
        self.onPostmortemVehicleChanged = Event()
        self.onSetReloading = Event()
        self.onSetReloadingPercents = Event()
        self.__isArenaStarted = False
        self.__isStarted = False
        self.__targeting = _Targeting()
        self.__vertScreenshotCamera = _VertScreenshotCamera()
        self.__ctrls = dict()
        self.__killerVehicleID = None
        self.__isAutorotation = True
        self.__prevModeAutorotation = None
        self.__isSPG = False
        self.__isATSPG = False
        self.__setupCtrls(sec)
        self.__curCtrl = self.__ctrls[_CTRLS_FIRST]
        self.ctrlModeName = _CTRLS_FIRST
        self.__isDetached = False
        self.__waitObserverCallback = None
        self.__observerVehicle = None
        return

    def prerequisites(self):
        out = []
        for ctrl in self.__ctrls.itervalues():
            out += ctrl.prerequisites()

        return out

    def handleKeyEvent(self, event):
        import game
        isDown, key, mods, isRepeat = game.convertKeyEvent(event)
        if isRepeat:
            return False
        elif self.__isStarted and self.__isDetached:
            return BigWorld.player().handleKey(isDown, key, mods)
        elif not self.__isStarted or self.__isDetached:
            return False
        if isDown and BigWorld.isKeyDown(Keys.KEY_CAPSLOCK):
            if self.__alwaysShowAimKey is not None and key == self.__alwaysShowAimKey:
                gui_event_dispatcher.toggleCrosshairVisibility()
                return True
            if self.__showMarkersKey is not None and key == self.__showMarkersKey and not self.__isGUIVisible:
                gui_event_dispatcher.toggleMarkers2DVisibility()
                return True
            if key == Keys.KEY_F5 and constants.HAS_DEV_RESOURCES:
                self.__vertScreenshotCamera.enable(not self.__vertScreenshotCamera.isEnabled)
                return True
        if self.__curCtrl.handleKeyEvent(isDown, key, mods, event):
            return True
        else:
            return BigWorld.player().handleKey(isDown, key, mods)

    def handleMouseEvent(self, dx, dy, dz):
        if not self.__isStarted or self.__isDetached:
            return False
        return self.__curCtrl.handleMouseEvent(dx, dy, dz)

    def setForcedGuiControlMode(self, flags):
        result = False
        if not self.__isStarted:
            return result
        detached = flags & GUI_CTRL_MODE_FLAG.CURSOR_ATTACHED > 0
        if detached ^ self.__isDetached:
            self.__isDetached = detached
            self.__targeting.detach(self.__isDetached)
            if detached:
                g_appLoader.attachCursor(settings.APP_NAME_SPACE.SF_BATTLE, flags=flags)
                result = True
                if flags & GUI_CTRL_MODE_FLAG.AIMING_ENABLED > 0:
                    self.setAimingMode(False, AIMING_MODE.USER_DISABLED)
            else:
                g_appLoader.detachCursor(settings.APP_NAME_SPACE.SF_BATTLE)
                result = True
            self.__curCtrl.setForcedGuiControlMode(not detached)
        elif detached:
            g_appLoader.syncCursor(settings.APP_NAME_SPACE.SF_BATTLE, flags=flags)
        return result

    def updateShootingStatus(self, canShoot):
        if self.__isDetached:
            return
        return self.__curCtrl.updateShootingStatus(canShoot)

    def getDesiredShotPoint(self):
        if self.__isDetached:
            return None
        else:
            g_postProcessingEvents.onFocalPlaneChanged()
            return self.__curCtrl.getDesiredShotPoint()

    def showGunMarker(self, flag):
        self.__curCtrl.showGunMarker(flag)

    def showGunMarker2(self, flag):
        self.__curCtrl.showGunMarker2(flag)

    def updateGunMarker(self, pos, dir, size, relaxTime, collData):
        self.__gunMarkerPosition = (pos, relaxTime)
        self.__curCtrl.updateGunMarker(pos, dir, size, relaxTime, collData)

    def updateGunMarker2(self, pos, dir, size, relaxTime, collData):
        self.__curCtrl.updateGunMarker2(pos, dir, size, relaxTime, collData)

    def setAimingMode(self, enable, mode):
        self.__curCtrl.setAimingMode(enable, mode)

    def getAimingMode(self, mode):
        return self.__curCtrl.getAimingMode(mode)

    def setAutorotation(self, bValue):
        if not self.__curCtrl.enableSwitchAutorotationMode():
            return
        elif not BigWorld.player().isOnArena:
            return
        else:
            if self.__isAutorotation != bValue:
                self.__isAutorotation = bValue
                BigWorld.player().enableOwnVehicleAutorotation(self.__isAutorotation)
            self.__prevModeAutorotation = None
            return

    def getAutorotation(self):
        return self.__isAutorotation

    def switchAutorotation(self):
        self.setAutorotation(not self.__isAutorotation)

    def activatePostmortem(self, isRespawn):
        BigWorld.player().consistentMatrices.notifyPreBind(BigWorld.player())
        if not isRespawn:
            try:
                params = self.__curCtrl.postmortemCamParams
            except:
                params = None

            onPostmortemActivation = getattr(self.__curCtrl, 'onPostmortemActivation', None)
            if onPostmortemActivation is not None:
                onPostmortemActivation()
            else:
                self.onControlModeChanged('postmortem', postmortemParams=params, bPostmortemDelay=True)
        else:
            BigWorld.player().autoAim(None)
            for ctlMode in self.__ctrls.itervalues():
                ctlMode.resetAimingMode()

            self.onControlModeChanged('falloutdeath')
        return

    def addVehicleToCameraCollider(self, vehicle):
        cams = (self.ctrls['arcade'].camera, self.ctrls['postmortem'].camera)
        for camera in cams:
            if camera is None:
                continue
            camera.addVehicleToCollideWith(vehicle)

        return

    def removeVehicleFromCameraCollider(self, vehicle):
        cams = (self.ctrls['arcade'].camera, self.ctrls['postmortem'].camera)
        for camera in cams:
            if camera is None:
                continue
            camera.removeVehicleToCollideWith(vehicle)

        return

    def reinitVehicleMatrix(self):
        arcadeMode = self.__ctrls['arcade']
        arcadeMode.camera.reinitMatrix()

    def deactivatePostmortem(self):
        self.onControlModeChanged('arcade')
        arcadeMode = self.__ctrls['arcade']
        arcadeMode.camera.setToVehicleDirection()
        self.__identifySPG()
        self.setReloading(-1)

    def setKillerVehicleID(self, killerVehicleID):
        self.__killerVehicleID = killerVehicleID

    def getKillerVehicleID(self):
        return self.__killerVehicleID

    def start(self):
        g_guiResetters.add(self.__onRecreateDevice)
        self.__identifySPG()
        for control in self.__ctrls.itervalues():
            control.create()

        self.__addBattleCtrlListeners()
        if not self.__curCtrl.isManualBind():
            BigWorld.player().positionControl.bindToVehicle(True)
        self.__curCtrl.enable(ctrlState=control_modes.dumpStateEmpty())
        self.onCameraChanged('arcade')
        tmp = self.__curCtrl.getPreferredAutorotationMode()
        if tmp is not None:
            self.__isAutorotation = tmp
            self.__prevModeAutorotation = True
        else:
            self.__isAutorotation = True
            self.__prevModeAutorotation = None
        BigWorld.player().enableOwnVehicleAutorotation(self.__isAutorotation)
        self.__targeting.enable(True)
        self.__isStarted = True
        self.__isGUIVisible = True
        self.__killerVehicleID = None
        arena = BigWorld.player().arena
        arena.onPeriodChange += self.__onArenaStarted
        from account_helpers.settings_core.SettingsCore import g_settingsCore
        g_settingsCore.onSettingsChanged += self.__onSettingsChanged
        BigWorld.player().consistentMatrices.onVehicleMatrixBindingChanged += self.__onVehicleChanged
        self.__onArenaStarted(arena.period)
        return

    def stop(self):
        self.__isStarted = False
        import SoundGroups
        SoundGroups.g_instance.changePlayMode(1)
        aim_global_binding.clear()
        self.__removeBattleCtrlListeners()
        for control in self.__ctrls.itervalues():
            control.destroy()

        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isRecording:
            replayCtrl.setPlayerVehicleID(0)
        self.onCameraChanged = None
        self.__targeting.enable(False)
        self.__killerVehicleID = None
        g_guiResetters.remove(self.__onRecreateDevice)
        BigWorld.player().arena.onPeriodChange -= self.__onArenaStarted
        from account_helpers.settings_core.SettingsCore import g_settingsCore
        g_settingsCore.onSettingsChanged -= self.__onSettingsChanged
        BigWorld.player().consistentMatrices.onVehicleMatrixBindingChanged -= self.__onVehicleChanged
        CallbackDelayer.destroy(self)
        return

    def __onVehicleChanged(self, isStatic):
        if self.__waitObserverCallback and self.__observerVehicle:
            player = BigWorld.player()
            ownVehicle = BigWorld.entity(player.playerVehicleID)
            vehicle = player.getVehicleAttached()
            if vehicle != ownVehicle:
                self.__waitObserverCallback()
                self.__waitObserverCallback = None
        return

    def onControlModeChanged(self, eMode, **args):
        if not self.__isArenaStarted and eMode != 'postmortem':
            return
        else:
            player = BigWorld.player()
            isObserverMode = 'observer' in player.vehicleTypeDescriptor.type.tags
            if self.__waitObserverCallback:
                self.__waitObserverCallback = None
            if isObserverMode and eMode == 'postmortem':
                player = BigWorld.player()
                ownVehicle = BigWorld.entity(player.playerVehicleID)
                vehicle = player.getVehicleAttached()
                if (vehicle == ownVehicle or vehicle is None) and self.__observerVehicle is not None:
                    self.__waitObserverCallback = partial(self.onControlModeChanged, eMode, **args)
                    player.positionControl.followCamera(False)
                    player.positionControl.bindToVehicle(True, self.__observerVehicle)
                    return
            if isObserverMode and self.ctrlModeName == _CTRL_MODE.POSTMORTEM:
                player = BigWorld.player()
                self.__observerVehicle = player.vehicle.id if player.vehicle else None
            ctrl = BattleReplay.g_replayCtrl
            if ctrl.isRecording:
                ctrl.setControlMode(eMode)
            ctrlState = self.__curCtrl.dumpState()
            self.__curCtrl.disable()
            prevCtrl = self.__curCtrl
            self.__curCtrl = self.__ctrls[eMode]
            self.ctrlModeName = eMode
            if player is not None:
                if not prevCtrl.isManualBind() and self.__curCtrl.isManualBind():
                    player.positionControl.bindToVehicle(False)
                if prevCtrl.isManualBind() and not self.__curCtrl.isManualBind():
                    player.positionControl.bindToVehicle(True)
            if player is not None:
                newAutoRotationMode = self.__curCtrl.getPreferredAutorotationMode()
                if newAutoRotationMode is not None:
                    if prevCtrl.getPreferredAutorotationMode() is None:
                        self.__prevModeAutorotation = self.__isAutorotation
                    if self.__isAutorotation != newAutoRotationMode:
                        self.__isAutorotation = newAutoRotationMode
                        BigWorld.player().enableOwnVehicleAutorotation(self.__isAutorotation)
                elif prevCtrl.getPreferredAutorotationMode() is not None:
                    if self.__prevModeAutorotation is None:
                        self.__prevModeAutorotation = True
                    if self.__isAutorotation != self.__prevModeAutorotation:
                        self.__isAutorotation = self.__prevModeAutorotation
                        BigWorld.player().enableOwnVehicleAutorotation(self.__isAutorotation)
                    self.__prevModeAutorotation = None
            self.__targeting.onRecreateDevice()
            self.__curCtrl.setGUIVisible(self.__isGUIVisible)
            vehicle = player.getVehicleAttached()
            if isObserverMode:
                self.__curCtrl.enable(ctrlState=ctrlState, vehicleID=self.__observerVehicle, **args)
            else:
                self.__curCtrl.enable(ctrlState=ctrlState, **args)
            self.onCameraChanged(eMode, vehicle.id if isObserverMode else None)
            self.__curCtrl.handleMouseEvent(0.0, 0.0, 0.0)
            return

    def getTargeting(self):
        return self.__targeting

    def setGUIVisible(self, isVisible):
        self.__isGUIVisible = isVisible
        self.__curCtrl.setGUIVisible(isVisible)

    def selectPlayer(self, vehId):
        self.__curCtrl.selectPlayer(vehId)

    def onMinimapClicked(self, worldPos):
        self.__curCtrl.onMinimapClicked(worldPos)

    def setReloading(self, duration, startTime = None, baseTime = None):
        self.onSetReloading(duration, startTime, baseTime)

    def setReloadingInPercent(self, percent):
        self.onSetReloadingPercents(percent)

    def onVehicleShaken(self, vehicle, impulsePosition, impulseDir, caliber, shakeReason):
        if shakeReason == ShakeReason.OWN_SHOT_DELAYED:
            shakeFuncBound = functools.partial(self.onVehicleShaken, vehicle, impulsePosition, impulseDir, caliber, ShakeReason.OWN_SHOT)
            delayTime = self.__dynamicCameraSettings.settings['ownShotImpulseDelay']
            self.delayCallback(delayTime, shakeFuncBound)
            return
        else:
            camera = getattr(self.ctrl, 'camera', None)
            if camera is None:
                return
            impulseValue = self.__dynamicCameraSettings.getGunImpulse(caliber)
            vehicleSensitivity = 0.0
            avatarVehicle = BigWorld.player().getVehicleAttached()
            if avatarVehicle is None or not avatarVehicle.isAlive():
                return
            avatarVehicleTypeDesc = getattr(avatarVehicle, 'typeDescriptor', None)
            if avatarVehicleTypeDesc is not None:
                avatarVehWeightTons = avatarVehicleTypeDesc.physics['weight'] / 1000.0
                vehicleSensitivity = self.__dynamicCameraSettings.getSensitivityToImpulse(avatarVehWeightTons)
                vehicleSensitivity *= avatarVehicleTypeDesc.hull['swinging']['sensitivityToImpulse']
            impulseReason = None
            isDistant = False
            if shakeReason == ShakeReason.OWN_SHOT:
                if vehicle is avatarVehicle:
                    impulseReason = cameras.ImpulseReason.MY_SHOT
                    isDistant = False
                else:
                    impulseReason = cameras.ImpulseReason.OTHER_SHOT
                    isDistant = True
            elif vehicle is avatarVehicle:
                if shakeReason == ShakeReason.HIT or shakeReason == ShakeReason.HIT_NO_DAMAGE:
                    impulseValue *= 1.0 if shakeReason == ShakeReason.HIT else self.__dynamicCameraSettings.settings['zeroDamageHitSensitivity']
                    impulseReason = cameras.ImpulseReason.ME_HIT
                    isDistant = False
                else:
                    impulseReason = cameras.ImpulseReason.SPLASH
                    isDistant = True
            impulseDir, impulseValue = self.__adjustImpulse(impulseDir, impulseValue, camera, impulsePosition, vehicleSensitivity, impulseReason)
            if isDistant:
                camera.applyDistantImpulse(impulsePosition, impulseValue, impulseReason)
            else:
                camera.applyImpulse(impulsePosition, impulseDir * impulseValue, impulseReason)
            return

    def onVehicleCollision(self, vehicle, impactVelocity):
        if impactVelocity < self.__dynamicCameraSettings.settings['minCollisionSpeed']:
            return
        else:
            camera = getattr(self.ctrl, 'camera', None)
            if camera is None:
                return
            avatarVehicle = BigWorld.player().getVehicleAttached()
            if avatarVehicle is None or not avatarVehicle.isAlive():
                return
            if vehicle is avatarVehicle:
                impulse = Math.Vector3(0, impactVelocity * self.__dynamicCameraSettings.settings['collisionSpeedToImpulseRatio'], 0)
                camera.applyImpulse(vehicle.position, impulse, cameras.ImpulseReason.COLLISION)
            return

    def onVehicleDeath(self, vehicle, exploded):
        if not exploded:
            return
        else:
            camera = getattr(self.ctrl, 'camera', None)
            if camera is None:
                return
            avatarVehicle = BigWorld.player().getVehicleAttached()
            if avatarVehicle is None or avatarVehicle is vehicle:
                return
            caliber = vehicle.typeDescriptor.shot['shell']['caliber']
            impulseValue = self.__dynamicCameraSettings.getGunImpulse(caliber)
            avatarVehicleWeightInTons = avatarVehicle.typeDescriptor.physics['weight'] / 1000.0
            vehicleSensitivity = self.__dynamicCameraSettings.getSensitivityToImpulse(avatarVehicleWeightInTons)
            vehicleSensitivity *= avatarVehicle.typeDescriptor.hull['swinging']['sensitivityToImpulse']
            _, impulseValue = self.__adjustImpulse(Math.Vector3(0, 0, 0), impulseValue, camera, vehicle.position, vehicleSensitivity, cameras.ImpulseReason.VEHICLE_EXPLOSION)
            camera.applyDistantImpulse(vehicle.position, impulseValue, cameras.ImpulseReason.VEHICLE_EXPLOSION)
            return

    def onExplosionImpulse(self, position, impulseValue):
        camera = getattr(self.ctrl, 'camera', None)
        if camera is None:
            return
        else:
            avatarVehicle = BigWorld.player().getVehicleAttached()
            if avatarVehicle is None:
                return
            avatarVehicleWeightInTons = avatarVehicle.typeDescriptor.physics['weight'] / 1000.0
            vehicleSensitivity = self.__dynamicCameraSettings.getSensitivityToImpulse(avatarVehicleWeightInTons)
            vehicleSensitivity *= avatarVehicle.typeDescriptor.hull['swinging']['sensitivityToImpulse']
            _, impulseValue = self.__adjustImpulse(Math.Vector3(0, 0, 0), impulseValue, camera, position, vehicleSensitivity, cameras.ImpulseReason.HE_EXPLOSION)
            camera.applyDistantImpulse(position, impulseValue, cameras.ImpulseReason.HE_EXPLOSION)
            return

    def onProjectileHit(self, position, caliber, isOwnShot):
        if not isOwnShot:
            return
        else:
            camera = getattr(self.ctrl, 'camera', None)
            if camera is None:
                return
            impulseValue = self.__dynamicCameraSettings.getGunImpulse(caliber)
            vehicleSensitivity = 1.0
            avatarVehicle = BigWorld.player().getVehicleAttached()
            if avatarVehicle is not None:
                avatarVehicleWeightInTons = avatarVehicle.typeDescriptor.physics['weight'] / 1000.0
                vehicleSensitivity = self.__dynamicCameraSettings.getSensitivityToImpulse(avatarVehicleWeightInTons)
                vehicleSensitivity *= avatarVehicle.typeDescriptor.hull['swinging']['sensitivityToImpulse']
            _, impulseValue = self.__adjustImpulse(Math.Vector3(0, 0, 0), impulseValue, camera, position, vehicleSensitivity, cameras.ImpulseReason.VEHICLE_EXPLOSION)
            camera.applyDistantImpulse(position, impulseValue, cameras.ImpulseReason.PROJECTILE_HIT)
            return

    def __adjustImpulse(self, impulseDir, impulseValue, camera, impulsePosition, vehicleSensitivity, impulseReason):
        if impulseReason in camera.getReasonsAffectCameraDirectly():
            dirToCamera = camera.camera.position - impulsePosition
            dirToCamera.normalise()
            impulseDir = dirToCamera
        else:
            impulseValue *= vehicleSensitivity
        return (impulseDir, impulseValue)

    def __identifySPG(self):
        vehTypeDesc = BigWorld.entity(BigWorld.player().playerVehicleID).typeDescriptor.type
        self.__isSPG = 'SPG' in vehTypeDesc.tags
        self.__isATSPG = 'AT-SPG' in vehTypeDesc.tags

    def reloadDynamicSettings(self):
        if not constants.HAS_DEV_RESOURCES:
            return
        ResMgr.purge(_INPUT_HANDLER_CFG)
        sec = ResMgr.openSection(_INPUT_HANDLER_CFG)
        self.__dynamicCameraSettings = DynamicCameraSettings(sec['dynamicCameraCommon'])
        try:
            self.__ctrls['sniper'].camera.aimingSystem.reloadConfig(sec['sniperMode']['camera'])
        except:
            pass

    def _readCfg(self):
        sec = ResMgr.openSection(_INPUT_HANDLER_CFG)
        if sec is None:
            LOG_ERROR('can not open <%s>.' % _INPUT_HANDLER_CFG)
            return
        else:
            self.__checkSections(sec)
            keySec = sec['keys']
            if keySec is not None:
                self.__showMarkersKey = getattr(Keys, keySec.readString('showMarkersKey', ''), None)
                self.__alwaysShowAimKey = getattr(Keys, keySec.readString('alwaysShowAimKey', ''), None)
            self.__dynamicCameraSettings = DynamicCameraSettings(sec['dynamicCameraCommon'])
            return sec

    def __setupCtrls(self, section):
        modules = (control_modes, MapCaseMode, FalloutDeathMode)
        for name, desc in _CTRLS_DESC_MAP.items():
            try:
                if desc[2] != _CTRL_TYPE.DEVELOPMENT or desc[2] == _CTRL_TYPE.DEVELOPMENT and constants.HAS_DEV_RESOURCES:
                    if name not in self.__ctrls:
                        for module in modules:
                            classType = getattr(module, desc[0], None)
                            if classType is None:
                                pass
                            else:
                                self.__ctrls[name] = classType(section[desc[1]] if desc[1] else None, self)
                                break

            except:
                LOG_DEBUG('Error while setting ctrls', name, desc, constants.HAS_DEV_RESOURCES)
                LOG_CURRENT_EXCEPTION()

        return

    def __checkSections(self, section):
        for name, desc in _CTRLS_DESC_MAP.items():
            if desc[1] is None or desc[2] == _CTRL_TYPE.OPTIONAL or desc[2] == _CTRL_TYPE.DEVELOPMENT and not constants.HAS_DEV_RESOURCES:
                continue
            if not section.has_key(desc[1]):
                LOG_ERROR('Invalid section <%s> in <%s>.' % (desc[1], _INPUT_HANDLER_CFG))

        return

    def __onArenaStarted(self, period, *args):
        self.__isArenaStarted = True if period == ARENA_PERIOD.BATTLE else False
        show = self.__isGUIVisible and self.__isArenaStarted
        self.__curCtrl.showGunMarker2(show and control_modes.useServerAim())
        if constants.HAS_DEV_RESOURCES:
            showArcadeAim = show
        else:
            showArcadeAim = show and not control_modes.useServerAim()
        self.__curCtrl.showGunMarker(showArcadeAim)

    def __onRecreateDevice(self):
        self.__curCtrl.onRecreateDevice()
        self.__targeting.onRecreateDevice()

    def __onSettingsChanged(self, diff):
        from account_helpers.settings_core.SettingsCore import g_settingsCore
        if 'dynamicCamera' in diff or 'horStabilizationSnp' in diff:
            dynamicCamera = g_settingsCore.getSetting('dynamicCamera')
            horStabilizationSnp = g_settingsCore.getSetting('horStabilizationSnp')
            self.enableDynamicCamera(dynamicCamera, horStabilizationSnp)

    def __addBattleCtrlListeners(self):
        ammoCtrl = _getAmmoGuiCtrl()
        if ammoCtrl is not None:
            ammoCtrl.onGunReloadTimeSet += self.__onGunReloadTimeSet
        return

    def __removeBattleCtrlListeners(self):
        ammoCtrl = _getAmmoGuiCtrl()
        if ammoCtrl is not None:
            ammoCtrl.onGunReloadTimeSet -= self.__onGunReloadTimeSet
        return

    def __onGunReloadTimeSet(self, _, state):
        valueType = state.getValueType()
        if valueType == GUN_RELOADING_VALUE_TYPE.TIME:
            self.setReloading(state.getActualValue(), None, state.getBaseValue())
        elif valueType == GUN_RELOADING_VALUE_TYPE.PERCENT:
            self.setReloadingInPercent(state.getActualValue())
        return


class _Targeting():

    def __init__(self):
        target = BigWorld.target
        target.selectionFovDegrees = 1.0
        target.deselectionFovDegrees = 80.0
        target.maxDistance = 710.0
        target.skeletonCheckEnabled = True
        BigWorld.target.isEnabled = False
        self.__mouseMatProv = BigWorld.MouseTargettingMatrix()

    def isEnabled(self):
        return BigWorld.target.isEnabled

    def getTargetEntity(self):
        return BigWorld.target.entity

    def enable(self, flag):
        if flag and not BigWorld.target.isEnabled:
            player = BigWorld.player()
            player.targetBlur(player.target)
            BigWorld.target.isEnabled = True
            BigWorld.target.source = self.__mouseMatProv
        elif not flag:
            BigWorld.target.isEnabled = False
            BigWorld.target.clear()
            BigWorld.target.source = None
        return

    def onRecreateDevice(self):
        if BigWorld.target.isEnabled:
            BigWorld.target.clear()

    def detach(self, value):
        self.__mouseMatProv.detach(value)


class _VertScreenshotCamera(object):
    isEnabled = property(lambda self: self.__isEnabled)

    def __init__(self):
        self.__isEnabled = False
        self.__watcherNames = ('Render/Fov', 'Render/Near Plane', 'Render/Far Plane', 'Render/Objects Far Plane/Enabled', 'Render/Shadows/qualityPreset', 'Visibility/Draw tanks', 'Visibility/Control Points', 'Visibility/GUI', 'Visibility/particles', 'Client Settings/std fog/enabled', 'Client Settings/Script tick')

    def destroy(self):
        self.enable(False)

    def enable(self, doEnable):
        if self.__isEnabled == doEnable:
            return
        from cameras import FovExtended
        if not doEnable:
            self.__isEnabled = False
            BigWorld.camera(self.__savedCamera)
            BigWorld.wg_enableSuperShot(False, False)
            for k, v in self.__savedWatchers.iteritems():
                BigWorld.setWatcher(k, v)

            FovExtended.instance().enabled = True
            LOG_DEBUG('Vertical screenshot camera is disabled')
            return
        self.__isEnabled = True
        self.__savedCamera = BigWorld.camera()
        FovExtended.instance().enabled = False
        arenaBB = BigWorld.wg_getSpaceBounds()
        centerXZ = Math.Vector2(0.5 * (arenaBB[0] + arenaBB[2]), 0.5 * (arenaBB[1] + arenaBB[3]))
        halfSizesXZ = Math.Vector2(0.5 * (arenaBB[2] - arenaBB[0]), 0.5 * (arenaBB[3] - arenaBB[1]))
        camFov = math.radians(15.0)
        camPos = Math.Vector3(centerXZ.x, 0, centerXZ.z)
        aspectRatio = 1.0
        if not BigWorld.isVideoWindowed():
            aspectRatio = BigWorld.getFullScreenAspectRatio()
        else:
            aspectRatio = BigWorld.screenWidth() / BigWorld.screenHeight()
        camPos.y = max(halfSizesXZ.x / math.sin(0.5 * camFov * aspectRatio), halfSizesXZ.y / math.sin(0.5 * camFov))
        camMatr = Math.Matrix()
        camMatr.setRotateYPR(Math.Vector3(0.0, math.pi * 0.5, 0.0))
        camMatr.translation = camPos
        camMatr.invert()
        self.__cam = BigWorld.FreeCamera()
        self.__cam.set(camMatr)
        BigWorld.camera(self.__cam)
        BigWorld.wg_enableSuperShot(True, False)
        self.__savedWatchers = {}
        for name in self.__watcherNames:
            try:
                self.__savedWatchers[name] = BigWorld.getWatcher(name)
                if name.startswith('Visibility'):
                    BigWorld.setWatcher(name, False)
            except TypeError:
                LOG_WARNING('Failed to get/set watcher', name)

        BigWorld.setWatcher('Client Settings/std fog/enabled', False)
        BigWorld.projection().fov = camFov
        BigWorld.setWatcher('Render/Fov', camFov)
        BigWorld.setWatcher('Render/Near Plane', max(0.1, camPos.y - 1000.0))
        BigWorld.setWatcher('Render/Far Plane', camPos.y + 1000.0)
        BigWorld.setWatcher('Render/Objects Far Plane/Enabled', False)
        BigWorld.setWatcher('Render/Shadows/qualityPreset', 7)
        BigWorld.setWatcher('Client Settings/Script tick', False)
        LOG_DEBUG('Vertical screenshot camera is enabled')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\avatarinputhandler\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:48:14 St�edn� Evropa (letn� �as)
