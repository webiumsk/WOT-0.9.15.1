# 2016.08.04 19:51:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationInvitesAndRequestsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationInvitesAndRequestsMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def setDescription(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setDescription')

    def setShowOnlyInvites(self, value):
        """
        :param value:
        :return :
        """
        self._printOverrideError('setShowOnlyInvites')

    def resolvePlayerRequest(self, playerId, playerAccepted):
        """
        :param playerId:
        :param playerAccepted:
        :return :
        """
        self._printOverrideError('resolvePlayerRequest')

    def as_getDataProviderS(self):
        """
        :return Object:
        """
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setStaticDataS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setTeamDescriptionS(self, description):
        """
        :param description:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamDescription(description)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\meta\staticformationinvitesandrequestsmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:48 St�edn� Evropa (letn� �as)
