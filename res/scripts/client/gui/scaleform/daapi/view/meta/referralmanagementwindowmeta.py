# 2016.08.04 19:51:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralManagementWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def onInvitesManagementLinkClick(self):
        """
        :return :
        """
        self._printOverrideError('onInvitesManagementLinkClick')

    def inviteIntoSquad(self, referralID):
        """
        :param referralID:
        :return :
        """
        self._printOverrideError('inviteIntoSquad')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTableDataS(self, referrals):
        """
        :param referrals:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(referrals)

    def as_setAwardDataDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardDataData(data)

    def as_setProgressDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressData(data)

    def as_showAlertS(self, alertStr):
        """
        :param alertStr:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showAlert(alertStr)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\referralmanagementwindowmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:46 St�edn� Evropa (letn� �as)
