# 2016.08.04 19:49:41 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/classic/base_stats.py
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.battle_control import g_sessionProvider
from gui.shared import events, EVENT_BUS_SCOPE

class StatsBase(StatsBaseMeta):

    def acceptSquad(self, playerID):
        g_sessionProvider.invitations.accept(long(playerID))

    def addToSquad(self, playerID):
        g_sessionProvider.invitations.send(long(playerID))

    def _populate(self):
        self.addListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.addListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._populate()

    def _dispose(self):
        self.__invitations = None
        self.removeListener(events.GameEvent.SHOW_CURSOR, self.__handleShowCursor, EVENT_BUS_SCOPE.GLOBAL)
        self.removeListener(events.GameEvent.HIDE_CURSOR, self.__handleHideCursor, EVENT_BUS_SCOPE.GLOBAL)
        super(StatsBase, self)._dispose()
        return

    def __handleShowCursor(self, _):
        self.as_setIsIntaractiveS(True)

    def __handleHideCursor(self, _):
        self.as_setIsIntaractiveS(False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\classic\base_stats.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:41 St�edn� Evropa (letn� �as)
