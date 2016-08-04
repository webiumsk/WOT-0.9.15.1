# 2016.08.04 19:48:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/customization/quests.py
from collections import namedtuple
from gui.customization.shared import CUSTOMIZATION_TYPE
_QuestData = namedtuple('QuestData', ('id', 'name', 'count'))

class Quests(object):

    def __init__(self, events, dependencies):
        self.__events = events
        self._questsCache = dependencies.g_questsCache
        self._currentVehicle = dependencies.g_currentVehicle

    def init(self):
        self._questsCache.onSyncCompleted += self._update

    def start(self):
        self._update()

    def fini(self):
        self._questsCache.onSyncCompleted -= self._update

    def _getQuestsCache(self):
        return self._questsCache

    def _update(self):
        cNationID = self._currentVehicle.item.descriptor.type.customizationNationID
        incompleteQuestItems = ({}, {}, {})
        for name, quest in self._questsCache.getEvents().items():
            for bonus in quest.getBonuses('customizations'):
                for item in bonus.getList():
                    if item['nationId'] == cNationID or item['type'] == CUSTOMIZATION_TYPE.EMBLEM:
                        incompleteQuestItems[item['type']][item['id']] = _QuestData(id=quest.getID(), name=quest.getUserName(), count=item['value'])

        self.__events.onQuestsUpdated(incompleteQuestItems)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\customization\quests.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:48:55 St�edn� Evropa (letn� �as)
