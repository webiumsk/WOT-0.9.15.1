# 2016.08.04 19:48:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/avatar_helpers/AvatarSyncData.py
import AccountCommands
from debug_utils import *

class AvatarSyncData(object):

    def __init__(self):
        self.__isSynchronized = False
        self.__subscribers = []
        self.__avatar = None
        return

    def setAvatar(self, avatar):
        self.__avatar = avatar

    def onAvatarBecomePlayer(self):
        self.__isSynchronized = self.__avatar.isSynchronized()
        if not self.__isSynchronized:
            self.__avatar._doCmdStr(AccountCommands.CMD_GET_AVATAR_SYNC, '', self.__onSyncResponse)

    def onAvatarBecomeNonPlayer(self):
        pass

    def waitForSync(self, callback):
        if self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)
        if callback is not None:
            self.__subscribers.append(callback)
        return

    def __onSyncResponse(self, syncID, resultID, ext = {}):
        self.__isSynchronized = True
        subscribers = self.__subscribers
        self.__subscribers = []
        for callback in subscribers:
            callback(resultID)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\avatar_helpers\avatarsyncdata.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:48:17 St�edn� Evropa (letn� �as)
