# 2016.08.04 19:49:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/legacy/BattleRibbonsPanel.py
from account_helpers.settings_core.settings_constants import GAME
from gui.battle_control import g_sessionProvider, avatar_getter
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID
from helpers import i18n
from debug_utils import LOG_ERROR
from account_helpers.settings_core.SettingsCore import g_settingsCore
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES
_FEEDBACK_EVENT_TO_BATTLE_EFFICIENCY = {FEEDBACK_EVENT_ID.PLAYER_KILLED_ENEMY: BATTLE_EFFICIENCY_TYPES.DESTRUCTION,
 FEEDBACK_EVENT_ID.PLAYER_DAMAGED_HP_ENEMY: BATTLE_EFFICIENCY_TYPES.DAMAGE,
 FEEDBACK_EVENT_ID.PLAYER_DAMAGED_DEVICE_ENEMY: BATTLE_EFFICIENCY_TYPES.CRITS,
 FEEDBACK_EVENT_ID.PLAYER_SPOTTED_ENEMY: BATTLE_EFFICIENCY_TYPES.DETECTION,
 FEEDBACK_EVENT_ID.PLAYER_ASSIST_TO_KILL_ENEMY: BATTLE_EFFICIENCY_TYPES.ASSIST,
 FEEDBACK_EVENT_ID.PLAYER_USED_ARMOR: BATTLE_EFFICIENCY_TYPES.ARMOR,
 FEEDBACK_EVENT_ID.PLAYER_CAPTURED_BASE: BATTLE_EFFICIENCY_TYPES.CAPTURE,
 FEEDBACK_EVENT_ID.PLAYER_DROPPED_CAPTURE: BATTLE_EFFICIENCY_TYPES.DEFENCE}
_AIM_MODE_TO_RADIUS = {'arcade': 120,
 'strategic': 260,
 'sniper': 200,
 'postmortem': 230}
_RIBBON_SOUNDS_ENABLED = True
_SHOW_RIBBON_SOUND_NAME = 'show_ribbon'
_HIDE_RIBBON_SOUND_NAME = 'hide_ribbon'
_INC_COUNTER_SOUND_NAME = 'increment_ribbon_counter'
_POS_COEFF = (1.0, 1.0)

class BattleRibbonsPanel(object):

    def __init__(self, parentUI):
        self.__ui = parentUI
        self.__enabled = False

    def start(self):
        self.__flashObject = self.__ui.getMember('_level0.ribbonsPanel')
        self.__enabled = bool(g_settingsCore.getSetting(GAME.SHOW_BATTLE_EFFICIENCY_RIBBONS))
        if self.__flashObject:
            self.__flashObject.resync()
            self.__flashObject.script = self
            self.__flashObject.setup(self.__enabled, _RIBBON_SOUNDS_ENABLED, *_POS_COEFF)
            self.__addListeners()
        else:
            LOG_ERROR('Display object is not found in the swf file.')

    def destroy(self):
        self.__removeListeners()
        self.__ui = None
        if self.__flashObject is not None:
            self.__flashObject.script = None
            self.__flashObject = None
        return

    def onShow(self, type, count):
        self.__playSound(_SHOW_RIBBON_SOUND_NAME)

    def onChange(self, type, count):
        self.__playSound(_SHOW_RIBBON_SOUND_NAME)

    def onIncCount(self, type, count):
        self.__playSound(_INC_COUNTER_SOUND_NAME)

    def onHide(self, type):
        self.__playSound(_HIDE_RIBBON_SOUND_NAME)

    def __playSound(self, eventName):
        if not _RIBBON_SOUNDS_ENABLED:
            return
        soundNotifications = avatar_getter.getSoundNotifications()
        if soundNotifications and hasattr(soundNotifications, 'play'):
            soundNotifications.play(eventName)

    def __addListeners(self):
        ctrl = g_sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onPlayerFeedbackReceived += self.__onPlayerFeedbackReceived
        ctrl = g_sessionProvider.shared.crosshair
        if ctrl is not None:
            ctrl.onCrosshairPositionChanged += self.__onCrosshairPositionChanged
            self.__onCrosshairPositionChanged(*ctrl.getPosition())
        g_settingsCore.onSettingsChanged += self.__onSettingsChanged
        return

    def __removeListeners(self):
        ctrl = g_sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onPlayerFeedbackReceived -= self.__onPlayerFeedbackReceived
        ctrl = g_sessionProvider.shared.crosshair
        if ctrl is not None:
            ctrl.onCrosshairPositionChanged -= self.__onCrosshairPositionChanged
        g_settingsCore.onSettingsChanged -= self.__onSettingsChanged
        return

    def __onCrosshairPositionChanged(self, x, y):
        if not self.__ui:
            return
        else:
            inputHandler = avatar_getter.getInputHandler()
            if inputHandler is None:
                return
            mode = inputHandler.ctrlModeName
            if mode not in _AIM_MODE_TO_RADIUS:
                LOG_ERROR('Value of radius is not defined', mode)
                return
            radius = _AIM_MODE_TO_RADIUS[mode]
            bounds = [x - radius,
             y - radius,
             x + radius,
             y + radius]
            self.__ui.call('battle.aimVisibleSizeChanged', bounds)
            return

    def __onPlayerFeedbackReceived(self, eventID, series):
        if self.__enabled and eventID in _FEEDBACK_EVENT_TO_BATTLE_EFFICIENCY:
            effType = _FEEDBACK_EVENT_TO_BATTLE_EFFICIENCY[eventID]
            effShortDesc = i18n.makeString('#ingame_gui:efficiencyRibbons/{0:>s}'.format(effType))
            self.__flashObject.addBattleEfficiencyEvent(effType, effShortDesc, series)

    def __onSettingsChanged(self, diff):
        key = GAME.SHOW_BATTLE_EFFICIENCY_RIBBONS
        if key in diff and self.__flashObject:
            self.__enabled = bool(diff[key])
            self.__flashObject.setup(self.__enabled, _RIBBON_SOUNDS_ENABLED, *_POS_COEFF)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\legacy\battleribbonspanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:45 St�edn� Evropa (letn� �as)
