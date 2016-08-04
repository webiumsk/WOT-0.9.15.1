# 2016.08.04 19:52:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/formatters/__init__.py
import BigWorld
from debug_utils import LOG_WARNING
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from gui.shared.formatters import time_formatters
from gui.shared.formatters.currency import getBWFormatter
from gui.shared.money import Money, Currency
from helpers.i18n import makeString
__all__ = ('icons', 'text_styles', 'time_formatters')

def formatPrice(price, reverse = False):
    outPrice = []
    currencies = price.getSetCurrencies(byWeight=False)
    if not currencies:
        currencies = [Currency.CREDITS]
    for currency in currencies:
        formatter = getBWFormatter(currency)
        cname = makeString('#menu:price/{}'.format(currency)) + ': '
        cformatted = formatter(price.get(currency)) if formatter else price.get(currency)
        outPrice.append(''.join((cformatted, ' ', cname) if reverse else (cname, ' ', cformatted)))

    return ', '.join(outPrice)


def formatGoldPrice(gold, reverse = False):
    return formatPrice(Money(gold=gold), reverse)


def getGlobalRatingFmt(globalRating):
    if globalRating >= 0:
        return BigWorld.wg_getIntegralFormat(globalRating)
    return '--'
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\formatters\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:52:49 St�edn� Evropa (letn� �as)
