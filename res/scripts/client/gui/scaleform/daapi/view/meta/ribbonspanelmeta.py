# 2016.08.04 19:51:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RibbonsPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RibbonsPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onShow(self):
        """
        :return :
        """
        self._printOverrideError('onShow')

    def onChange(self):
        """
        :return :
        """
        self._printOverrideError('onChange')

    def onIncCount(self):
        """
        :return :
        """
        self._printOverrideError('onIncCount')

    def onHide(self):
        """
        :return :
        """
        self._printOverrideError('onHide')

    def as_setupS(self, isEnabled, isPlaySounds):
        """
        :param isEnabled:
        :param isPlaySounds:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setup(isEnabled, isPlaySounds)

    def as_addBattleEfficiencyEventS(self, type, title, count):
        """
        :param type:
        :param title:
        :param count:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_addBattleEfficiencyEvent(type, title, count)

    def as_setOffsetXS(self, offsetX):
        """
        :param offsetX:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOffsetX(offsetX)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\ribbonspanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:47 Støední Evropa (letní èas)
