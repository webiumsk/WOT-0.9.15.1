# 2016.08.04 19:51:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutRespawnViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutRespawnViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onVehicleSelected(self, vehicleID):
        """
        :param vehicleID:
        :return :
        """
        self._printOverrideError('onVehicleSelected')

    def onPostmortemBtnClick(self):
        """
        :return :
        """
        self._printOverrideError('onPostmortemBtnClick')

    def as_initializeS(self, mainData, slotsData):
        """
        :param mainData:
        :param slotsData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initialize(mainData, slotsData)

    def as_updateTimerS(self, mainTimer, slotsStateData):
        """
        :param mainTimer:
        :param slotsStateData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(mainTimer, slotsStateData)

    def as_updateS(self, selectedVehicleName, slotsStateData):
        """
        :param selectedVehicleName:
        :param slotsStateData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(selectedVehicleName, slotsStateData)

    def as_showGasAttackModeS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showGasAttackMode()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\falloutrespawnviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:35 St�edn� Evropa (letn� �as)
