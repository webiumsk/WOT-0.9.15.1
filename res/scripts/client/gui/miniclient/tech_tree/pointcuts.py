# 2016.08.04 19:49:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/miniclient/tech_tree/pointcuts.py
import aspects
from helpers import aop

class OnTechTreePopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.techtree.TechTree', 'TechTree', '_populate', aspects=(aspects.OnTechTreePopulate,))


class OnBuyVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.VehicleBuyWindow', 'VehicleBuyWindow', 'submit', aspects=(aspects.OnBuyVehicle(config),))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\tech_tree\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:09 St�edn� Evropa (letn� �as)
