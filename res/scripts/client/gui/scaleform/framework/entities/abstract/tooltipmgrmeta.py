# 2016.08.04 19:51:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ToolTipMgrMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ToolTipMgrMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def onCreateComplexTooltip(self, tooltipId, stateType):
        """
        :param tooltipId:
        :param stateType:
        :return :
        """
        self._printOverrideError('onCreateComplexTooltip')

    def onCreateTypedTooltip(self, tooltipType, args, stateType):
        """
        :param tooltipType:
        :param args:
        :param stateType:
        :return :
        """
        self._printOverrideError('onCreateTypedTooltip')

    def as_showS(self, tooltipData, linkage):
        """
        :param tooltipData:
        :param linkage:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_show(tooltipData, linkage)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\tooltipmgrmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:57 St�edn� Evropa (letn� �as)
