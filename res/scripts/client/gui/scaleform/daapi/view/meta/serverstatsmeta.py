# 2016.08.04 19:51:47 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ServerStatsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ServerStatsMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def relogin(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('relogin')

    def startListenCsisUpdate(self, startListenCsis):
        """
        :param startListenCsis:
        :return :
        """
        self._printOverrideError('startListenCsisUpdate')

    def as_changePeripheryFailedS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changePeripheryFailed()

    def as_disableRoamingDDS(self, disable):
        """
        :param disable:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_disableRoamingDD(disable)

    def as_setServerStatsS(self, stats, tooltipType):
        """
        :param stats:
        :param tooltipType:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setServerStatsInfoS(self, tooltipFullData):
        """
        :param tooltipFullData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStatsInfo(tooltipFullData)

    def as_getServersDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()

    def as_setSelectedServerIndexS(self, index):
        """
        :param index:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedServerIndex(index)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\serverstatsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:47 St�edn� Evropa (letn� �as)
