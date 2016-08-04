# 2016.08.04 19:53:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/__init__.py
from messenger.m_constants import MESSENGER_SCOPE

def setGUIEntries(decorator):
    from gui import GUI_SETTINGS
    from messenger.gui.Scaleform.battle_entry import BattleEntry
    from messenger.gui.Scaleform.lobby_entry import LobbyEntry
    from messenger.gui.Scaleform.legacy_entry import LegacyBattleEntry
    decorator.setEntry(MESSENGER_SCOPE.LOBBY, LobbyEntry())
    if GUI_SETTINGS.useAS3Battle:
        decorator.setEntry(MESSENGER_SCOPE.BATTLE, BattleEntry())
    else:
        decorator.setEntry(MESSENGER_SCOPE.BATTLE, LegacyBattleEntry())
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:53:57 St�edn� Evropa (letn� �as)
