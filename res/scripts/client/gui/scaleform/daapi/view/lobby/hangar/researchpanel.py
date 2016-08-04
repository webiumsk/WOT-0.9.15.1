# 2016.08.04 19:50:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ResearchPanel.py
from CurrentVehicle import g_currentVehicle
from debug_utils import LOG_ERROR
from gui.shared import g_itemsCache, event_dispatcher as shared_events
from gui.shared.gui_items.Vehicle import getLobbyDescription
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.ResearchPanelMeta import ResearchPanelMeta

class ResearchPanel(ResearchPanelMeta):

    def _populate(self):
        super(ResearchPanel, self)._populate()
        g_clientUpdateManager.addCallbacks({'stats.vehTypeXP': self.onVehicleTypeXPChanged,
         'stats.eliteVehicles': self.onVehicleBecomeElite})
        self.onCurrentVehicleChanged()

    def _dispose(self):
        super(ResearchPanel, self)._dispose()
        g_clientUpdateManager.removeObjectCallbacks(self)

    def goToResearch(self):
        if g_currentVehicle.isPresent():
            shared_events.showResearchView(g_currentVehicle.item.intCD)
        else:
            LOG_ERROR('Current vehicle is not preset')

    def onCurrentVehicleChanged(self):
        if g_currentVehicle.isPresent():
            xps = g_itemsCache.items.stats.vehiclesXPs
            xp = xps.get(g_currentVehicle.item.intCD, 0)
            vehicle = g_currentVehicle.item
            self.as_updateCurrentVehicleS(vehicle.userName, vehicle.type, getLobbyDescription(vehicle), xp, vehicle.isElite, g_currentVehicle.item.isPremiumIGR)
        else:
            self.as_updateCurrentVehicleS('', '', '', 0, False, False)

    def onVehicleTypeXPChanged(self, xps):
        if g_currentVehicle.isPresent():
            vehCD = g_currentVehicle.item.intCD
            if vehCD in xps:
                self.as_setEarnedXPS(xps[vehCD])

    def onVehicleBecomeElite(self, elite):
        if g_currentVehicle.isPresent():
            vehCD = g_currentVehicle.item.intCD
            if vehCD in elite:
                self.as_setEliteS(True)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\hangar\researchpanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:50:51 St�edn� Evropa (letn� �as)
