# 2016.08.04 19:51:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class CyberSportIntroMeta(BaseRallyIntroView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyIntroView
    null
    """

    def requestVehicleSelection(self):
        """
        :return :
        """
        self._printOverrideError('requestVehicleSelection')

    def startAutoMatching(self):
        """
        :return :
        """
        self._printOverrideError('startAutoMatching')

    def showSelectorPopup(self):
        """
        :return :
        """
        self._printOverrideError('showSelectorPopup')

    def showStaticTeamProfile(self):
        """
        :return :
        """
        self._printOverrideError('showStaticTeamProfile')

    def cancelWaitingTeamRequest(self):
        """
        :return :
        """
        self._printOverrideError('cancelWaitingTeamRequest')

    def showStaticTeamStaff(self):
        """
        :return :
        """
        self._printOverrideError('showStaticTeamStaff')

    def joinClubUnit(self):
        """
        :return :
        """
        self._printOverrideError('joinClubUnit')

    def as_setSelectedVehicleS(self, selectedVehicleData, selectedVehicleIsReady, warnTooltip):
        """
        :param selectedVehicleData:
        :param selectedVehicleIsReady:
        :param warnTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicle(selectedVehicleData, selectedVehicleIsReady, warnTooltip)

    def as_setTextsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTexts(data)

    def as_setStaticTeamDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticTeamData(data)

    def as_setNoVehiclesS(self, warnTooltip):
        """
        :param warnTooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setNoVehicles(warnTooltip)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportintrometa.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:33 St�edn� Evropa (letn� �as)
