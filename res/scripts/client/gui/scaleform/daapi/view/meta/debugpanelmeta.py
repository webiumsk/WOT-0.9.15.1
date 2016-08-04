# 2016.08.04 19:51:34 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DebugPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DebugPanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_updatePingInfoS(self, pingValue):
        """
        :param pingValue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingInfo(pingValue)

    def as_updateFPSInfoS(self, fpsValue):
        """
        :param fpsValue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFPSInfo(fpsValue)

    def as_updateLagInfoS(self, isLagging):
        """
        :param isLagging:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateLagInfo(isLagging)

    def as_updatePingFPSInfoS(self, pingValue, fpsValue):
        """
        :param pingValue:
        :param fpsValue:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPSInfo(pingValue, fpsValue)

    def as_updatePingFPSLagInfoS(self, pingValue, fpsValue, isLagging):
        """
        :param pingValue:
        :param fpsValue:
        :param isLagging:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPSLagInfo(pingValue, fpsValue, isLagging)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\debugpanelmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:34 Støední Evropa (letní èas)
