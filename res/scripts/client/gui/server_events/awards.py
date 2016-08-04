# 2016.08.04 19:52:35 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/server_events/awards.py
import random
from collections import namedtuple
import BigWorld
import constants
import potapov_quests
from gui.shared.utils.functions import makeTooltip
from helpers import i18n
from shared_utils import findFirst
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui.server_events import g_eventsCache
from gui.Scaleform.daapi.view.lobby.AwardWindow import AwardAbstract, ExplosionBackAward, packRibbonInfo
from gui.Scaleform.genConsts.BOOSTER_CONSTANTS import BOOSTER_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.MENU import MENU
from gui.shared.formatters import text_styles
_BG_IMG_BY_VEH_TYPE = {'lightTank': RES_ICONS.MAPS_ICONS_QUESTS_LTAWARDBACK,
 'mediumTank': RES_ICONS.MAPS_ICONS_QUESTS_MTAWARDBACK,
 'heavyTank': RES_ICONS.MAPS_ICONS_QUESTS_HTAWARDBACK,
 'AT-SPG': RES_ICONS.MAPS_ICONS_QUESTS_AT_SPGAWARDBACK,
 'SPG': RES_ICONS.MAPS_ICONS_QUESTS_SPGAWARDBACK}
_BG_IMG_FALLOUT = {'classic': RES_ICONS.MAPS_ICONS_QUESTS_CLASSICFALLOUTAWARDBACK,
 'multiteam': RES_ICONS.MAPS_ICONS_QUESTS_MULTITEAMFALLOUTAWARDBACK}

def _getNextQuestInTileByID(questID):
    quests = g_eventsCache.potapov.getQuests()
    questsInTile = sorted(potapov_quests.g_cache.questListByTileIDChainID(quests[questID].getTileID(), quests[questID].getChainID()))
    try:
        questInd = questsInTile.index(questID)
        for nextID in questsInTile[questInd + 1:]:
            if quests[nextID].isAvailableToPerform():
                return nextID

        for nextID in questsInTile[:questInd + 1]:
            if quests[nextID].isAvailableToPerform():
                return nextID

    except ValueError:
        LOG_ERROR('Cannot find quest ID {questID} in quests from tile {quests}'.format(questID=questID, quests=questsInTile))
        LOG_CURRENT_EXCEPTION()

    return None


class AchievementsAward(AwardAbstract):

    def __init__(self, achieves):
        raise hasattr(achieves, '__iter__') or AssertionError
        self.__achieves = achieves

    def getWindowTitle(self):
        return i18n.makeString(MENU.AWARDWINDOW_TITLE_NEWMEDALS)

    def getBackgroundImage(self):
        return RES_ICONS.MAPS_ICONS_REFERRAL_AWARDBACK

    def getAwardImage(self):
        return RES_ICONS.MAPS_ICONS_REFERRAL_AWARD_CREDITS_GLOW

    def getHeader(self):
        return text_styles.highTitle(i18n.makeString(MENU.AWARDWINDOW_QUESTS_MEDALS_HEADER))

    def getDescription(self):
        descr = []
        for achieve in self.__achieves:
            noteInfo = achieve.getNotificationInfo()
            if len(noteInfo):
                descr.append(noteInfo)

        return text_styles.main('\n\n'.join(descr))

    def getExtraFields(self):
        result = []
        for a in self.__achieves:
            result.append({'type': a.getRecordName()[1],
             'block': a.getBlock(),
             'icon': {'big': a.getBigIcon(),
                      'small': a.getSmallIcon()}})

        return {'achievements': result}


