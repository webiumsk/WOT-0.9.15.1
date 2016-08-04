# 2016.08.04 19:51:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsTileChainsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsTileChainsViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def getTileData(self, vehicleType, taskFilterType):
        """
        :param vehicleType:
        :param taskFilterType:
        :return :
        """
        self._printOverrideError('getTileData')

    def getChainProgress(self):
        """
        :return :
        """
        self._printOverrideError('getChainProgress')

    def getTaskDetails(self, taskId):
        """
        :param taskId:
        :return :
        """
        self._printOverrideError('getTaskDetails')

    def selectTask(self, taskId):
        """
        :param taskId:
        :return :
        """
        self._printOverrideError('selectTask')

    def refuseTask(self, taskId):
        """
        :param taskId:
        :return :
        """
        self._printOverrideError('refuseTask')

    def gotoBack(self):
        """
        :return :
        """
        self._printOverrideError('gotoBack')

    def showAwardVehicleInfo(self, awardVehicleID):
        """
        :param awardVehicleID:
        :return :
        """
        self._printOverrideError('showAwardVehicleInfo')

    def showAwardVehicleInHangar(self, awardVehicleID):
        """
        :param awardVehicleID:
        :return :
        """
        self._printOverrideError('showAwardVehicleInHangar')

    def as_setHeaderDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_updateTileDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTileData(data)

    def as_updateChainProgressS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateChainProgress(data)

    def as_updateTaskDetailsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTaskDetails(data)

    def as_setSelectedTaskS(self, taskId):
        """
        :param taskId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedTask(taskId)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\queststilechainsviewmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:45 St�edn� Evropa (letn� �as)
