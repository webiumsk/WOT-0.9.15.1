# 2016.08.04 19:51:36 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FlagNotificationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FlagNotificationMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setStateS(self, state):
        """
        :param state:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setActiveS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setActive(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\flagnotificationmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:36 St�edn� Evropa (letn� �as)
