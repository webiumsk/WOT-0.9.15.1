# 2016.08.04 19:49:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/legacy/damage_info_panel.py
from gui.battle_control import g_sessionProvider
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as _EVENT_ID

class VehicleDamageInfoPanel(object):

    def __init__(self, parent):
        self.__parent = parent
        self.__isShown = False

    def start(self):
        feedback = g_sessionProvider.shared.feedback
        if feedback is not None:
            feedback.onVehicleFeedbackReceived += self.__onVehicleFeedbackReceived
        return

    def destroy(self):
        feedback = g_sessionProvider.shared.feedback
        if feedback is not None:
            feedback.onVehicleFeedbackReceived -= self.__onVehicleFeedbackReceived
        return

    def __show(self, vehicleID, fetcher):
        itemsList = []
        for deviceName, state in fetcher.getDamagedDevices():
            itemsList.append({'name': deviceName,
             'state': state})

        self.__parent.movie.showDamageInfoPanel(vehicleID, itemsList, fetcher.isInFire())
        self.__isShown = True

    def __hide(self):
        if not self.__isShown:
            return
        self.__parent.movie.hideDamageInfoPanel()
        self.__isShown = False

    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        if eventID == _EVENT_ID.SHOW_VEHICLE_DAMAGES_DEVICES:
            self.__show(vehicleID, value)
        elif eventID == _EVENT_ID.HIDE_VEHICLE_DAMAGES_DEVICES:
            self.__hide()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\legacy\damage_info_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:46 St�edn� Evropa (letn� �as)
