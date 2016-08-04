# 2016.08.04 19:51:49 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankCarouselMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TankCarouselMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def selectVehicle(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('selectVehicle')

    def buyTank(self):
        """
        :return :
        """
        self._printOverrideError('buyTank')

    def buySlot(self):
        """
        :return :
        """
        self._printOverrideError('buySlot')

    def setFilter(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('setFilter')

    def resetFilters(self):
        """
        :return :
        """
        self._printOverrideError('resetFilters')

    def as_getDataProviderS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setCarouselFilterS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselFilter(data)

    def as_initCarouselFilterS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initCarouselFilter(data)

    def as_showCounterS(self, countText, isAttention):
        """
        :param countText:
        :param isAttention:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_hideCounterS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\tankcarouselmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:49 Støední Evropa (letní èas)
