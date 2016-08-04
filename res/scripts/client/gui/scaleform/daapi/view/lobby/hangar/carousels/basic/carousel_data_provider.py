# 2016.08.04 19:50:52 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/basic/carousel_data_provider.py
from gui import GUI_NATIONS_ORDER_INDEX
from gui.shared.formatters import icons, text_styles
from gui.shared.formatters.time_formatters import RentLeftFormatter
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER_INDICES
from gui.shared.money import Money
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from helpers import i18n
_UPDATE_LOCKS_PERIOD = 60

class _SUPPLY_ITEMS(object):
    BUY_TANK = 0
    BUY_SLOT = 1
    ALL = (BUY_TANK, BUY_SLOT)


def _sortedIndices(seq, getter):
    """ Sort the sequence by value fetched by getter func and return the
    list with indices of items in the original list
    
    For example, original list is: a = [3, 2, 1, 4].
    Output will be [2, 1, 0, 3], like a[2] is first, then a[1], etc.
    
    :param seq: original list
    :param getter: function that fetches values from the original list
    :return: indices in the original list
    """
    return sorted(range(len(seq)), key=lambda idx: getter(seq[idx]))


def _vehicleComparisonKey(vehicle):
    """ Get comparison key for a vehicle.
    
    :param vehicle: instance of gui_items.Vehicle
    :return: tuple with comparison keys
    """
    return (not vehicle.isEvent,
     not vehicle.isFavorite,
     GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
     VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
     vehicle.level,
     vehicle.buyPrice.gold,
     vehicle.buyPrice.credits,
     vehicle.userName)


def _getStatusString(vState, vStateLvl):
    if vState == Vehicle.VEHICLE_STATE.IN_PREMIUM_IGR_ONLY:
        status = i18n.makeString('#menu:tankCarousel/vehicleStates/{}'.format(vState), icon=icons.premiumIgrSmall())
    else:
        status = i18n.makeString('#menu:tankCarousel/vehicleStates/{}'.format(vState))
    if not status:
        return status
    elif vStateLvl == Vehicle.VEHICLE_STATE_LEVEL.CRITICAL:
        return text_styles.vehicleStatusCriticalText(status)
    else:
        return text_styles.vehicleStatusInfoText(status)


