# 2016.08.04 19:53:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/ReadyForBattleMTAchievement.py
from abstract import ClassProgressAchievement, getCompletedPotapovQuestsCount
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB

class ReadyForBattleMTAchievement(ClassProgressAchievement):

    def __init__(self, dossier, value = None):
        self.__isCurrentUserAchievement = dossier.isCurrentUser() if dossier is not None else False
        super(ReadyForBattleMTAchievement, self).__init__('readyForBattleMT', _AB.TOTAL, dossier, value)
        return

    def getNextLevelInfo(self):
        return ('questsLeft', self._lvlUpValue if self.__isCurrentUserAchievement else 0)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TOTAL, 'readyForBattleMT')

    def _readCurrentProgressValue(self, dossier):
        return getCompletedPotapovQuestsCount(1, {'mediumTank'})
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\readyforbattlemtachievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:53:04 St�edn� Evropa (letn� �as)
