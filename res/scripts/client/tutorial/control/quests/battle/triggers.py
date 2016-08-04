# 2016.08.04 19:54:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/quests/battle/triggers.py
from gui.battle_control import g_sessionProvider
from tutorial.control.triggers import TriggerWithValidateVar

class UseItemsTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            eqCtrl = g_sessionProvider.shared.equipments
            if eqCtrl is not None:
                eqCtrl.onEquipmentUpdated += self.__onEquipmentUpdated
        self.toggle(isOn=self.isOn())
        return

    def isOn(self, result = False):
        return result

    def __onEquipmentUpdated(self, intCD, item):
        conditionVar = self.getVar()
        itemsList = conditionVar.get('items', [])
        if intCD in itemsList and item.getQuantity() == 0:
            self.toggle(isOn=self.isOn(True))

    def clear(self):
        eqCtrl = g_sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        self.isSubscribed = False
        self.isRunning = False
        return


class InstallItemsTrigger(TriggerWithValidateVar):

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            eqCtrl = g_sessionProvider.shared.equipments
            if eqCtrl is not None:
                eqCtrl.onEquipmentUpdated += self.__onEquipmentAdded
        self.toggle(isOn=self.isOn())
        return

    def isOn(self):
        eqCtrl = g_sessionProvider.shared.equipments
        if eqCtrl is not None:
            conditionVar = self.getVar()
            itemsList = conditionVar.get('items', [])
            for eqCD in itemsList:
                if eqCtrl.hasEquipment(eqCD):
                    return True

        return False

    def __onEquipmentAdded(self, *args):
        self.toggle(isOn=self.isOn())

    def clear(self):
        eqCtrl = g_sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated -= self.__onEquipmentAdded
        self.isSubscribed = False
        self.isRunning = False
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\quests\battle\triggers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:54:45 St�edn� Evropa (letn� �as)
