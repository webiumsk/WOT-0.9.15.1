# 2016.08.04 19:51:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CursorMeta.py
from gui.Scaleform.framework.entities.View import View

class CursorMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    null
    """

    def as_setCursorS(self, cursor):
        """
        :param cursor:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCursor(cursor)

    def as_showCursorS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showCursor()

    def as_hideCursorS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideCursor()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\cursormeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:33 Støední Evropa (letní èas)
