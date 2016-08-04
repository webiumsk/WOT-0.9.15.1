# 2016.08.04 19:47:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/ReloadEffect.py
from helpers.CallbackDelayer import CallbackDelayer
from helpers import gEffectsDisabled
import SoundGroups

def _createReloadEffectDesc(type, dataSection):
    if len(dataSection.values()) == 0:
        return None
    elif type == 'SimpleReload':
        return _SimpleReloadDesc(dataSection)
    else:
        return None


class _ReloadDesc(object):

    def __init__(self):
        pass

    def create(self):
        return None


class _SimpleReloadDesc(_ReloadDesc):

    def __init__(self, dataSection):
        super(_SimpleReloadDesc, self).__init__()
        self.duration = dataSection.readFloat('duration', 0.0) / 1000.0
        self.soundEvent = dataSection.readString('sound', '')

    def create(self):
        return SimpleReload(self)


def effectFromSection(section):
    type = section.readString('type', '')
    return _createReloadEffectDesc(type, section)


class SimpleReload(CallbackDelayer):

    def __init__(self, effectDesc):
        CallbackDelayer.__init__(self)
        self.__desc = effectDesc
        self.__sound = None
        return

    def __del__(self):
        if self.__sound is not None:
            self.__sound.stop()
            self.__sound = None
        CallbackDelayer.destroy(self)
        return

    def start(self, reloadTime):
        if gEffectsDisabled():
            return
        else:
            if self.__sound is None:
                self.__sound = SoundGroups.g_instance.getSound2D(self.__desc.soundEvent)
            else:
                self.__sound.stop()
            time = reloadTime - self.__desc.duration
            if time > 0.0:
                self.delayCallback(time, self.__startEvent)
            return

    def stop(self):
        if self.__sound is not None:
            self.__sound.stop()
            self.__sound = None
        self.stopCallback(self.__startEvent)
        return

    def __startEvent(self):
        if self.__sound is not None:
            self.__sound.stop()
            self.__sound.play()
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\reloadeffect.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:47:46 St�edn� Evropa (letn� �as)
