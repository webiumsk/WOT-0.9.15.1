# 2016.08.04 19:49:08 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/login/aspects.py
from helpers import aop

class ShowBGInsteadVideo(aop.Aspect):

    def __init__(self):
        super(ShowBGInsteadVideo, self).__init__()

    def atCall(self, cd):
        super(ShowBGInsteadVideo, self).atCall(cd)
        cd.self._showOnlyStaticBackground()
        cd.avoid()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\login\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:49:08 Støední Evropa (letní èas)
