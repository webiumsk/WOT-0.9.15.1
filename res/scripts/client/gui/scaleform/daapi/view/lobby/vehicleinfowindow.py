# 2016.08.04 19:50:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/VehicleInfoWindow.py
from gui.shared.items_parameters import formatters
from items import tankmen
from helpers import i18n
from debug_utils import LOG_ERROR
from gui.shared import g_itemsCache
from gui.Scaleform.daapi.view.meta.VehicleInfoMeta import VehicleInfoMeta

class VehicleInfoWindow(VehicleInfoMeta):

    def __init__(self, ctx = None):
        super(VehicleInfoWindow, self).__init__()
        vehicleCompactDescr = ctx.get('vehicleCompactDescr', 0)
        self.vehicleCompactDescr = vehicleCompactDescr

    def onCancelClick(self):
        self.destroy()

    def onWindowClose(self):
        self.destroy()

    def getVehicleInfo(self):
        vehicle = g_itemsCache.items.getItemByCD(self.vehicleCompactDescr)
        if vehicle is None:
            LOG_ERROR('There is error while showing vehicle info window: ', self.vehicleCompactDescr)
            return
        else:
            params = vehicle.getParams()
            tankmenParams = list()
            for slotIdx, tankman in vehicle.crew:
                role = vehicle.descriptor.type.crewRoles[slotIdx][0]
                tankmanLabel = ''
                if tankman is not None:
                    tankmanLabel = '%s %s (%d%%)' % (tankman.rankUserName, tankman.lastUserName, tankman.roleLevel)
                tankmenParams.append({'tankmanType': i18n.convert(tankmen.getSkillsConfig()[role].get('userString', '')),
                 'value': tankmanLabel})

            paramsList = formatters.getFormattedParamsList(vehicle.descriptor, params['parameters'], excludeRelative=True)
            info = {'vehicleName': vehicle.longUserName,
             'vehicleDiscription': vehicle.fullDescription,
             'vehicleImage': vehicle.icon,
             'vehicleLevel': vehicle.level,
             'vehicleNation': vehicle.nationID,
             'vehicleElite': vehicle.isElite,
             'vehicleType': vehicle.type,
             'VehicleInfoPropsData': [ {'name': n,
                                      'value': v} for n, v in paramsList ],
             'VehicleInfoBaseData': params['base'],
             'VehicleInfoCrewData': tankmenParams}
            self.as_setVehicleInfoS(info)
            return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\lobby\vehicleinfowindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:50:12 St�edn� Evropa (letn� �as)
