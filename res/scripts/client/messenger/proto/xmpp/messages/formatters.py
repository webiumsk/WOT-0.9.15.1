# 2016.08.04 19:54:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/proto/xmpp/messages/formatters.py
from messenger.formatters.chat_message import LobbyMessageBuilder
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_USER_TEMPLATE_GROUPS

class XmppLobbyMessageBuilder(LobbyMessageBuilder):

    def __init__(self):
        super(XmppLobbyMessageBuilder, self).__init__()
        self.__affiliation = 'none'
        self.__role = 'none'

    def setAffiliation(self, affiliation):
        if affiliation in XMPP_MUC_USER_TEMPLATE_GROUPS.keys():
            self.__templateKey = XMPP_MUC_USER_TEMPLATE_GROUPS[affiliation]
        return self

    def setRole(self, role):
        if role in XMPP_MUC_USER_TEMPLATE_GROUPS.keys():
            self.__templateKey = XMPP_MUC_USER_TEMPLATE_GROUPS[role]
        return self
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\proto\xmpp\messages\formatters.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:54:28 St�edn� Evropa (letn� �as)
