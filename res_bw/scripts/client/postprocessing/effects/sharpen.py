# 2016.08.04 19:56:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/PostProcessing/Effects/Sharpen.py
from PostProcessing.RenderTargets import *
from PostProcessing import Effect
from PostProcessing.Phases import build9TapFilterPhase
from PostProcessing.Phases import buildBackBufferCopyPhase
from PostProcessing.FilterKernels import *
from PostProcessing import chain
from PostProcessing.Effects.Properties import *
from PostProcessing.Effects import implementEffectFactory
import Math
amount = MaterialFloatProperty('Sharpen', -1, 'alpha', primary=True)

@implementEffectFactory('Sharpen', 'Sharpen the edges of the scene.')
def sharpen():
    """This method creates and returns a post-process effect that sharpens
    the back buffer.  It does this by using a generic sharpening filter kernel.
    """
    backBufferCopy = rt('PostProcessing/backBufferCopy')
    c = buildBackBufferCopyPhase(backBufferCopy)
    s = build9TapFilterPhase(backBufferCopy.texture, None, sharpFilter)
    e = Effect()
    e.name = 'Sharpen'
    e.phases = [c, s]
    return e
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\client\postprocessing\effects\sharpen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:56:21 St�edn� Evropa (letn� �as)
