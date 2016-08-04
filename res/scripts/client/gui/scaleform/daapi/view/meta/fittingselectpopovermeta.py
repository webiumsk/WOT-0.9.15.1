# 2016.08.04 19:51:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def setVehicleModule(self, newId, oldId, isRemove):
        """
        :param newId:
        :param oldId:
        :param isRemove:
        :return :
        """
        self._printOverrideError('setVehicleModule')

    def showModuleInfo(self, moduleId):
        """
        :param moduleId:
        :return :
        """
        self._printOverrideError('showModuleInfo')

    def as_updateS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fittingselectpopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:36 Støední Evropa (letní èas)
