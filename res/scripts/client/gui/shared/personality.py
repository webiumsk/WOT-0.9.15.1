# 2016.08.04 19:52:47 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/personality.py
import SoundGroups
import BigWorld
from adisp import process
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_DEBUG
from constants import HAS_DEV_RESOURCES
from PlayerEvents import g_playerEvents
from account_helpers import isPremiumAccount
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from ConnectionManager import connectionManager
from gui.app_loader import g_appLoader
from gui.shared.items_parameters.params_cache import g_paramsCache
from helpers import isPlayerAccount, time_utils
from gui import SystemMessages, g_guiResetters, game_control, miniclient, macroses
from gui.wgnc import g_wgncProvider
from gui.server_events import g_eventsCache
from gui.LobbyContext import g_lobbyContext
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.sounds import g_soundsCtrl
from gui.battle_results.VehicleProgressCache import g_vehicleProgressCache
from gui.goodies import g_goodiesCache
from gui.clubs.ClubsController import g_clubsCtrl
from gui.clans.clan_controller import g_clanCtrl
from gui.prb_control.dispatcher import g_prbLoader
from account_helpers.settings_core.SettingsCache import g_settingsCache
from account_helpers.settings_core.SettingsCore import g_settingsCore
from account_helpers.AccountValidator import AccountValidator
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.Scaleform.daapi.view.login.EULADispatcher import EULADispatcher
from gui.Scaleform.Waiting import Waiting
from gui.shared import g_eventBus, g_itemsCache, events, EVENT_BUS_SCOPE
from gui.shared.ClanCache import g_clanCache
from gui.shared.ItemsCache import CACHE_SYNC_REASON
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper
from gui.shared.utils.HangarSpace import g_hangarSpace
from gui.shared.utils.RareAchievementsCache import g_rareAchievesCache
from gui.login import g_loginManager
from helpers.statistics import g_statistics, HANGAR_LOADING_STATE
try:
    from gui import mods
    guiModsInit = mods.init
    guiModsFini = mods.fini
    guiModsSendEvent = mods.sendEvent
except ImportError:
    LOG_DEBUG('There is not mods package in the scripts')
    guiModsInit = guiModsFini = guiModsSendEvent = lambda *args: None

@process
def onAccountShowGUI(ctx):
    global onCenterIsLongDisconnected
    g_statistics.noteHangarLoadingState(HANGAR_LOADING_STATE.SHOW_GUI)
    g_lobbyContext.onAccountShowGUI(ctx)
    yield g_itemsCache.update(CACHE_SYNC_REASON.SHOW_GUI)
    g_statistics.noteHangarLoadingState(HANGAR_LOADING_STATE.QUESTS_SYNC)
    g_eventsCache.start()
    yield g_eventsCache.update()
    g_statistics.noteHangarLoadingState(HANGAR_LOADING_STATE.USER_SERVER_SETTINGS_SYNC)
    yield g_settingsCache.update()
    if not g_itemsCache.isSynced():
        g_appLoader.goToLoginByError('#menu:disconnect/codes/0')
        return
    eula = EULADispatcher()
    yield eula.processLicense()
    eula.fini()
    g_playerEvents.onGuiCacheSyncCompleted(ctx)
    code = yield AccountValidator().validate()
    if code > 0:
        g_appLoader.goToLoginByError('#menu:disconnect/codes/%d' % code)
        return
    g_settingsCore.serverSettings.applySettings()
    game_control.g_instance.onAccountShowGUI(g_lobbyContext.getGuiCtx())
    accDossier = g_itemsCache.items.getAccountDossier()
    g_rareAchievesCache.request(accDossier.getBlock('rareAchievements'))
    premium = isPremiumAccount(g_itemsCache.items.stats.attributes)
    if g_hangarSpace.inited:
        g_hangarSpace.refreshSpace(premium)
    else:
        g_hangarSpace.init(premium)
    g_currentVehicle.init()
    g_currentPreviewVehicle.init()
    g_appLoader.showLobby()
    g_prbLoader.onAccountShowGUI(g_lobbyContext.getGuiCtx())
    g_clanCache.onAccountShowGUI()
    g_clubsCtrl.start()
    g_clanCtrl.start()
    g_soundsCtrl.start()
    SoundGroups.g_instance.enableLobbySounds(True)
    onCenterIsLongDisconnected(True)
    guiModsSendEvent('onAccountShowGUI', ctx)
    Waiting.hide('enter')


