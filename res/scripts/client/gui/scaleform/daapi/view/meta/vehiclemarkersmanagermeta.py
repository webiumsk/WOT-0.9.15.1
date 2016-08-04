# 2016.08.04 19:51:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleMarkersManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleMarkersManagerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    null
    """

    def as_setMarkerDurationS(self, duration):
        """
        :param duration:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerDuration(duration)

    def as_setMarkerSettingsS(self, settings):
        """
        :param settings:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMarkerSettings(settings)

    def as_setShowExInfoFlagS(self, flag):
        """
        :param flag:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setShowExInfoFlag(flag)

    def as_updateMarkersSettingsS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateMarkersSettings()

    def as_setColorBlindS(self, isColorBlind):
        """
        :param isColorBlind:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setColorBlind(isColorBlind)

    def as_setColorSchemesS(self, defaultSchemes, colorBlindSchemes):
        """
        :param defaultSchemes:
        :param colorBlindSchemes:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setColorSchemes(defaultSchemes, colorBlindSchemes)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\vehiclemarkersmanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:51 Støední Evropa (letní èas)
