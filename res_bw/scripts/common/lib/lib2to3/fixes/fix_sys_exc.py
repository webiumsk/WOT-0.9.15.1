# 2016.08.04 20:00:19 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_sys_exc.py
"""Fixer for sys.exc_{type, value, traceback}

sys.exc_type -> sys.exc_info()[0]
sys.exc_value -> sys.exc_info()[1]
sys.exc_traceback -> sys.exc_info()[2]
"""
from .. import fixer_base
from ..fixer_util import Attr, Call, Name, Number, Subscript, Node, syms

class FixSysExc(fixer_base.BaseFix):
    exc_info = [u'exc_type', u'exc_value', u'exc_traceback']
    BM_compatible = True
    PATTERN = "\n              power< 'sys' trailer< dot='.' attribute=(%s) > >\n              " % '|'.join(("'%s'" % e for e in exc_info))

    def transform(self, node, results):
        sys_attr = results['attribute'][0]
        index = Number(self.exc_info.index(sys_attr.value))
        call = Call(Name(u'exc_info'), prefix=sys_attr.prefix)
        attr = Attr(Name(u'sys'), call)
        attr[1].children[0].prefix = results['dot'].prefix
        attr.append(Subscript(index))
        return Node(syms.power, attr, prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_sys_exc.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 20:00:19 St�edn� Evropa (letn� �as)