class TokenAward(ExplosionBackAward):

    def __init__(self, potapovQuest, tokenID, count, proxyEvent):
        super(TokenAward, self).__init__()
        self.__potapovQuest = potapovQuest
        self.__tokenID = tokenID
        self.__tokenCount = count
        self.__proxyEvent = proxyEvent

    def getWindowTitle(self):
        return i18n.makeString(MENU.AWARDWINDOW_TITLE_TOKENS)

    def getAwardImage(self):
        return RES_ICONS.MAPS_ICONS_QUESTS_TOKEN256

    def getHeader(self):
        return text_styles.highTitle(i18n.makeString(MENU.AWARDWINDOW_QUESTS_TOKENS_HEADER, count=self.__tokenCount))

    def getDescription(self):
        return text_styles.main(i18n.makeString(MENU.AWARDWINDOW_QUESTS_TOKENS_DESCRIPTION))

    def handleBodyButton(self):
        nextQuestID = _getNextQuestInTileByID(int(self.__potapovQuest.getID()))
        if nextQuestID is not None:
            self.__proxyEvent(nextQuestID, constants.EVENT_TYPE.POTAPOV_QUEST)
        return

    def getBodyButtonText(self):
        return i18n.makeString(MENU.AWARDWINDOW_TAKENEXTBUTTON)

    def getButtonStates(self):
        if not self.__potapovQuest.isFinal():
            return super(TokenAward, self).getButtonStates()
        else:
            nextQuestID = _getNextQuestInTileByID(int(self.__potapovQuest.getID()))
            return (False, True, nextQuestID is not None)
            return None


class VehicleAward(ExplosionBackAward):

    def __init__(self, vehicle):
        super(VehicleAward, self).__init__()
        self.__vehicle = vehicle

    def getWindowTitle(self):
        return i18n.makeString(MENU.AWARDWINDOW_TITLE_NEWVEHICLE)

    def getAwardImage(self):
        return self.__vehicle.iconUniqueLight

    def getHeader(self):
        return text_styles.highTitle(i18n.makeString(MENU.AWARDWINDOW_QUESTS_VEHICLE_HEADER, vehicleName=self.__vehicle.userName))

    def getDescription(self):
        return text_styles.main(i18n.makeString(MENU.AWARDWINDOW_QUESTS_VEHICLE_DESCRIPTION))


class TankwomanAward(ExplosionBackAward):

    def __init__(self, questID, tankmanData, proxyEvent):
        super(TankwomanAward, self).__init__()
        self.__questID = questID
        self.__tankmanData = tankmanData
        self.__proxyEvent = proxyEvent

    def getWindowTitle(self):
        return i18n.makeString(MENU.AWARDWINDOW_TITLE_NEWTANKMAN)

    def getAwardImage(self):
        return RES_ICONS.MAPS_ICONS_QUESTS_TANKMANFEMALEORANGE

    def getHeader(self):
        return text_styles.highTitle(i18n.makeString(MENU.AWARDWINDOW_QUESTS_TANKMANFEMALE_HEADER))

    def getDescription(self):
        return text_styles.main(i18n.makeString(MENU.AWARDWINDOW_QUESTS_TANKMANFEMALE_DESCRIPTION))

    def getOkButtonText(self):
        return i18n.makeString(MENU.AWARDWINDOW_RECRUITBUTTON)

    def handleOkButton(self):
        self.__proxyEvent(self.__questID, self.__tankmanData.isPremium, self.__tankmanData.fnGroupID, self.__tankmanData.lnGroupID, self.__tankmanData.iGroupID)


