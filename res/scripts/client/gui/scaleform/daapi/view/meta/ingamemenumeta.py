# 2016.08.04 19:51:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def quitBattleClick(self):
        """
        :return :
        """
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        """
        :return :
        """
        self._printOverrideError('settingsClick')

    def helpClick(self):
        """
        :return :
        """
        self._printOverrideError('helpClick')

    def cancelClick(self):
        """
        :return :
        """
        self._printOverrideError('cancelClick')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        """
        :param serverName:
        :param tooltipFullData:
        :param serverState:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)

    def as_setServerStatsS(self, stats, tooltipType):
        """
        :param stats:
        :param tooltipType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\ingamemenumeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:41 St�edn� Evropa (letn� �as)
