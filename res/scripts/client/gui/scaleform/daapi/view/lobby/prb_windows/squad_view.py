# 2016.08.04 19:51:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/prb_windows/squad_view.py
import account_helpers
from gui.Scaleform.daapi.view.lobby.prb_windows.SquadActionButtonStateVO import SquadActionButtonStateVO
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.game_control import getFalloutCtrl
from gui.shared.formatters import text_styles
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.Scaleform.locale.MENU import MENU
from gui.prb_control.context import unit_ctx
from gui.Scaleform.daapi.view.meta.SquadViewMeta import SquadViewMeta
from gui.Scaleform.daapi.view.lobby.rally import vo_converters
from gui.prb_control.settings import CTRL_ENTITY_TYPE, REQUEST_TYPE, FUNCTIONAL_FLAG
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.formatters.ranges import toRomanRangeString
from gui.server_events import g_eventsCache
from helpers import i18n, int2roman
from gui.prb_control import settings
from gui.shared.utils.functions import makeTooltip

class SquadView(SquadViewMeta):

    def inviteFriendRequest(self):
        if self.__canSendInvite():
            self.fireEvent(events.LoadViewEvent(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY, ctx={'prbName': 'squad',
             'ctrlType': CTRL_ENTITY_TYPE.UNIT}), scope=EVENT_BUS_SCOPE.LOBBY)

    def toggleReadyStateRequest(self):
        self.unitFunctional.togglePlayerReadyAction(True)

    def onUnitVehiclesChanged(self, dbID, vInfos):
        functional = self.unitFunctional
        pInfo = functional.getPlayerInfo(dbID=dbID)
        needToUpdateSlots = g_eventsCache.isSquadXpFactorsEnabled()
        if pInfo.isInSlot:
            slotIdx = pInfo.slotIdx
            if vInfos and not vInfos[0].isEmpty():
                vInfo = vInfos[0]
                vehicleVO = makeVehicleVO(g_itemsCache.items.getItemByCD(vInfo.vehTypeCD), functional.getRosterSettings().getLevelsRange(), isCurrentPlayer=pInfo.isCurrentPlayer())
                slotCost = vInfo.vehLevel
            else:
                slotState = functional.getSlotState(slotIdx)
                vehicleVO = None
                if slotState.isClosed:
                    slotCost = settings.UNIT_CLOSED_SLOT_COST
                else:
                    slotCost = 0
            self.as_setMemberVehicleS(slotIdx, slotCost, vehicleVO)
            if pInfo.isCurrentPlayer():
                if len(vInfos) < slotIdx + 1:
                    needToUpdateSlots = True
            elif vehicleVO is None:
                needToUpdateSlots = True
        if g_eventsCache.isSquadXpFactorsEnabled():
            self.as_setActionButtonStateS(self.__getActionButtonStateVO())
        if needToUpdateSlots:
            self._updateMembersData()
        return

    def chooseVehicleRequest(self):
        pass

    def leaveSquad(self):
        self.prbDispatcher.doLeaveAction(unit_ctx.LeaveUnitCtx(waitingID='prebattle/leave', flags=FUNCTIONAL_FLAG.UNDEFINED))

    def onUnitPlayerAdded(self, pInfo):
        super(SquadView, self).onUnitPlayerAdded(pInfo)
        self._setActionButtonState()

    def onUnitPlayerRemoved(self, pInfo):
        super(SquadView, self).onUnitPlayerRemoved(pInfo)
        self._setActionButtonState()

    def onUnitPlayerStateChanged(self, pInfo):
        self._updateRallyData()
        self._setActionButtonState()

    def onUnitFlagsChanged(self, flags, timeLeft):
        super(SquadView, self).onUnitFlagsChanged(flags, timeLeft)
        self._setActionButtonState()
        if flags.isInQueue():
            self._closeSendInvitesWindow()

    def onUnitRosterChanged(self):
        super(SquadView, self).onUnitRosterChanged()
        self._setActionButtonState()
        if not self.__canSendInvite():
            self._closeSendInvitesWindow()

    def onUnitMembersListChanged(self):
        super(SquadView, self).onUnitMembersListChanged()
        self._updateRallyData()
        self._setActionButtonState()

    def getCoolDownRequests(self):
        requests = super(SquadView, self).getCoolDownRequests()
        requests.append(REQUEST_TYPE.SET_PLAYER_STATE)
        return requests

    def _populate(self):
        super(SquadView, self)._populate()
        self.addListener(events.CoolDownEvent.PREBATTLE, self.__handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        self._updateHeader()

    def _dispose(self):
        self.removeListener(events.CoolDownEvent.PREBATTLE, self.__handleSetPrebattleCoolDown, scope=EVENT_BUS_SCOPE.LOBBY)
        super(SquadView, self)._dispose()

    def _setActionButtonState(self):
        functional = self.unitFunctional
        enabled = not (functional.getFlags().isInQueue() and functional.getPlayerInfo().isReady) and self.__canSendInvite()
        if enabled:
            enabled = False
            unitIdx = functional.getUnitIdx()
            for slot in functional.getSlotsIterator(*functional.getUnit(unitIdx=unitIdx)):
                if not slot.player:
                    enabled = True
                    break

        self.as_updateInviteBtnStateS(enabled)
        self.as_setActionButtonStateS(self.__getActionButtonStateVO())

    def _updateHeader(self):
        isSquadXpFactorsEnabled = g_eventsCache.isSquadXpFactorsEnabled()
        isArtVisible = isSquadXpFactorsEnabled
        if isArtVisible:
            tooltip, tooltipType = self._getInfoIconTooltipParams()
            hdrIconSource, iXPadding, iYPadding, hdrMessageText = self._getHeaderMessageParams()
        else:
            tooltip = ''
            tooltipType = ''
            hdrIconSource = ''
            hdrMessageText = ''
            iXPadding = 0
            iYPadding = 0
        data = {'infoIconTooltip': tooltip,
         'infoIconTooltipType': tooltipType,
         'isVisibleInfoIcon': isArtVisible,
         'isVisibleHeaderIcon': isArtVisible,
         'headerIconSource': hdrIconSource,
         'icoXPadding': iXPadding,
         'icoYPadding': iYPadding,
         'headerMessageText': hdrMessageText,
         'isVisibleHeaderMessage': isArtVisible}
        self.as_setSimpleTeamSectionDataS(data)

    def _getHeaderMessageParams(self):
        functional = self.unitFunctional
        isBalancedSquadEnabled = g_eventsCache.isBalancedSquadEnabled()
        if isBalancedSquadEnabled:
            if functional.isDynamic():
                headerIconSource = RES_ICONS.MAPS_ICONS_SQUAD_SQUAD_SILVER_STARS_ATTENTION
                headerMessageText = text_styles.middleTitle(i18n.makeString(MESSENGER.DIALOGS_SQUADCHANNEL_HEADERMSG_DYNSQUAD))
                iconXPadding = 0
                iconYPadding = 0
            else:
                headerIconSource = RES_ICONS.MAPS_ICONS_SQUAD_SQUAD_SILVER_STARS
                headerMessageText = text_styles.main(i18n.makeString(MESSENGER.DIALOGS_SQUADCHANNEL_HEADERMSG_SQUADFORMATION))
                iconXPadding = 9
                iconYPadding = 9
        else:
            headerIconSource = RES_ICONS.MAPS_ICONS_SQUAD_SQUAD_SILVER_STARS
            headerMessageText = text_styles.main(i18n.makeString(MESSENGER.DIALOGS_SQUADCHANNEL_HEADERMSG_SQUADFORMATIONRESTRICTION))
            iconXPadding = 9
            iconYPadding = 9
        return (headerIconSource,
         iconXPadding,
         iconYPadding,
         headerMessageText)

    def _getInfoIconTooltipParams(self):
        isBalancedSquadEnabled = g_eventsCache.isBalancedSquadEnabled()
        if isBalancedSquadEnabled:
            tooltipType = TOOLTIPS_CONSTANTS.COMPLEX
            tooltip = TOOLTIPS.SQUADWINDOW_INFOICON_TECH
        else:
            tooltipType = TOOLTIPS_CONSTANTS.SPECIAL
            tooltip = TOOLTIPS_CONSTANTS.SQUAD_RESTRICTIONS_INFO
        return (tooltip, tooltipType)

    def _updateMembersData(self):
        functional = self.unitFunctional
        self.as_setMembersS(*vo_converters.makeSlotsVOs(functional, functional.getUnitIdx(), app=self.app))
        self._setActionButtonState()

    def _updateRallyData(self):
        functional = self.unitFunctional
        data = vo_converters.makeUnitVO(functional, unitIdx=functional.getUnitIdx(), app=self.app)
        self.as_updateRallyS(data)
        self.as_updateBattleTypeS({'battleTypeName': '',
         'isNew': self._isNew(),
         'leaveBtnTooltip': self._getLeaveBtnTooltip()})

    def _getLeaveBtnTooltip(self):
        return TOOLTIPS.SQUADWINDOW_BUTTONS_LEAVESQUAD

    def _getBattleTypeName(self):
        return text_styles.main(MESSENGER.DIALOGS_SQUADCHANNEL_BATTLETYPE) + '\n' + i18n.makeString(MENU.HEADERBUTTONS_BATTLE_MENU_STANDART)

    def _isEvent(self):
        return False

    def _isNew(self):
        return False

    def __getActionButtonStateVO(self):
        unitFunctional = self.unitFunctional
        return SquadActionButtonStateVO(unitFunctional)

    def __canSendInvite(self):
        return self.unitFunctional.getPermissions().canSendInvite()

    def __handleSetPrebattleCoolDown(self, event):
        if event.requestID is REQUEST_TYPE.SET_PLAYER_STATE:
            self.as_setCoolDownForReadyButtonS(event.coolDown)


class EventSquadView(SquadView):

    def _getBattleTypeName(self):
        return text_styles.main(MESSENGER.DIALOGS_SQUADCHANNEL_BATTLETYPE) + '\n' + i18n.makeString(MENU.HEADERBUTTONS_BATTLE_MENU_EVENT)

    def _isEvent(self):
        return True

    def _getInfoIconTooltipParams(self):
        vehiclesNames = [ veh.userName for veh in g_eventsCache.getEventVehicles() ]
        tooltip = i18n.makeString(TOOLTIPS.SQUADWINDOW_EVENTVEHICLE, tankName=', '.join(vehiclesNames))
        return (makeTooltip(body=tooltip), TOOLTIPS_CONSTANTS.COMPLEX)

    def _getHeaderMessageParams(self):
        headerIconSource = RES_ICONS.MAPS_ICONS_SQUAD_EVENT
        headerMessageText = text_styles.main(i18n.makeString(MESSENGER.DIALOGS_SQUADCHANNEL_HEADERMSG_EVENTFORMATIONRESTRICTION))
        iconXPadding = 0
        iconYPadding = 0
        return (headerIconSource,
         iconXPadding,
         iconYPadding,
         headerMessageText)

    def _getLeaveBtnTooltip(self):
        return TOOLTIPS.SQUADWINDOW_BUTTONS_LEAVEEVENTSQUAD


class FalloutSquadView(SquadView):

    def __init__(self):
        super(FalloutSquadView, self).__init__()
        self.__falloutCtrl = None
        return

    def toggleReadyStateRequest(self):
        self.unitFunctional.togglePlayerReadyAction()

    def onUnitVehiclesChanged(self, dbID, vInfos):
        if dbID != account_helpers.getAccountDatabaseID():
            self._updateRallyData()

    def onUnitRejoin(self):
        super(FalloutSquadView, self).onUnitRejoin()
        self.__updateHeader()

    def _populate(self):
        self.__falloutCtrl = getFalloutCtrl()
        self.__falloutCtrl.onSettingsChanged += self.__onSettingsChanged
        self.__falloutCtrl.onVehiclesChanged += self.__onVehiclesChanged
        self.as_isFalloutS(True)
        super(FalloutSquadView, self)._populate()
        self.__updateHeader()

    def _dispose(self):
        self.__falloutCtrl.onSettingsChanged -= self.__onSettingsChanged
        self.__falloutCtrl.onVehiclesChanged -= self.__onVehiclesChanged
        self.__falloutCtrl = None
        super(FalloutSquadView, self)._dispose()
        return

    def _updateRallyData(self):
        functional = self.unitFunctional
        data = vo_converters.makeUnitVO(functional, unitIdx=functional.getUnitIdx(), app=self.app)
        self.as_updateRallyS(data)
        self.as_updateBattleTypeS({'battleTypeName': self._getBattleTypeName(),
         'isNew': self._isNew(),
         'leaveBtnTooltip': self._getLeaveBtnTooltip()})

    def _getBattleTypeName(self):
        return text_styles.main(MESSENGER.DIALOGS_SQUADCHANNEL_BATTLETYPE) + '\n' + i18n.makeString(MENU.HEADERBUTTONS_BATTLE_MENU_STANDART)

    def __dominationVehicleInfoTooltip(self, requiredLevel, allowedLevelsStr):
        return {'id': TOOLTIPS.SQUADWINDOW_DOMINATION_VEHICLESINFOICON,
         'header': {},
         'body': {'level': int2roman(requiredLevel),
                  'allowedLevels': allowedLevelsStr}}

    def __updateHeader(self):
        allowedLevelsList = list(self.__falloutCtrl.getConfig().allowedLevels)
        allowedLevelsStr = toRomanRangeString(allowedLevelsList, 1)
        vehicleLbl = i18n.makeString(CYBERSPORT.WINDOW_UNIT_TEAMVEHICLESLBL, levelsRange=text_styles.main(allowedLevelsStr))
        tooltipData = {}
        if len(allowedLevelsList) > 1:
            tooltipData = self.__dominationVehicleInfoTooltip(self.__falloutCtrl.getConfig().vehicleLevelRequired, allowedLevelsStr)
        self.as_setVehiclesTitleS(vehicleLbl, tooltipData)

    def __onSettingsChanged(self, *args):
        self._updateRallyData()
        self._setActionButtonState()
        self.__updateHeader()

    def __onVehiclesChanged(self, *args):
        self._updateRallyData()
        self._setActionButtonState()
        self.__updateHeader()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\prb_windows\squad_view.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:02 St�edn� Evropa (letn� �as)