class FormattedAward(AwardAbstract):

    class _BonusFormatter(object):
        _BonusFmt = namedtuple('_BonusFmt', 'icon value tooltip bonusVO')

        def __call__(self, bonus):
            return []

    class _SimpleFormatter(_BonusFormatter):

        def __init__(self, icon, tooltip = ''):
            self._icon = icon
            self._tooltip = tooltip

        def __call__(self, bonus):
            return [self._BonusFmt(self._icon, BigWorld.wg_getIntegralFormat(bonus.getValue()), self._tooltip, None)]

    class _SimpleNoValueFormatter(_SimpleFormatter):

        def __call__(self, bonus):
            return [self._BonusFmt(self._icon, '', self._tooltip, None)]

    class _ItemsFormatter(_BonusFormatter):

        def __call__(self, bonus):
            result = []
            for item, count in bonus.getItems().iteritems():
                if item is not None and count:
                    tooltip = makeTooltip(header=item.userName, body=item.fullDescription)
                    result.append(self._BonusFmt(item.icon, BigWorld.wg_getIntegralFormat(count), tooltip, None))

            return result

    class _BoostersFormatter(_BonusFormatter):

        def __call__(self, bonus):
            result = []
            for booster, count in bonus.getBoosters().iteritems():
                if booster is not None and count:
                    tooltip = TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO
                    result.append(self._BonusFmt('', BigWorld.wg_getIntegralFormat(count), tooltip, self.__makeBoosterVO(booster)))

            return result

        @staticmethod
        def __makeBoosterVO(booster):
            return {'icon': booster.icon,
             'showCount': False,
             'qualityIconSrc': booster.getQualityIcon(),
             'slotLinkage': BOOSTER_CONSTANTS.SLOT_UI,
             'showLeftTime': False,
             'boosterId': booster.boosterID}

    def __init__(self):
        self._formatters = {'gold': self._SimpleFormatter(RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICONBIG, tooltip=TOOLTIPS.AWARDITEM_GOLD),
         'credits': self._SimpleFormatter(RES_ICONS.MAPS_ICONS_LIBRARY_CREDITSICONBIG_1, tooltip=TOOLTIPS.AWARDITEM_CREDITS),
         'freeXP': self._SimpleFormatter(RES_ICONS.MAPS_ICONS_LIBRARY_FREEXPICONBIG, tooltip=TOOLTIPS.AWARDITEM_FREEXP),
         'premium': self._SimpleNoValueFormatter(RES_ICONS.MAPS_ICONS_LIBRARY_PREMDAYICONBIG, tooltip=TOOLTIPS.AWARDITEM_PREMDAYS),
         'items': self._ItemsFormatter(),
         'goodies': self._BoostersFormatter()}

    def clear(self):
        self._formatters.clear()

    def getRibbonInfo(self):
        awards, strAwards = self._getMainAwards(self._getBonuses())
        if strAwards or awards:
            return packRibbonInfo(awardForCompleteText=i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_AWARDFORCOMLETE), awardBonusStrText=strAwards, awards=awards)
        else:
            return None

    def _getBonuses(self):
        return []

    def _getMainAwards(self, bonuses):
        awards = []
        strAwardsList = []
        strAwards = ''
        for b in bonuses:
            formatter = self._formatters.get(b.getName(), None)
            if callable(formatter):
                for bonus in formatter(b):
                    awards.append({'value': bonus.value,
                     'itemSource': bonus.icon,
                     'tooltip': bonus.tooltip,
                     'boosterVO': bonus.bonusVO})

            else:
                formattedBonus = b.format()
                if formattedBonus:
                    strAwardsList.append(text_styles.warning(formattedBonus))

        if len(strAwardsList):
            strAwards = ', '.join(strAwardsList)
        return (awards, strAwards)


