# 2016.08.04 19:50:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/RosterSlotSettingsWindow.py
from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.lobby.cyberSport.VehicleSelectorBase import VehicleSelectorBase
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleVO, makeFiltersVO
from gui.Scaleform.daapi.view.meta.RosterSlotSettingsWindowMeta import RosterSlotSettingsWindowMeta
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shared.ItemsCache import g_itemsCache
from gui.shared.events import CSRosterSlotSettingsWindow
from gui.shared.formatters import text_styles, icons
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
VEHICLE_SELECTOR_TAB_ID = 'vehicleSelectorTab'
RANGE_SELECTOR_TAB_ID = 'rangeSelectorTab'
TAB_ORDER = [VEHICLE_SELECTOR_TAB_ID, RANGE_SELECTOR_TAB_ID]
TAB_DATA_MAP = {VEHICLE_SELECTOR_TAB_ID: (CYBER_SPORT_ALIASES.VEHICLE_SELECTOR_VIEW, CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TABBTNLBL_VEHICLE),
 RANGE_SELECTOR_TAB_ID: (CYBER_SPORT_ALIASES.RANGE_ROSTER_SETTINGS_VIEW, CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TABBTNLBL_RANGE)}

class RosterSlotSettingsWindow(RosterSlotSettingsWindowMeta, VehicleSelectorBase):

    def __init__(self, ctx = None):
        super(RosterSlotSettingsWindow, self).__init__()
        raise 'section' in ctx or AssertionError('Section is required to show selector popup')
        self.__section = ctx.get('section')
        self.__levelsRange = ctx.get('levelsRange', [1, 10])
        self.__levelsLimits = self.__convertLevelsRange(self.__levelsRange)
        self.__vehicleTypes = ctx.get('vehicleTypes', None)
        self.__flashSlots = ctx.get('settings')
        return

    def updateSlots(self, slots):
        self.__currentSlot, tabID = self.__makeInitialSlotData(slots.pop())
        self.__setSelection(tabID)

    def onFiltersUpdate(self, nation, vehicleType, isMain, level, compatibleOnly):
        self._updateFilter(nation, vehicleType, isMain, level, compatibleOnly)
        self.updateData()

    def updateData(self):
        result = self._updateData(g_itemsCache.items.getVehicles(~REQ_CRITERIA.SECRET), self.__levelsRange, self.__vehicleTypes, isVehicleRoster=True)
        self.as_setListDataS(result)

    def requestVehicleFilters(self):
        filters = AccountSettings.getFilter(self.__section)
        filters['isMain'] = False
        result = self._initFilter(**filters)
        self.as_updateVehicleFiltersS(result)

    def submitButtonHandler(self, value):
        self.__currentSlot, _ = self.__makeInitialSlotData(value)
        self.fireEvent(CSRosterSlotSettingsWindow(CSRosterSlotSettingsWindow.APPLY_SLOT_SETTINGS, self.__getSlotsSettings()))
        self.onWindowClose()

    def cancelButtonHandler(self):
        self.onWindowClose()

    def onWindowClose(self):
        self.destroy()

    def _getLevelsRange(self):
        return [0] + self.__levelsRange

    def _populate(self):
        super(RosterSlotSettingsWindow, self)._populate()
        self.as_setStaticDataS(self.__packStaticData())
        self.__currentSlot, tabID = self.__makeInitialSlotData(self.__flashSlots.pop())
        self.setLimits()
        self.__setSelection(tabID)

    def setLimits(self):
        self.as_setRosterLimitsS({'minLevel': self.__levelsLimits[0],
         'maxLevel': self.__levelsLimits[1]})

    def _dispose(self):
        currentFilters = self.getFilters()
        if currentFilters:
            filters = {'nation': currentFilters['nation'],
             'vehicleType': currentFilters['vehicleType'],
             'isMain': currentFilters['isMain'],
             'level': currentFilters['level'],
             'compatibleOnly': currentFilters['compatibleOnly']}
            AccountSettings.setFilter(self.__section, filters)
        self.__currentSlot = None
        self.__flashSlots = None
        self.__section = None
        self.__levelsRange = None
        self.__vehicleTypes = None
        super(RosterSlotSettingsWindow, self)._dispose()
        return

    def __packStaticData(self):
        text = text_styles.main(CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_HEADERTEXT)
        return {'windowTitle': CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_TITLE,
         'headerText': '%s %s' % (text, icons.info()),
         'headerTextTooltip': TOOLTIPS.CYBERSPORT_ROSTERSLOTSETTINGS_HEADERTEXT,
         'selectedTxt': text_styles.middleTitle(CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_BOTTOMRESULT),
         'submitBtnLabel': CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_SUBMITBTN,
         'cancelBtnLabel': CYBERSPORT.WINDOW_ROSTERSLOTSETTINGS_VEHICLETAB_CANCELBTN,
         'buttonBarItems': self.__packTabsData()}

    def __packTabsData(self):
        data = []
        for id in TAB_ORDER:
            linkage, label = TAB_DATA_MAP[id]
            data.append({'label': label,
             'linkage': linkage})

        return data

    def __setSelection(self, tabID):
        if tabID == VEHICLE_SELECTOR_TAB_ID:
            self.as_setVehicleSelectionS(self.__currentSlot)
            self.as_selectTabS(TAB_ORDER.index(tabID))
        elif tabID == RANGE_SELECTOR_TAB_ID:
            self.as_setRangeSelectionS(self.__currentSlot)
            self.as_selectTabS(TAB_ORDER.index(tabID))
        else:
            self.as_resetSelectionS()
            self.as_selectTabS(TAB_ORDER.index(VEHICLE_SELECTOR_TAB_ID))

    def __makeInitialSlotData(self, currentSlotSetting):
        if currentSlotSetting is None:
            return (makeFiltersVO([], [], self.__convertLevelsRange(self.__levelsRange)), RANGE_SELECTOR_TAB_ID)
        elif currentSlotSetting.selectedVehicle > 0:
            vehicle = g_itemsCache.items.getItemByCD(int(currentSlotSetting.selectedVehicle))
            return (makeVehicleVO(vehicle, self.__convertLevelsRange(self.__levelsRange), self.__vehicleTypes), VEHICLE_SELECTOR_TAB_ID)
        elif currentSlotSetting.nationIDRange or currentSlotSetting.vTypeRange or currentSlotSetting.vLevelRange:
            levelsRange = self.__convertLevelsRange(currentSlotSetting.vLevelRange or self.__levelsRange)
            return (makeFiltersVO(currentSlotSetting.nationIDRange, currentSlotSetting.vTypeRange, levelsRange), RANGE_SELECTOR_TAB_ID)
        else:
            return (None, None)
            return

    def __convertLevelsRange(self, levels):
        return levels[::len(levels) - 1]

    def __getSlotsSettings(self):
        slotsSettings = []
        slotsSettings.extend(self.__flashSlots)
        slotsSettings.append(self.__currentSlot)
        return slotsSettings
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\cybersport\rosterslotsettingswindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:50:30 St�edn� Evropa (letn� �as)
