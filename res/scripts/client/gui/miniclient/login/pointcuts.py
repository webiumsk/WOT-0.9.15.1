# 2016.08.04 19:49:08 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/login/pointcuts.py
import aspects
from helpers import aop

class ShowBGInsteadVideo(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.login.LoginView', 'LoginView', '_showBackground', aspects=(aspects.ShowBGInsteadVideo,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\login\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:08 Støední Evropa (letní èas)
