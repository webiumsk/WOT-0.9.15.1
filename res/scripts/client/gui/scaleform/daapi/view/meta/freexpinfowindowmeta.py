# 2016.08.04 19:51:40 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FreeXPInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FreeXPInfoWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onSubmitButton(self):
        """
        :return :
        """
        self._printOverrideError('onSubmitButton')

    def onCancelButton(self):
        """
        :return :
        """
        self._printOverrideError('onCancelButton')

    def as_setSubmitLabelS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSubmitLabel(value)

    def as_setTitleS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setTextS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setText(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\freexpinfowindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:40 St�edn� Evropa (letn� �as)
