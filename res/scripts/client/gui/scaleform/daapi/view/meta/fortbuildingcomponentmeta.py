# 2016.08.04 19:51:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBuildingComponentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortBuildingComponentMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onTransportingRequest(self, exportFrom, importTo):
        """
        :param exportFrom:
        :param importTo:
        :return :
        """
        self._printOverrideError('onTransportingRequest')

    def requestBuildingProcess(self, direction, position):
        """
        :param direction:
        :param position:
        :return :
        """
        self._printOverrideError('requestBuildingProcess')

    def upgradeVisitedBuilding(self, uid):
        """
        :param uid:
        :return :
        """
        self._printOverrideError('upgradeVisitedBuilding')

    def requestBuildingToolTipData(self, uid, type):
        """
        :param uid:
        :param type:
        :return :
        """
        self._printOverrideError('requestBuildingToolTipData')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setBuildingDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingData(data)

    def as_setBuildingToolTipDataS(self, uid, type, header, value):
        """
        :param uid:
        :param type:
        :param header:
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBuildingToolTipData(uid, type, header, value)

    def as_refreshTransportingS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_refreshTransporting()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortbuildingcomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:36 St�edn� Evropa (letn� �as)
