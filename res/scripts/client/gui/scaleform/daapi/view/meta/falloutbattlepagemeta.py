# 2016.08.04 19:51:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class FalloutBattlePageMeta(ClassicPage):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClassicPage
    null
    """

    def as_setPostmortemGasAtackInfoS(self, infoStr, respawnStr, showDeadIcon):
        """
        :param infoStr:
        :param respawnStr:
        :param showDeadIcon:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortemGasAtackInfo(infoStr, respawnStr, showDeadIcon)

    def as_hidePostmortemGasAtackInfoS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hidePostmortemGasAtackInfo()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\falloutbattlepagemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:35 Støední Evropa (letní èas)
