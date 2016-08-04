# 2016.08.04 19:51:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MinimapMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MinimapMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def setAttentionToCell(self, x, y, isRightClick):
        """
        :param x:
        :param y:
        :param isRightClick:
        :return :
        """
        self._printOverrideError('setAttentionToCell')

    def as_setSizeS(self, size):
        """
        :param size:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSize(size)

    def as_setVisibleS(self, isVisible):
        """
        :param isVisible:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)

    def as_setAlphaS(self, alpha):
        """
        :param alpha:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAlpha(alpha)

    def as_showVehiclesNameS(self, visibility):
        """
        :param visibility:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showVehiclesName(visibility)

    def as_setBackgroundS(self, path):
        """
        :param path:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(path)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\minimapmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:42 Støední Evropa (letní èas)
