# 2016.08.04 19:51:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RallyMainWindowWithSearchMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyMainWindow import BaseRallyMainWindow

class RallyMainWindowWithSearchMeta(BaseRallyMainWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyMainWindow
    null
    """

    def onAutoMatch(self, value, values):
        """
        :param value:
        :param values:
        :return :
        """
        self._printOverrideError('onAutoMatch')

    def autoSearchApply(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('autoSearchApply')

    def autoSearchCancel(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('autoSearchCancel')

    def as_autoSearchEnableBtnS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_autoSearchEnableBtn(value)

    def as_changeAutoSearchStateS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchState(value)

    def as_changeAutoSearchBtnsStateS(self, waitingPlayers, searchEnemy):
        """
        :param waitingPlayers:
        :param searchEnemy:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_changeAutoSearchBtnsState(waitingPlayers, searchEnemy)

    def as_hideAutoSearchS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideAutoSearch()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\rallymainwindowwithsearchmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:46 St�edn� Evropa (letn� �as)
