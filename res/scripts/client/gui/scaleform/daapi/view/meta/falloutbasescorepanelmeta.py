# 2016.08.04 19:51:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBaseScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutBaseScorePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_initS(self, maxValue, warningValue):
        """
        :param maxValue:
        :param warningValue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(maxValue, warningValue)

    def as_playScoreHighlightAnimS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_playScoreHighlightAnim()

    def as_stopScoreHighlightAnimS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_stopScoreHighlightAnim()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\falloutbasescorepanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:35 Støední Evropa (letní èas)
