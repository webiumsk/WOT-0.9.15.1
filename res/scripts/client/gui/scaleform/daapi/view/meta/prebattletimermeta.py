# 2016.08.04 19:51:43 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PrebattleTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PrebattleTimerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setTimerS(self, totalTime):
        """
        :param totalTime:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(totalTime)

    def as_setMessageS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(msg)

    def as_hideTimerS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideTimer()

    def as_hideAllS(self, speed):
        """
        :param speed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideAll(speed)

    def as_setWinConditionTextS(self, msg):
        """
        :param msg:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWinConditionText(msg)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\prebattletimermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:43 St�edn� Evropa (letn� �as)
