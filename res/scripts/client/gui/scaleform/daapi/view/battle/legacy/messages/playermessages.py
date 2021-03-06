# 2016.08.04 19:49:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/legacy/messages/PlayerMessages.py
from constants import EQUIPMENT_STAGES
from gui.battle_control import g_sessionProvider, avatar_getter
from gui.Scaleform.daapi.view.battle.legacy.messages.FadingMessages import FadingMessages
from debug_utils import LOG_DEBUG
from items import vehicles

class PlayerMessages(FadingMessages):

    def __init__(self, parentUI):
        super(PlayerMessages, self).__init__(parentUI, 'PlayerMessagesPanel', 'gui/legacy_player_messages.xml')

    def __del__(self):
        LOG_DEBUG('PlayerMessages panel is deleted')

    def _addGameListeners(self):
        super(PlayerMessages, self)._addGameListeners()
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowPlayerMessageByCode += self.__onShowPlayerMessageByCode
            ctrl.onShowPlayerMessageByKey += self.__onShowPlayerMessageByKey
        ctrl = g_sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated += self.__onCombatEquipmentUpdated
        arena = avatar_getter.getArena()
        if arena:
            arena.onCombatEquipmentUsed += self.__onCombatEquipmentUsed
        return

    def _removeGameListeners(self):
        ctrl = g_sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowPlayerMessageByCode -= self.__onShowPlayerMessageByCode
            ctrl.onShowPlayerMessageByKey -= self.__onShowPlayerMessageByKey
        ctrl = g_sessionProvider.shared.equipments
        if ctrl is not None:
            ctrl.onEquipmentUpdated -= self.__onCombatEquipmentUpdated
        arena = avatar_getter.getArena()
        if arena is not None:
            arena.onCombatEquipmentUsed -= self.__onCombatEquipmentUsed
        super(PlayerMessages, self)._removeGameListeners()
        return

    def __onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID):
        LOG_DEBUG('onShowPlayerMessage', code, postfix, targetID, attackerID, equipmentID)
        getFullName = g_sessionProvider.getCtx().getPlayerFullName
        if equipmentID:
            equipment = vehicles.g_cache.equipments().get(equipmentID)
            if equipment is not None:
                postfix = '_'.join((postfix, equipment.name.split('_')[0].upper()))
        self.showMessage(code, {'target': getFullName(targetID, showClan=False),
         'attacker': getFullName(attackerID, showClan=False)}, extra=(('target', targetID), ('attacker', attackerID)), postfix=postfix)
        return

    def __onShowPlayerMessageByKey(self, key, args = None, extra = None):
        self.showMessage(key, args, extra)

    def __onCombatEquipmentUpdated(self, intCD, item):
        if item.getPrevStage() in (EQUIPMENT_STAGES.DEPLOYING, EQUIPMENT_STAGES.UNAVAILABLE, EQUIPMENT_STAGES.COOLDOWN) and item.getStage() == EQUIPMENT_STAGES.READY:
            postfix = item.getDescriptor().name.split('_')[0].upper()
            self.showMessage('COMBAT_EQUIPMENT_READY', {}, postfix=postfix)

    def __onCombatEquipmentUsed(self, shooterID, eqID):
        battleCxt = g_sessionProvider.getCtx()
        if not battleCxt.isCurrentPlayer(shooterID):
            equipment = vehicles.g_cache.equipments().get(eqID)
            getFullName = battleCxt.getPlayerFullName
            if equipment is not None:
                postfix = equipment.name.split('_')[0].upper()
                self.showMessage('COMBAT_EQUIPMENT_USED', {'player': getFullName(shooterID, showClan=False)}, extra=(('player', shooterID),), postfix=postfix)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\battle\legacy\messages\playermessages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:51 St�edn� Evropa (letn� �as)
