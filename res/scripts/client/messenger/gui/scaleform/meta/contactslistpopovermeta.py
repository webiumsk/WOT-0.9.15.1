# 2016.08.04 19:54:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsListPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class ContactsListPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    null
    """

    def addToFriends(self, uid, name):
        """
        :param uid:
        :param name:
        :return :
        """
        self._printOverrideError('addToFriends')

    def addToIgnored(self, uid, name):
        """
        :param uid:
        :param name:
        :return :
        """
        self._printOverrideError('addToIgnored')

    def isEnabledInRoaming(self, uid):
        """
        :param uid:
        :return Boolean:
        """
        self._printOverrideError('isEnabledInRoaming')

    def changeGroup(self, dbId, contactName, groupData):
        """
        :param dbId:
        :param contactName:
        :param groupData:
        :return :
        """
        self._printOverrideError('changeGroup')

    def copyIntoGroup(self, contactDbId, groupData):
        """
        :param contactDbId:
        :param groupData:
        :return :
        """
        self._printOverrideError('copyIntoGroup')

    def as_setInitInfoS(self, data):
        """
        :param data:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitInfo(data)

    def as_editGroupS(self, targetGroupName):
        """
        :param targetGroupName:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_editGroup(targetGroupName)

    def as_removeGroupS(self, targetGroupName):
        """
        :param targetGroupName:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeGroup(targetGroupName)

    def as_createContactNoteS(self, userName, databaseID):
        """
        :param userName:
        :param databaseID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_createContactNote(userName, databaseID)

    def as_editContactNoteS(self, userName, databaseID):
        """
        :param userName:
        :param databaseID:
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.as_editContactNote(userName, databaseID)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\scaleform\meta\contactslistpopovermeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:54:05 St�edn� Evropa (letn� �as)
