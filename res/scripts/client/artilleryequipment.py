# 2016.08.04 19:47:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/ArtilleryEquipment.py
from AvatarInputHandler import mathUtils
import BigWorld
from Math import Vector3

class ArtilleryEquipment(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = mathUtils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.launchVelocity = launchDir * self.speed
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\artilleryequipment.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:47:28 St�edn� Evropa (letn� �as)
