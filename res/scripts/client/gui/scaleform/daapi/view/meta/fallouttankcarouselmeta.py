# 2016.08.04 19:51:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutTankCarouselMeta.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel

class FalloutTankCarouselMeta(TankCarousel):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends TankCarousel
    null
    """

    def changeVehicle(self, id):
        """
        :param id:
        :return :
        """
        self._printOverrideError('changeVehicle')

    def clearSlot(self, vehicleId):
        """
        :param vehicleId:
        :return :
        """
        self._printOverrideError('clearSlot')

    def shiftSlot(self, vehicleId):
        """
        :param vehicleId:
        :return :
        """
        self._printOverrideError('shiftSlot')

    def as_setMultiselectionInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMultiselectionInfo(data)

    def as_getMultiselectionDPS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getMultiselectionDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\fallouttankcarouselmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:36 Støední Evropa (letní èas)
