# 2016.08.04 19:51:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleEndWarningPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleEndWarningPanelMeta(BaseDAAPIComponent):
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

    def as_setTextInfoS(self, text):
        """
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTextInfo(text)

    def as_setStateS(self, isShow):
        """
        :param isShow:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(isShow)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\battleendwarningpanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:28 Støední Evropa (letní èas)
