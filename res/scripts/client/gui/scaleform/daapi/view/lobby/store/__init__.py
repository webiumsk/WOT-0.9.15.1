# 2016.08.04 19:51:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/store/__init__.py
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.store.Inventory import Inventory
    from gui.Scaleform.daapi.view.lobby.store.Shop import Shop
    from gui.Scaleform.daapi.view.lobby.store.StoreView import StoreView
    from gui.Scaleform.daapi.view.lobby.store.StoreTable import StoreTable
    return (ViewSettings(VIEW_ALIAS.LOBBY_STORE, StoreView, 'store.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_STORE, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.SHOP_TABLE, StoreTable, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.LOBBY_INVENTORY, Inventory, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(VIEW_ALIAS.LOBBY_SHOP, Shop, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (StorePackageBusinessHandler(),)


class StorePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.LOBBY_INVENTORY, self.loadViewByCtxEvent), (VIEW_ALIAS.LOBBY_STORE, self.loadViewByCtxEvent))
        super(StorePackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\store\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:16 St�edn� Evropa (letn� �as)
