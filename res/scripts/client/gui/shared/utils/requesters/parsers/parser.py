# 2016.08.04 19:53:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/utils/requesters/parsers/Parser.py


class Parser(object):

    @staticmethod
    def parseVehicles(data):
        return data

    @staticmethod
    def parseModules(data, type):
        return data

    @staticmethod
    def getParser(itemTypeID):
        if itemTypeID == 1:
            return Parser.parseVehicles
        return lambda data: Parser.parseModules(data, itemTypeID)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\utils\requesters\parsers\parser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:53:31 St�edn� Evropa (letn� �as)
