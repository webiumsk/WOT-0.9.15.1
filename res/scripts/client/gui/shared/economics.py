# 2016.08.04 19:52:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/economics.py
from gui.shared.money import Money, ZERO_MONEY, Currency

def getActionPrc(price, defaultPrice):

    def calculate(price, defaultPrice):
        if defaultPrice == 0 or price == defaultPrice:
            return 0
        return int(round((1 - float(price) / defaultPrice) * 100))

    if isinstance(price, Money):
        for currency in Currency.BY_WEIGHT:
            value = calculate(price.get(currency), defaultPrice.get(currency))
            if value > 0:
                return value

        return 0
    return calculate(price, defaultPrice)


def calcRentPackages(vehicle, proxy):
    result = []
    if proxy is not None and vehicle.isRentable:
        rentCost = proxy.shop.getVehicleRentPrices().get(vehicle.intCD, {})
        defaultRentCost = proxy.shop.defaults.getVehicleRentPrices().get(vehicle.intCD, {})
        if len(rentCost) and len(defaultRentCost) is not None:
            for key in sorted(rentCost.keys()):
                rentPrice = Money(*rentCost[key].get('cost', ZERO_MONEY))
                defaultRentPrice = Money(*defaultRentCost.get(key, {}).get('cost', rentPrice))
                result.append({'days': key,
                 'rentPrice': rentPrice,
                 'defaultRentPrice': defaultRentPrice})

    return result


def getPremiumCostActionPrc(discounts, packet, proxy):
    defaultPremiumCost = proxy.shop.defaults.premiumCost
    premiumCost = proxy.shop.getPremiumCostWithDiscount(discounts)
    return getActionPrc(premiumCost.get(packet), defaultPremiumCost.get(packet))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\economics.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:52:45 St�edn� Evropa (letn� �as)
