# 2016.08.04 19:51:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ResearchMeta.py
from gui.Scaleform.daapi.view.lobby.techtree.ResearchView import ResearchView

class ResearchMeta(ResearchView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ResearchView
    null
    """

    def requestNationData(self):
        """
        :return Boolean:
        """
        self._printOverrideError('requestNationData')

    def getResearchItemsData(self, vehCD, rootChanged):
        """
        :param vehCD:
        :param rootChanged:
        :return Object:
        """
        self._printOverrideError('getResearchItemsData')

    def onResearchItemsDrawn(self):
        """
        :return :
        """
        self._printOverrideError('onResearchItemsDrawn')

    def goToTechTree(self, nation):
        """
        :param nation:
        :return :
        """
        self._printOverrideError('goToTechTree')

    def exitFromResearch(self):
        """
        :return :
        """
        self._printOverrideError('exitFromResearch')

    def goToVehicleView(self, itemCD):
        """
        :param itemCD:
        :return :
        """
        self._printOverrideError('goToVehicleView')

    def as_drawResearchItemsS(self, nation, vehCD):
        """
        :param nation:
        :param vehCD:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_drawResearchItems(nation, vehCD)

    def as_setFreeXPS(self, freeXP):
        """
        :param freeXP:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setFreeXP(freeXP)

    def as_setInstalledItemsS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInstalledItems(data)

    def as_setWalletStatusS(self, walletStatus):
        """
        :param walletStatus:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\researchmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:46 St�edn� Evropa (letn� �as)
