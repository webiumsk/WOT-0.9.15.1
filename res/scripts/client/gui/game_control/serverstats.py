# 2016.08.04 19:49:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/ServerStats.py
import BigWorld
import constants
import Event
from PlayerEvents import g_playerEvents
from gui import makeHtmlString
from gui.shared.formatters import text_styles
from gui.game_control.controllers import Controller

class ServerStats(Controller):
    STATS_REQUEST_TIMEOUT = 5.0

    class TOOLTIP_TYPE:
        TYPE_UNAVAILABLE = ('unavailable',)
        TYPE_CLUSTER = ('clusterCCU',)
        TYPE_FULL = 'regionCCU/clusterCCU'

    onStatsReceived = Event.Event()

    def __init__(self, proxy):
        super(ServerStats, self).__init__(proxy)
        self.__statsCallbackID = None
        self.__stats = {}
        return

    def onLobbyStarted(self, ctx):
        g_playerEvents.onServerStatsReceived += self.__onStatsReceived
        self.__loadStatsCallback(0.0)

    def onAvatarBecomePlayer(self):
        self.__stop()

    def onDisconnected(self):
        self.__stop()

    def getStats(self):
        return self.__stats

    def getFormattedStats(self):
        clusterCCU = self.__stats.get('clusterCCU', 0)
        regionCCU = self.__stats.get('regionCCU', 0)
        if regionCCU:
            clusterUsers = text_styles.stats(BigWorld.wg_getIntegralFormat(clusterCCU))
            regionUsers = text_styles.main(' / ' + BigWorld.wg_getIntegralFormat(regionCCU))
            if clusterCCU == regionCCU:
                tooltipType = self.TOOLTIP_TYPE.TYPE_CLUSTER
                statsStr = clusterUsers
            else:
                tooltipType = self.TOOLTIP_TYPE.TYPE_FULL
                statsStr = clusterUsers + regionUsers
        else:
            tooltipType = self.TOOLTIP_TYPE.TYPE_UNAVAILABLE
            statsStr = text_styles.main('- / -')
        return (statsStr, tooltipType)

    def __stop(self):
        g_playerEvents.onServerStatsReceived -= self.__onStatsReceived
        self.__clearStatsCallback()

    def __onStatsReceived(self, stats):
        self.__stats = dict(stats)
        self.onStatsReceived(self.__stats)
        self.__loadStatsCallback()

    def __requestServerStats(self):
        self.__clearStatsCallback()
        if hasattr(BigWorld.player(), 'requestServerStats'):
            BigWorld.player().requestServerStats()

    def __loadStatsCallback(self, timeout = None):
        if constants.IS_SHOW_SERVER_STATS:
            self.__statsCallbackID = BigWorld.callback(timeout if timeout is not None else self.STATS_REQUEST_TIMEOUT, self.__requestServerStats)
        return

    def __clearStatsCallback(self):
        if self.__statsCallbackID is not None:
            BigWorld.cancelCallback(self.__statsCallbackID)
            self.__statsCallbackID = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\game_control\serverstats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:02 St�edn� Evropa (letn� �as)
