# 2016.08.04 19:51:55 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractTweenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class AbstractTweenMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    null
    """

    def initialiaze(self, props):
        """
        :param props:
        :return :
        """
        self._printOverrideError('initialiaze')

    def creatTweenPY(self, tween):
        """
        :param tween:
        :return :
        """
        self._printOverrideError('creatTweenPY')

    def getPaused(self):
        """
        :return Boolean:
        """
        self._printOverrideError('getPaused')

    def setPaused(self, paused):
        """
        :param paused:
        :return :
        """
        self._printOverrideError('setPaused')

    def getLoop(self):
        """
        :return Boolean:
        """
        self._printOverrideError('getLoop')

    def setLoop(self, loop):
        """
        :param loop:
        :return :
        """
        self._printOverrideError('setLoop')

    def getDuration(self):
        """
        :return uint:
        """
        self._printOverrideError('getDuration')

    def setDuration(self, duration):
        """
        :param duration:
        :return :
        """
        self._printOverrideError('setDuration')

    def getPosition(self):
        """
        :return uint:
        """
        self._printOverrideError('getPosition')

    def setPosition(self, position):
        """
        :param position:
        :return :
        """
        self._printOverrideError('setPosition')

    def getDelay(self):
        """
        :return uint:
        """
        self._printOverrideError('getDelay')

    def setDelay(self, delay):
        """
        :param delay:
        :return :
        """
        self._printOverrideError('setDelay')

    def resetAnim(self):
        """
        :return :
        """
        self._printOverrideError('resetAnim')

    def getTweenIdx(self):
        """
        :return uint:
        """
        self._printOverrideError('getTweenIdx')

    def getIsComplete(self):
        """
        :return Boolean:
        """
        self._printOverrideError('getIsComplete')

    def postponedCheckState(self):
        """
        :return :
        """
        self._printOverrideError('postponedCheckState')

    def getTargetDisplayObjectS(self):
        """
        :return flash.display.DisplayObject:
        """
        if self._isDAAPIInited():
            return self.flashObject.getTargetDisplayObject()

    def onAnimCompleteS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.onAnimComplete()

    def onAnimStartS(self):
        """
        :return :
        """
        if self._isDAAPIInited():
            return self.flashObject.onAnimStart()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\scaleform\framework\entities\abstract\abstracttweenmeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:51:55 St�edn� Evropa (letn� �as)
