# 2016.08.04 19:51:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattlePageMeta.py
from gui.Scaleform.framework.entities.View import View

class BattlePageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def as_checkDAAPIS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_checkDAAPI()

    def as_setPostmortemTipsVisibleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortemTipsVisible(value)

    def as_setComponentsVisibilityS(self, visible, hidden):
        """
        :param visible:
        :param hidden:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setComponentsVisibility(visible, hidden)

    def as_isComponentVisibleS(self, componentKey):
        """
        :param componentKey:
        :return Boolean:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_isComponentVisible(componentKey)

    def as_getComponentsVisibilityS(self):
        """
        :return Array:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getComponentsVisibility()

    def as_toggleCtrlPressFlagS(self, isCtrlPressed):
        """
        :param isCtrlPressed:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_toggleCtrlPressFlag(isCtrlPressed)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\battlepagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:28 St�edn� Evropa (letn� �as)
