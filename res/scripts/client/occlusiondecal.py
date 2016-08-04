# 2016.08.04 19:47:44 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/OcclusionDecal.py
import BigWorld
from vehicle_systems.tankStructure import TankPartNames

class OcclusionDecal:

    @staticmethod
    def isEnabled():
        return BigWorld.isForwardPipeline() is False and BigWorld.isSSAOEnabled() and BigWorld.isShadowsEnabled()

    def __init__(self):
        self.__attached = False
        self.__vehicle = None
        self.__model = None
        self.__chassisDecals = []
        self.__chassisParent = None
        self.__hullDecals = []
        self.__hullParent = None
        self.__turretDecals = []
        self.__turretParent = None
        from account_helpers.settings_core.SettingsCore import g_settingsCore
        g_settingsCore.onSettingsChanged += self.onSettingsChanged
        return

    def destroy(self):
        from account_helpers.settings_core.SettingsCore import g_settingsCore
        g_settingsCore.onSettingsChanged -= self.onSettingsChanged
        self.__vehicle = None
        self.__model = None
        self.detach()
        return

    def attach(self, vehicle, model, isSettingChanged = False):
        self.__vehicle = vehicle
        self.__model = model
        if not isSettingChanged:
            if not OcclusionDecal.isEnabled() or self.__attached:
                return
        elif self.__attached:
            return
        self.__attached = True
        self.__chassisParent = model.root
        for transform in vehicle.typeDescriptor.chassis['AODecals']:
            decal = OcclusionDecal.__createDecal(transform, self.__chassisParent, False)
            self.__chassisDecals.append(decal)

        self.__hullParent = model.node(TankPartNames.HULL)
        for transform in vehicle.typeDescriptor.hull['AODecals']:
            decal = OcclusionDecal.__createDecal(transform, self.__hullParent, True)
            self.__hullDecals.append(decal)

        self.__turretParent = model.node(TankPartNames.TURRET)
        for transform in vehicle.typeDescriptor.turret['AODecals']:
            decal = OcclusionDecal.__createDecal(transform, self.__turretParent, True)
            self.__turretDecals.append(decal)

    def detach(self):
        if not self.__attached:
            return
        else:
            self.__attached = False
            for decal in self.__chassisDecals:
                self.__chassisParent.detach(decal)

            self.__chassisDecals = []
            self.__chassisParent = None
            for decal in self.__hullDecals:
                self.__hullParent.detach(decal)

            self.__hullDecals = []
            self.__hullParent = None
            for decal in self.__turretDecals:
                self.__turretParent.detach(decal)

            self.__turretDecals = []
            self.__turretParent = None
            return

    def __reattach(self):
        if self.__attached:
            return
        elif self.__vehicle is None or self.__model is None:
            return
        else:
            self.attach(self.__vehicle, self.__model, True)
            return

    def onSettingsChanged(self, diff = None):
        enabled = False
        if 'SHADOWS_QUALITY' in diff:
            value = diff['SHADOWS_QUALITY']
            if value < 4 and OcclusionDecal.isEnabled():
                enabled = True
            if enabled:
                self.__reattach()
            else:
                self.detach()

    @staticmethod
    def __createDecal(transform, parentNode, applyToAll):
        diffuseTexture = ''
        bumpTexture = ''
        hmTexture = ''
        addTexture = 'maps/spots/TankOcclusion/TankOcclusionMap.dds'
        priority = 0
        materialType = 4
        visibilityMask = 4294967295L
        accuracy = 2
        influence = 30
        if applyToAll:
            influence = 62
        decal = BigWorld.WGOcclusionDecal()
        decal.create(diffuseTexture, bumpTexture, hmTexture, addTexture, priority, materialType, influence, visibilityMask, accuracy)
        decal.setLocalTransform(transform)
        parentNode.attach(decal)
        return decal
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\occlusiondecal.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:47:44 St�edn� Evropa (letn� �as)
