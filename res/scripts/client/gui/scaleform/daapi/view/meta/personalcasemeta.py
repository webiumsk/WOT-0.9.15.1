# 2016.08.04 19:51:43 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalCaseMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class PersonalCaseMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def dismissTankman(self, inventoryID):
        """
        :param inventoryID:
        :return :
        """
        self._printOverrideError('dismissTankman')

    def unloadTankman(self, invengoryid, currentVehicleID):
        """
        :param invengoryid:
        :param currentVehicleID:
        :return :
        """
        self._printOverrideError('unloadTankman')

    def getCommonData(self):
        """
        :return :
        """
        self._printOverrideError('getCommonData')

    def getDossierData(self):
        """
        :return :
        """
        self._printOverrideError('getDossierData')

    def getRetrainingData(self):
        """
        :return :
        """
        self._printOverrideError('getRetrainingData')

    def retrainingTankman(self, inventoryID, innationID, tankmanCostTypeIndex):
        """
        :param inventoryID:
        :param innationID:
        :param tankmanCostTypeIndex:
        :return :
        """
        self._printOverrideError('retrainingTankman')

    def getSkillsData(self):
        """
        :return :
        """
        self._printOverrideError('getSkillsData')

    def getDocumentsData(self):
        """
        :return :
        """
        self._printOverrideError('getDocumentsData')

    def addTankmanSkill(self, invengoryID, skillName):
        """
        :param invengoryID:
        :param skillName:
        :return :
        """
        self._printOverrideError('addTankmanSkill')

    def dropSkills(self):
        """
        :return :
        """
        self._printOverrideError('dropSkills')

    def changeTankmanPassport(self, invengoryID, firstNameID, firstNameGroup, lastNameID, lastNameGroup, iconID, iconGroup):
        """
        :param invengoryID:
        :param firstNameID:
        :param firstNameGroup:
        :param lastNameID:
        :param lastNameGroup:
        :param iconID:
        :param iconGroup:
        :return :
        """
        self._printOverrideError('changeTankmanPassport')

    def openExchangeFreeToTankmanXpWindow(self):
        """
        :return :
        """
        self._printOverrideError('openExchangeFreeToTankmanXpWindow')

    def openChangeRoleWindow(self):
        """
        :return :
        """
        self._printOverrideError('openChangeRoleWindow')

    def as_setCommonDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonData(data)

    def as_setDossierDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDossierData(data)

    def as_setRetrainingDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setRetrainingData(data)

    def as_setSkillsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setSkillsData(data)

    def as_setDocumentsDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDocumentsData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\personalcasemeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:43 St�edn� Evropa (letn� �as)