class CarouselDataProvider(SortableDAAPIDataProvider):

    def __init__(self, carouselFilter, itemsCache, currentVehicle):
        super(CarouselDataProvider, self).__init__()
        self._baseCriteria = REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.VEHICLE.ONLY_FOR_FALLOUT
        self._filter = carouselFilter
        self._itemsCache = itemsCache
        self._currentVehicle = currentVehicle
        self._vehicles = []
        self._vehicleItems = []
        self._supplyItems = []
        self._filteredIndices = []
        self._selectedIdx = -1
        self._emptySlotsCount = 0
        self._filter.load()

    def hasRentedVehicles(self):
        """ Returns True if there is at least one rented vehicle, False otherwise
        """
        return bool(self._getFilteredVehicles(REQ_CRITERIA.VEHICLE.RENT))

    def getTotalVehiclesCount(self):
        """ Get number of vehicles without applied filter.
        """
        return len(self._vehicles)

    def getCurrentVehiclesCount(self):
        """ Get number of vehicles with applied filter.
        """
        return len(self._getCurrentVehicles())

    @property
    def filter(self):
        return self._filter

    @property
    def collection(self):
        return self._vehicleItems + self._supplyItems

    def pyGetSelectedIdx(self):
        return self._selectedIdx

    def emptyItem(self):
        return None

    def clear(self):
        self._vehicles = []
        self._vehicleItems = []
        self._supplyItems = []
        self._filteredIndices = []
        self._selectedIdx = -1

    def fini(self):
        self.clear()
        self._dispose()

    def updateSupplies(self):
        """ Update the supply slots: 'buy tank' and 'buy slot'.
        """
        self._supplyItems = []
        self._buildSupplyItems()
        self.flashObject.invalidateItems(self.__getSupplyIndices(), self._supplyItems)
        self.applyFilter()

    def updateVehicles(self, vehicles = None, filterCriteria = None):
        isFullResync = vehicles is None and filterCriteria is None
        filterCriteria = filterCriteria or REQ_CRITERIA.EMPTY
        if vehicles:
            filterCriteria |= REQ_CRITERIA.IN_CD_LIST(vehicles)
        vehiclesCollection = self._itemsCache.items.getVehicles(self._baseCriteria | filterCriteria)
        isVehicleRemoved = not set(vehicles or ()).issubset(vehiclesCollection.viewkeys())
        isVehicleAdded = not set(vehicles or ()).issubset(self._vehicles)
        if isFullResync or isVehicleAdded or isVehicleRemoved:
            self.buildList()
        else:
            updateIndices = []
            updateVehicles = []
            for intCD, newVehicle in vehiclesCollection.iteritems():
                for idx, oldVehicle in enumerate(self._vehicles):
                    if oldVehicle.invID == newVehicle.invID:
                        self._vehicleItems[idx] = self._getVehicleDataVO(newVehicle)
                        self._vehicles[idx] = newVehicle
                        updateIndices.append(idx)
                        updateVehicles.append(self._vehicleItems[idx])

            self.flashObject.invalidateItems(updateIndices, updateVehicles)
            self.applyFilter()
        return

    def buildList(self):
        self.clear()
        self._buildVehicleItems()
        self._buildSupplyItems()
        self.refresh()
        self.applyFilter()

    def applyFilter(self):
        """ Apply filters and sort items in the carousel.
        """
        prevFilteredIndices = self._filteredIndices[:]
        self._filteredIndices = []
        if self._currentVehicle.isPresent():
            currentVehicleInvID = self._currentVehicle.item.invID
        else:
            currentVehicleInvID = None
        selectedItemID = -1
        visibleVehiclesInvIDs = [ vehicle.invID for vehicle in self._getCurrentVehicles() ]
        sortedVehicleIndices = _sortedIndices(self._vehicles, _vehicleComparisonKey)
        for idx in sortedVehicleIndices:
            vehicle = self._vehicles[idx]
            if vehicle.invID in visibleVehiclesInvIDs:
                self._filteredIndices.append(idx)
                if currentVehicleInvID == vehicle.invID:
                    selectedItemID = len(self._filteredIndices) - 1

        supplyIndices = self.__getSupplyIndices()
        if not self._emptySlotsCount:
            supplyIndices.pop(_SUPPLY_ITEMS.BUY_TANK)
        self._filteredIndices += supplyIndices
        self._selectedIdx = selectedItemID
        if prevFilteredIndices != self._filteredIndices:
            self.flashObject.as_setFilter(self._filteredIndices)
        return

    def _populate(self):
        super(CarouselDataProvider, self)._populate()

    def _dispose(self):
        self._filter = None
        self._itemsCache = None
        self._currentVehicle = None
        super(CarouselDataProvider, self)._dispose()
        return

    def _getVehicleDataVO(self, vehicle):
        rentInfoStr = RentLeftFormatter(vehicle.rentInfo, vehicle.isPremiumIGR).getRentLeftStr()
        vState, vStateLvl = vehicle.getState()
        infoText = _getStatusString(vState, vStateLvl)
        return {'id': vehicle.invID,
         'showInfoText': bool(infoText),
         'infoText': infoText,
         'clanLock': vehicle.clanLock,
         'lockBackground': vStateLvl == Vehicle.VEHICLE_STATE_LEVEL.CRITICAL,
         'tankIconData': {'image': vehicle.icon,
                          'label': vehicle.shortUserName if vehicle.isPremiumIGR else vehicle.userName,
                          'level': vehicle.level,
                          'elite': vehicle.isElite,
                          'premium': vehicle.isPremium,
                          'favorite': vehicle.isFavorite,
                          'nation': vehicle.nationID,
                          'doubleXPReceived': vehicle.dailyXPFactor,
                          'tankType': vehicle.type,
                          'rentLeft': rentInfoStr}}

    def _buildVehicleItems(self):
        self._vehicles = []
        self._vehicleItems = []
        vehicleIcons = []
        vehiclesCollection = self._itemsCache.items.getVehicles(self._baseCriteria)
        for intCD, vehicle in vehiclesCollection.iteritems():
            vehicleIcons.append(vehicle.icon)
            self._vehicles.append(vehicle)
            self._vehicleItems.append(self._getVehicleDataVO(vehicle))

        self.app.imageManager.loadImages(vehicleIcons)

    def _buildSupplyItems(self):
        self._supplyItems = []
        items = self._itemsCache.items
        slots = items.stats.vehicleSlots
        vehicles = len(items.getVehicles(REQ_CRITERIA.INVENTORY))
        slotPrice = items.shop.getVehicleSlotsPrice(slots)
        defaultSlotPrice = items.shop.defaults.getVehicleSlotsPrice(slots)
        if slotPrice != defaultSlotPrice:
            sale = packActionTooltipData(ACTION_TOOLTIPS_TYPE.ECONOMICS, 'slotsPrices', True, Money(gold=slotPrice), Money(gold=defaultSlotPrice))
        else:
            sale = None
        self._emptySlotsCount = slots - vehicles
        self._supplyItems.append({'buyTank': True,
         'additionalText': i18n.makeString('#menu:tankCarousel/vehicleStates/buyTankEmptyCount', count=self._emptySlotsCount),
         'showInfoText': True,
         'infoText': _getStatusString('buyTank', Vehicle.VEHICLE_STATE_LEVEL.INFO),
         'icon': RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_TANK})
        buySlotVO = {'buySlot': True,
         'slotPrice': slotPrice,
         'icon': RES_ICONS.MAPS_ICONS_LIBRARY_TANKITEM_BUY_SLOT,
         'showInfoText': True,
         'infoText': _getStatusString('buySlot', Vehicle.VEHICLE_STATE_LEVEL.INFO),
         'hasSale': sale is not None}
        if sale is not None:
            buySlotVO.update({'slotPriceActionData': sale})
        self._supplyItems.append(buySlotVO)
        return

    def _getCurrentVehicles(self):
        """ Get the vehicles that left with applied filter.
        """
        return self._getFilteredVehicles(self._filter.apply)

    def _getFilteredVehicles(self, criteria):
        """ Get the vehicles that left with applied filter criteria.
        """
        return [ vehicle for vehicle in self._vehicles if criteria(vehicle) ]

    def __getSupplyIndices(self):
        """ Get the indices of supply items relatively to the vehicles list.
        Supply items go after the vehicles, but they're in separate list.
        
        :return: list of supply items indices
        """
        return [ len(self._vehicles) + idx for idx in _SUPPLY_ITEMS.ALL ]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\hangar\carousels\basic\carousel_data_provider.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:50:52 St�edn� Evropa (letn� �as)
