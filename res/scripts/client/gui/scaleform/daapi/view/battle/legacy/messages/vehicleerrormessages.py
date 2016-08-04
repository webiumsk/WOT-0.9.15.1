# 2016.08.04 19:49:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/legacy/messages/VehicleErrorMessages.py
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.legacy.messages.FadingMessages import FadingMessages
from gui.battle_control import g_sessionProvider

class VehicleErrorMessages(FadingMessages):

    def __init__(self, parentUI):
        super(VehicleErrorMessages, self).__init__(parentUI, 'VehicleErrorsPanel', 'gui/legacy_vehicle_errors.xml')

    def __del__(self):
        LOG_DEBUG('VehicleErrorMessages panel is deleted')

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey
        return

    def _removeGameListeners(self):
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        super(VehicleErrorMessages, self)._removeGameListeners()
        return

    def __onShowVehicleErrorByKey(self, key, args = None, extra = None):
        self.showMessage(key, args, extra)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\legacy\messages\vehicleerrormessages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:51 Støední Evropa (letní èas)
