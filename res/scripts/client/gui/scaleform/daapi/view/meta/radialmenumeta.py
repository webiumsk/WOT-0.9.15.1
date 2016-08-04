# 2016.08.04 19:51:45 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadialMenuMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadialMenuMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def onSelect(self):
        """
        :return :
        """
        self._printOverrideError('onSelect')

    def onAction(self, action):
        """
        :param action:
        :return :
        """
        self._printOverrideError('onAction')

    def as_buildDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_buildData(data)

    def as_showS(self, radialState, offset, ratio):
        """
        :param radialState:
        :param offset:
        :param ratio:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_show(radialState, offset, ratio)

    def as_hideS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\radialmenumeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:45 Støední Evropa (letní èas)
