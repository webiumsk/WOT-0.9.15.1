# 2016.08.04 19:51:47 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SimpleDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SimpleDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onButtonClick(self, buttonId):
        """
        :param buttonId:
        :return :
        """
        self._printOverrideError('onButtonClick')

    def as_setTextS(self, text):
        """
        :param text:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setText(text)

    def as_setTitleS(self, title):
        """
        :param title:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setButtonsS(self, buttonNames):
        """
        :param buttonNames:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtons(buttonNames)

    def as_setButtonEnablingS(self, id, isEnabled):
        """
        :param id:
        :param isEnabled:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonEnabling(id, isEnabled)

    def as_setButtonFocusS(self, id):
        """
        :param id:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonFocus(id)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\simpledialogmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:47 St�edn� Evropa (letn� �as)
