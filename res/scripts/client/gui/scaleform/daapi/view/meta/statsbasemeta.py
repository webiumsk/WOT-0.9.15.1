# 2016.08.04 19:51:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StatsBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatsBaseMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def acceptSquad(self, uid):
        """
        :param uid:
        :return :
        """
        self._printOverrideError('acceptSquad')

    def addToSquad(self, uid):
        """
        :param uid:
        :return :
        """
        self._printOverrideError('addToSquad')

    def as_setIsIntaractiveS(self, value):
        """
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIsIntaractive(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\statsbasemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:49 Støední Evropa (letní èas)