def onAccountBecomeNonPlayer():
    g_itemsCache.clear()
    g_goodiesCache.clear()
    g_currentVehicle.destroy()
    g_currentPreviewVehicle.destroy()
    g_hangarSpace.destroy()
    guiModsSendEvent('onAccountBecomeNonPlayer')
    UsersInfoHelper.clear()


@process
def onAvatarBecomePlayer():
    yield g_settingsCache.update()
    g_settingsCore.serverSettings.applySettings()
    g_soundsCtrl.stop()
    g_clubsCtrl.stop()
    g_clanCtrl.stop()
    g_eventsCache.stop()
    g_prbLoader.onAvatarBecomePlayer()
    game_control.g_instance.onAvatarBecomePlayer()
    g_clanCache.onAvatarBecomePlayer()
    guiModsSendEvent('onAvatarBecomePlayer')
    Waiting.cancelCallback()


def onAccountBecomePlayer():
    g_lobbyContext.onAccountBecomePlayer()
    game_control.g_instance.onAccountBecomePlayer()
    guiModsSendEvent('onAccountBecomePlayer')


@process
def onClientUpdate(diff):
    yield lambda callback: callback(None)
    if isPlayerAccount():
        yield g_itemsCache.update(CACHE_SYNC_REASON.CLIENT_UPDATE, diff)
        yield g_eventsCache.update(diff)
        yield g_clanCache.update(diff)
    g_lobbyContext.update(diff)
    g_clientUpdateManager.update(diff)


def onShopResyncStarted():
    Waiting.show('sinhronize')


@process
def onShopResync():
    yield g_itemsCache.update(CACHE_SYNC_REASON.SHOP_RESYNC)
    if not g_itemsCache.isSynced():
        Waiting.hide('sinhronize')
        return
    yield g_eventsCache.update()
    Waiting.hide('sinhronize')
    now = time_utils.getCurrentTimestamp()
    SystemMessages.g_instance.pushI18nMessage(SYSTEM_MESSAGES.SHOP_RESYNC, date=BigWorld.wg_getLongDateFormat(now), time=BigWorld.wg_getShortTimeFormat(now), type=SystemMessages.SM_TYPE.Information)


def onCenterIsLongDisconnected(isLongDisconnected):
    isAvailable = not BigWorld.player().isLongDisconnectedFromCenter
    if isAvailable and not isLongDisconnected:
        SystemMessages.g_instance.pushI18nMessage(MENU.CENTERISAVAILABLE, type=SystemMessages.SM_TYPE.Information)
    elif not isAvailable:
        SystemMessages.g_instance.pushI18nMessage(MENU.CENTERISUNAVAILABLE, type=SystemMessages.SM_TYPE.Warning)


def onIGRTypeChanged(roomType, xpFactor):
    g_lobbyContext.updateGuiCtx({'igrData': {'roomType': roomType,
                 'igrXPFactor': xpFactor}})


def init(loadingScreenGUI = None):
    global onShopResyncStarted
    global onAccountShowGUI
    global onScreenShotMade
    global onIGRTypeChanged
    global onAccountBecomeNonPlayer
    global onAvatarBecomePlayer
    global onAccountBecomePlayer
    global onKickedFromServer
    global onShopResync
    g_loginManager.init()
    miniclient.configure_state()
    connectionManager.onKickedFromServer += onKickedFromServer
    g_playerEvents.onAccountShowGUI += onAccountShowGUI
    g_playerEvents.onAccountBecomeNonPlayer += onAccountBecomeNonPlayer
    g_playerEvents.onAccountBecomePlayer += onAccountBecomePlayer
    g_playerEvents.onAvatarBecomePlayer += onAvatarBecomePlayer
    g_playerEvents.onClientUpdated += onClientUpdate
    g_playerEvents.onShopResyncStarted += onShopResyncStarted
    g_playerEvents.onShopResync += onShopResync
    g_playerEvents.onCenterIsLongDisconnected += onCenterIsLongDisconnected
    g_playerEvents.onIGRTypeChanged += onIGRTypeChanged
    from gui.Scaleform.app_factory import createAppFactory
    g_appLoader.init(createAppFactory())
    game_control.g_instance.init()
    from gui.Scaleform import SystemMessagesInterface
    SystemMessages.g_instance = SystemMessagesInterface.SystemMessagesInterface()
    SystemMessages.g_instance.init()
    g_paramsCache.init()
    if loadingScreenGUI and loadingScreenGUI.script:
        loadingScreenGUI.script.active(False)
    g_prbLoader.init()
    g_soundsCtrl.init()
    g_itemsCache.init()
    g_settingsCache.init()
    g_settingsCore.init()
    g_eventsCache.init()
    g_clanCache.init()
    g_clubsCtrl.init()
    g_clanCtrl.init()
    g_vehicleProgressCache.init()
    g_goodiesCache.init()
    BigWorld.wg_setScreenshotNotifyCallback(onScreenShotMade)
    if HAS_DEV_RESOURCES:
        try:
            from gui.development import init
        except ImportError:
            LOG_ERROR('Development features not found.')
            init = lambda : None

        init()
    guiModsInit()


