# 2016.08.04 19:51:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsCurrentTabMeta.py
from gui.Scaleform.daapi.view.lobby.server_events.QuestsTab import QuestsTab

class QuestsCurrentTabMeta(QuestsTab):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends QuestsTab
    null
    """

    def sort(self, type, hideDone):
        """
        :param type:
        :param hideDone:
        :return :
        """
        self._printOverrideError('sort')

    def getSortedTableData(self, tableData):
        """
        :param tableData:
        :return Array:
        """
        self._printOverrideError('getSortedTableData')

    def getQuestInfo(self, questID):
        """
        :param questID:
        :return :
        """
        self._printOverrideError('getQuestInfo')

    def as_updateQuestInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateQuestInfo(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\questscurrenttabmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:45 St�edn� Evropa (letn� �as)
