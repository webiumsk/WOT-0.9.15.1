# 2016.08.04 19:47:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/AimTrigger.py
import BigWorld
import TriggersManager

class AimTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AIM, name=self.name, position=self.position, radius=self.radius, maxDistance=self.maxDistance)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\aimtrigger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:47:26 St�edn� Evropa (letn� �as)
