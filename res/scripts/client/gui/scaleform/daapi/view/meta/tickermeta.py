# 2016.08.04 19:51:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TickerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TickerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def showBrowser(self, entryID):
        """
        :param entryID:
        :return :
        """
        self._printOverrideError('showBrowser')

    def as_setItemsS(self, items):
        """
        :param items:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\tickermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:50 St�edn� Evropa (letn� �as)