def start():
    g_appLoader.startLobby()


def fini():
    guiModsFini()
    g_soundsCtrl.fini()
    Waiting.close()
    g_appLoader.fini()
    SystemMessages.g_instance.destroy()
    g_eventBus.clear()
    g_prbLoader.fini()
    g_clubsCtrl.fini()
    g_clanCtrl.fini()
    g_clanCache.fini()
    game_control.g_instance.fini()
    macroses.fini()
    g_settingsCore.fini()
    g_settingsCache.fini()
    g_eventsCache.fini()
    g_itemsCache.fini()
    g_goodiesCache.fini()
    g_vehicleProgressCache.fini()
    UsersInfoHelper.fini()
    connectionManager.onKickedFromServer -= onKickedFromServer
    g_playerEvents.onIGRTypeChanged -= onIGRTypeChanged
    g_playerEvents.onAccountShowGUI -= onAccountShowGUI
    g_playerEvents.onAccountBecomeNonPlayer -= onAccountBecomeNonPlayer
    g_playerEvents.onAvatarBecomePlayer -= onAvatarBecomePlayer
    g_playerEvents.onAccountBecomePlayer -= onAccountBecomePlayer
    g_playerEvents.onClientUpdated -= onClientUpdate
    g_playerEvents.onShopResyncStarted -= onShopResyncStarted
    g_playerEvents.onShopResync -= onShopResync
    g_playerEvents.onCenterIsLongDisconnected -= onCenterIsLongDisconnected
    g_loginManager.fini()
    BigWorld.wg_setScreenshotNotifyCallback(None)
    if HAS_DEV_RESOURCES:
        try:
            from gui.development import fini
        except ImportError:
            LOG_ERROR('Development features not found.')
            fini = lambda : None

        fini()
    return


def onConnected():
    g_statistics.noteHangarLoadingState(HANGAR_LOADING_STATE.CONNECTED)
    guiModsSendEvent('onConnected')
    game_control.g_instance.onConnected()


def onDisconnected():
    g_statistics.noteHangarLoadingState(HANGAR_LOADING_STATE.DISCONNECTED)
    g_loginManager.writePeripheryLifetime()
    guiModsSendEvent('onDisconnected')
    g_prbLoader.onDisconnected()
    g_clanCache.onDisconnected()
    g_soundsCtrl.stop(isDisconnected=True)
    game_control.g_instance.onDisconnected()
    g_clubsCtrl.stop(isDisconnected=True)
    g_clanCtrl.stop()
    g_wgncProvider.clear()
    g_itemsCache.clear()
    g_goodiesCache.clear()
    g_eventsCache.clear()
    g_lobbyContext.clear()
    g_vehicleProgressCache.clear()
    UsersInfoHelper.clear()
    Waiting.rollback()
    Waiting.cancelCallback()
    g_appLoader.goToLoginByEvent()


def onKickedFromServer(reason, isBan, expiryTime):
    g_appLoader.goToLoginByKick(reason, isBan, expiryTime)


def onScreenShotMade(path):
    g_eventBus.handleEvent(events.GameEvent(events.GameEvent.SCREEN_SHOT_MADE, {'path': path}), scope=EVENT_BUS_SCOPE.GLOBAL)


def onRecreateDevice():
    for c in g_guiResetters:
        try:
            c()
        except Exception:
            LOG_CURRENT_EXCEPTION()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\personality.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:52:47 St�edn� Evropa (letn� �as)
