# 2016.08.04 19:51:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleTimerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setTotalTimeS(self, minutes, seconds):
        """
        :param minutes:
        :param seconds:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalTime(minutes, seconds)

    def as_setColorS(self, criticalColor):
        """
        :param criticalColor:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setColor(criticalColor)

    def as_showBattleTimerS(self, show):
        """
        :param show:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showBattleTimer(show)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\battletimermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:29 Støední Evropa (letní èas)
