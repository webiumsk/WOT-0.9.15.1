# 2016.08.04 19:51:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LobbyMenuMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def settingsClick(self):
        """
        :return :
        """
        self._printOverrideError('settingsClick')

    def cancelClick(self):
        """
        :return :
        """
        self._printOverrideError('cancelClick')

    def refuseTraining(self):
        """
        :return :
        """
        self._printOverrideError('refuseTraining')

    def logoffClick(self):
        """
        :return :
        """
        self._printOverrideError('logoffClick')

    def quitClick(self):
        """
        :return :
        """
        self._printOverrideError('quitClick')

    def versionInfoClick(self):
        """
        :return :
        """
        self._printOverrideError('versionInfoClick')

    def as_setVersionMessageS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVersionMessage(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\lobbymenumeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:42 St�edn� Evropa (letn� �as)
