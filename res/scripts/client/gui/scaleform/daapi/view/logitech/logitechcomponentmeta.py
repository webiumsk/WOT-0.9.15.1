# 2016.08.04 19:51:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/logitech/LogitechComponentMeta.py
"""
Hand-made!
We imitate DAAPI hierarchy for AS2 flash used in Logitech Monitor
"""

class LogitechMonitorComponentMeta(object):

    def __init__(self):
        super(LogitechMonitorComponentMeta, self).__init__()
        self._flashObject = None
        return

    def _populate(self, flashObject):
        raise flashObject is not None or AssertionError
        self._flashObject = flashObject
        return True

    def _dispose(self):
        if self._flashObject is not None:
            self._flashObject = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\daapi\view\logitech\logitechcomponentmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:26 St�edn� Evropa (letn� �as)
