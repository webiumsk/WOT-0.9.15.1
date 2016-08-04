# 2016.08.04 19:54:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/vehicle_systems/components/highlighter.py
import BigWorld
from gui.battle_control import g_sessionProvider
from vehicle_systems import assembly_utility

class Highlighter(assembly_utility.Component):
    HIGHLIGHT_OFF = 0
    HIGHLIGHT_SIMPLE = 1
    HIGHLIGHT_ON = 2
    status = property(lambda self: self.__highlightStatus)

    @property
    def enabled(self):
        return self.__highlightStatus != self.HIGHLIGHT_OFF

    def __init__(self, vehicle):
        super(Highlighter, self).__init__()
        self.__vehicle = vehicle
        self.__highlightStatus = self.HIGHLIGHT_OFF

    def destroy(self):
        if self.__highlightStatus != self.HIGHLIGHT_OFF:
            BigWorld.wgDelEdgeDetectEntity(self.__vehicle)
            self.__highlightStatus = self.HIGHLIGHT_OFF
        self.__vehicle = None
        return

    def highlight(self, enable, forceSimpleEdge = False):
        vehicle = self.__vehicle
        if self.__highlightStatus != self.HIGHLIGHT_OFF:
            BigWorld.wgDelEdgeDetectEntity(vehicle)
        args = (0, 1, True)
        if enable:
            if vehicle.isPlayerVehicle:
                if forceSimpleEdge:
                    self.__highlightStatus |= self.HIGHLIGHT_SIMPLE
                    args = (0, 0, False)
                else:
                    self.__highlightStatus |= self.HIGHLIGHT_ON
                    args = (0, 1, True)
            else:
                self.__highlightStatus |= self.HIGHLIGHT_ON
                arenaDP = g_sessionProvider.getArenaDP()
                isAllyTeam = arenaDP.isAllyTeam(vehicle.publicInfo['team'])
                args = (2, 0, False) if isAllyTeam else (1, 0, False)
        elif vehicle.isPlayerVehicle and forceSimpleEdge:
            self.__highlightStatus &= ~self.HIGHLIGHT_SIMPLE
            args = (0, 1, True)
        else:
            self.__highlightStatus &= ~self.HIGHLIGHT_ON
        self.__doHighlightOperation(self.__highlightStatus, args)

    def __doHighlightOperation(self, status, args):
        if status != self.HIGHLIGHT_OFF:
            BigWorld.wgAddEdgeDetectEntity(self.__vehicle, args[0], args[1], args[2])
        else:
            BigWorld.wgDelEdgeDetectEntity(self.__vehicle)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\vehicle_systems\components\highlighter.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:54:57 St�edn� Evropa (letn� �as)
