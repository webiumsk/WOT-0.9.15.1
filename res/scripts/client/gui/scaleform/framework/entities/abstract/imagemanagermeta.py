# 2016.08.04 19:51:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ImageManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class ImageManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def as_setImageCacheSettingsS(self, maxSize, minSize):
        """
        :param maxSize:
        :param minSize:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setImageCacheSettings(maxSize, minSize)

    def as_loadImagesS(self, sourceData):
        """
        :param sourceData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadImages(sourceData)

    def as_unloadImagesS(self, sourceData):
        """
        :param sourceData:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_unloadImages(sourceData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\imagemanagermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:56 Støední Evropa (letní èas)