class RegularAward(FormattedAward):

    def __init__(self, potapovQuest, proxyEvent, isMainReward = False, isAddReward = False):
        super(RegularAward, self).__init__()
        raise True in (isMainReward, isAddReward) or AssertionError
        self.__potapovQuest = potapovQuest
        self.__isMainReward = isMainReward
        self.__isAddReward = isAddReward
        self.__proxyEvent = proxyEvent

    def getWindowTitle(self):
        return i18n.makeString(MENU.AWARDWINDOW_TITLE_TASKCOMPLETE)

    def getBackgroundImage(self):
        if self.__potapovQuest.getQuestBranch() == potapov_quests.PQ_BRANCH.FALLOUT:
            return _BG_IMG_FALLOUT[self.__potapovQuest.getMajorTag()]
        else:
            vehType = findFirst(None, self.__potapovQuest.getVehicleClasses())
            if vehType in _BG_IMG_BY_VEH_TYPE:
                return _BG_IMG_BY_VEH_TYPE[vehType]
            return random.choice(_BG_IMG_BY_VEH_TYPE.values())

    def getAwardImage(self):
        return ''

    def getHeader(self):
        return i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_HEADER, taskName=self.__potapovQuest.getUserName())

    def getDescription(self):
        return i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_DESCRIPTION)

    def getAdditionalText(self):
        nextQuestID = _getNextQuestInTileByID(self.__potapovQuest.getID())
        if nextQuestID:
            nextQuestInfo = i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_NEXTTASKAUTOCHOICE, taskName=g_eventsCache.potapov.getQuests()[nextQuestID].getUserName())
        else:
            nextQuestInfo = ''
        if self.__isAddReward:
            result = []
            for b in self.__potapovQuest.getBonuses(isMain=False):
                if b.isShowInGUI():
                    result.append(b.format())

            taskComplete = i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_ADDITIONAL, award=', '.join(result))
            return text_styles.main('{0}\n{1}'.format(taskComplete, nextQuestInfo))
        else:
            return '{0}\n{1}'.format(i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_ADDITIONALNOTCOMPLETE), nextQuestInfo)

    def getButtonStates(self):
        nextQuestID = _getNextQuestInTileByID(int(self.__potapovQuest.getID()))
        return (False, True, nextQuestID is not None)

    def getBodyButtonText(self):
        return i18n.makeString(MENU.AWARDWINDOW_TAKENEXTBUTTON)

    def getRibbonInfo(self):
        if self.__isMainReward:
            awards, awardBonusStrText = self._getMainAwards(self._getBonuses())
            return packRibbonInfo(awardForCompleteText=i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_AWARDFORCOMLETE), awards=awards, awardBonusStrText=awardBonusStrText)
        else:
            return packRibbonInfo(awardReceivedText=i18n.makeString(MENU.AWARDWINDOW_QUESTS_TASKCOMPLETE_AWARDRECIEVED))

    def handleBodyButton(self):
        nextQuestID = _getNextQuestInTileByID(int(self.__potapovQuest.getID()))
        if nextQuestID is not None:
            self.__proxyEvent(nextQuestID, constants.EVENT_TYPE.POTAPOV_QUEST)
        return

    def _getBonuses(self):
        return self.__potapovQuest.getBonuses(isMain=True)


class MotiveQuestAward(FormattedAward):

    def __init__(self, motiveQuest, proxyEvent):
        super(MotiveQuestAward, self).__init__()
        self.__quest = motiveQuest
        self.__proxyEvent = proxyEvent

    def clear(self):
        super(MotiveQuestAward, self).clear()
        self.__quest = None
        return

    def getButtonStates(self):
        return (False, True, self.__getNextMotiveQuest() is not None)

    def getWindowTitle(self):
        return i18n.makeString('#tutorial:tutorialQuest/awardWindow/title')

    def getBackgroundImage(self):
        return RES_ICONS.MAPS_ICONS_HANGARTUTORIAL_GOALSQUEST

    def getHeader(self):
        return i18n.makeString('#tutorial:tutorialQuest/awardWindow/header', qName=i18n.makeString(self.__quest.getUserName()))

    def getDescription(self):
        return self.__quest.getAwardMsg()

    def getBodyButtonText(self):
        return i18n.makeString('#tutorial:tutorialQuest/awardWindow/nextQuest')

    def _getBonuses(self):
        return self.__quest.getBonuses()

    def __getNextMotiveQuest(self):
        quests = g_eventsCache.getMotiveQuests(lambda q: q.isAvailable() and not q.isCompleted())
        sortedQuests = sorted(quests.values(), key=lambda q: q.getPriority())
        nextQuest = findFirst(None, sortedQuests)
        for quest in sortedQuests:
            if quest.getPriority() > self.__quest.getPriority():
                return quest

        return nextQuest

    def handleBodyButton(self):
        nextQuest = self.__getNextMotiveQuest()
        if nextQuest is not None:
            self.__proxyEvent(nextQuest.getID(), constants.EVENT_TYPE.MOTIVE_QUEST)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\server_events\awards.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:52:36 St�edn� Evropa (letn� �as)
