# 2016.08.04 20:00:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_raise.py
"""Fixer for 'raise E, V, T'

raise         -> raise
raise E       -> raise E
raise E, V    -> raise E(V)
raise E, V, T -> raise E(V).with_traceback(T)
raise E, None, T -> raise E.with_traceback(T)

raise (((E, E'), E''), E'''), V -> raise E(V)
raise "foo", V, T               -> warns about string exceptions


CAVEATS:
1) "raise E, V" will be incorrectly translated if V is an exception
   instance. The correct Python 3 idiom is

        raise E from V

   but since we can't detect instance-hood by syntax alone and since
   any client code would have to be changed as well, we don't automate
   this.
"""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, Attr, ArgList, is_tuple

class FixRaise(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    raise_stmt< 'raise' exc=any [',' val=any [',' tb=any]] >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results['exc'].clone()
        if exc.type == token.STRING:
            msg = 'Python 3 does not support string exceptions'
            self.cannot_convert(node, msg)
            return
        if is_tuple(exc):
            while is_tuple(exc):
                exc = exc.children[1].children[0].clone()

            exc.prefix = u' '
        if 'val' not in results:
            new = pytree.Node(syms.raise_stmt, [Name(u'raise'), exc])
            new.prefix = node.prefix
            return new
        val = results['val'].clone()
        if is_tuple(val):
            args = [ c.clone() for c in val.children[1:-1] ]
        else:
            val.prefix = u''
            args = [val]
        if 'tb' in results:
            tb = results['tb'].clone()
            tb.prefix = u''
            e = exc
            if val.type != token.NAME or val.value != u'None':
                e = Call(exc, args)
            with_tb = Attr(e, Name(u'with_traceback')) + [ArgList([tb])]
            new = pytree.Node(syms.simple_stmt, [Name(u'raise')] + with_tb)
            new.prefix = node.prefix
            return new
        else:
            return pytree.Node(syms.raise_stmt, [Name(u'raise'), Call(exc, args)], prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib2to3\fixes\fix_raise.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 20:00:18 St�edn� Evropa (letn� �as)
