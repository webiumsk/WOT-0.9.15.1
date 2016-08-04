# 2016.08.04 19:51:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CompanyRoomMeta.py
from gui.Scaleform.daapi.view.lobby.prb_windows.BasePrebattleRoomView import BasePrebattleRoomView

class CompanyRoomMeta(BasePrebattleRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BasePrebattleRoomView
    null
    """

    def requestToAssign(self, pID):
        """
        :param pID:
        :return :
        """
        self._printOverrideError('requestToAssign')

    def requestToUnassign(self, pID):
        """
        :param pID:
        :return :
        """
        self._printOverrideError('requestToUnassign')

    def requestToChangeOpened(self, isOpened):
        """
        :param isOpened:
        :return :
        """
        self._printOverrideError('requestToChangeOpened')

    def requestToChangeComment(self, comment):
        """
        :param comment:
        :return :
        """
        self._printOverrideError('requestToChangeComment')

    def requestToChangeDivision(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        self._printOverrideError('requestToChangeDivision')

    def getCompanyName(self):
        """
        :return String:
        """
        self._printOverrideError('getCompanyName')

    def canMoveToAssigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToAssigned')

    def canMoveToUnassigned(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMoveToUnassigned')

    def canMakeOpenedClosed(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canMakeOpenedClosed')

    def canChangeComment(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canChangeComment')

    def canChangeDivision(self):
        """
        :return Boolean:
        """
        self._printOverrideError('canChangeDivision')

    def as_setDivisionsListS(self, data, selected):
        """
        :param data:
        :param selected:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDivisionsList(data, selected)

    def as_setOpenedS(self, isOpened):
        """
        :param isOpened:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setOpened(isOpened)

    def as_setCommentS(self, comment):
        """
        :param comment:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setComment(comment)

    def as_setDivisionS(self, divisionID):
        """
        :param divisionID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDivision(divisionID)

    def as_setTotalLimitLabelsS(self, totalLevel):
        """
        :param totalLevel:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLimitLabels(totalLevel)

    def as_setMaxCountLimitLabelS(self, label):
        """
        :param label:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxCountLimitLabel(label)

    def as_setInvalidVehiclesS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInvalidVehicles(data)

    def as_setChangeSettingCoolDownS(self, coolDown):
        """
        :param coolDown:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeSettingCoolDown(coolDown)

    def as_setHeaderDataS(self, viewType, value):
        """
        :param viewType:
        :param value:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(viewType, value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\companyroommeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:32 St�edn� Evropa (letn� �as)
