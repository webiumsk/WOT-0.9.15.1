# 2016.08.04 19:51:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortOrderPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FortOrderPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def requestForCreateOrder(self):
        """
        :return :
        """
        self._printOverrideError('requestForCreateOrder')

    def requestForUseOrder(self):
        """
        :return :
        """
        self._printOverrideError('requestForUseOrder')

    def getLeftTime(self):
        """
        :return Number:
        """
        self._printOverrideError('getLeftTime')

    def getLeftTimeStr(self):
        """
        :return String:
        """
        self._printOverrideError('getLeftTimeStr')

    def getLeftTimeTooltip(self):
        """
        :return String:
        """
        self._printOverrideError('getLeftTimeTooltip')

    def openQuest(self, questID):
        """
        :param questID:
        :return :
        """
        self._printOverrideError('openQuest')

    def openOrderDetailsWindow(self):
        """
        :return :
        """
        self._printOverrideError('openOrderDetailsWindow')

    def as_setInitDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_disableOrderS(self, daisable):
        """
        :param daisable:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_disableOrder(daisable)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fortorderpopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:39 St�edn� Evropa (letn� �as)
