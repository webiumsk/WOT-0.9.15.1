# 2016.08.04 19:51:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnFormMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportRespawnFormMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    null
    """

    def as_updateEnemyStatusS(self, statusID, enemyStatusLabel):
        """
        :param statusID:
        :param enemyStatusLabel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateEnemyStatus(statusID, enemyStatusLabel)

    def as_setTeamNameS(self, name):
        """
        :param name:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamName(name)

    def as_setTeamEmblemS(self, teamEmblemId):
        """
        :param teamEmblemId:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamEmblem(teamEmblemId)

    def as_setArenaTypeIdS(self, mapName, arenaTypeID):
        """
        :param mapName:
        :param arenaTypeID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaTypeId(mapName, arenaTypeID)

    def as_timerUpdateS(self, timeLeft):
        """
        :param timeLeft:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_timerUpdate(timeLeft)

    def as_statusUpdateS(self, status, level, tooltip):
        """
        :param status:
        :param level:
        :param tooltip:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_statusUpdate(status, level, tooltip)

    def as_setTotalLabelS(self, hasTotalLevelError, totalLevelLabel, totalLevel):
        """
        :param hasTotalLevelError:
        :param totalLevelLabel:
        :param totalLevel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLabel(hasTotalLevelError, totalLevelLabel, totalLevel)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cybersportrespawnformmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:33 St�edn� Evropa (letn� �as)
