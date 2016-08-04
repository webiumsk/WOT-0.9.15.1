# 2016.08.04 19:59:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/idlelib/idle_test/test_text.py
import unittest
from test.test_support import requires
from _tkinter import TclError
import Tkinter as tk

class TextTest(object):
    hw = 'hello\nworld'
    hwn = hw + '\n'
    Text = None

    def setUp(self):
        self.text = self.Text()

    def test_init(self):
        self.assertEqual(self.text.get('1.0'), '\n')
        self.assertEqual(self.text.get('end'), '')

    def test_index_empty(self):
        index = self.text.index
        for dex in (-1.0, 0.3, '1.-1', '1.0', '1.0 lineend', '1.end', '1.33', 'insert'):
            self.assertEqual(index(dex), '1.0')

        for dex in ('end', 2.0, '2.1', '33.44'):
            self.assertEqual(index(dex), '2.0')

    def test_index_data(self):
        index = self.text.index
        self.text.insert('1.0', self.hw)
        for dex in (-1.0, 0.3, '1.-1', '1.0'):
            self.assertEqual(index(dex), '1.0')

        for dex in ('1.0 lineend', '1.end', '1.33'):
            self.assertEqual(index(dex), '1.5')

        for dex in ('end', '33.44'):
            self.assertEqual(index(dex), '3.0')

    def test_get(self):
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert('1.0', self.hw)
        Equal(get('end'), '')
        Equal(get('end', 'end'), '')
        Equal(get('1.0'), 'h')
        Equal(get('1.0', '1.1'), 'h')
        Equal(get('1.0', '1.3'), 'hel')
        Equal(get('1.1', '1.3'), 'el')
        Equal(get('1.0', '1.0 lineend'), 'hello')
        Equal(get('1.0', '1.10'), 'hello')
        Equal(get('1.0 lineend'), '\n')
        Equal(get('1.1', '2.3'), 'ello\nwor')
        Equal(get('1.0', '2.5'), self.hw)
        Equal(get('1.0', 'end'), self.hwn)
        Equal(get('0.0', '5.0'), self.hwn)

    def test_insert(self):
        insert = self.text.insert
        get = self.text.get
        Equal = self.assertEqual
        insert('1.0', self.hw)
        Equal(get('1.0', 'end'), self.hwn)
        insert('1.0', '')
        Equal(get('1.0', 'end'), self.hwn)
        insert('1.0', '*')
        Equal(get('1.0', 'end'), '*hello\nworld\n')
        insert('1.0 lineend', '*')
        Equal(get('1.0', 'end'), '*hello*\nworld\n')
        insert('2.3', '*')
        Equal(get('1.0', 'end'), '*hello*\nwor*ld\n')
        insert('end', 'x')
        Equal(get('1.0', 'end'), '*hello*\nwor*ldx\n')
        insert('1.4', 'x\n')
        Equal(get('1.0', 'end'), '*helx\nlo*\nwor*ldx\n')

    def test_no_delete(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert('1.0', self.hw)
        delete('insert')
        Equal(get('1.0', 'end'), self.hwn)
        delete('end')
        Equal(get('1.0', 'end'), self.hwn)
        delete('insert', 'end')
        Equal(get('1.0', 'end'), self.hwn)
        delete('insert', '5.5')
        Equal(get('1.0', 'end'), self.hwn)
        delete('1.4', '1.0')
        Equal(get('1.0', 'end'), self.hwn)
        delete('1.4', '1.4')
        Equal(get('1.0', 'end'), self.hwn)

    def test_delete_char(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert('1.0', self.hw)
        delete('1.0')
        Equal(get('1.0', '1.end'), 'ello')
        delete('1.0', '1.1')
        Equal(get('1.0', '1.end'), 'llo')
        delete('1.end')
        Equal(get('1.0', '1.end'), 'lloworld')
        self.text.insert('1.3', '\n')
        delete('1.10')
        Equal(get('1.0', '1.end'), 'lloworld')
        self.text.insert('1.3', '\n')
        delete('1.3', '2.0')
        Equal(get('1.0', '1.end'), 'lloworld')

    def test_delete_slice(self):
        delete = self.text.delete
        get = self.text.get
        Equal = self.assertEqual
        self.text.insert('1.0', self.hw)
        delete('1.0', '1.0 lineend')
        Equal(get('1.0', 'end'), '\nworld\n')
        delete('1.0', 'end')
        Equal(get('1.0', 'end'), '\n')
        self.text.insert('1.0', self.hw)
        delete('1.0', '2.0')
        Equal(get('1.0', 'end'), 'world\n')
        delete('1.0', 'end')
        Equal(get('1.0', 'end'), '\n')
        self.text.insert('1.0', self.hw)
        delete('1.2', '2.3')
        Equal(get('1.0', 'end'), 'held\n')

    def test_multiple_lines(self):
        self.text.insert('1.0', 'hello')
        self.text.insert('1.3', '1\n2\n3\n4\n5')
        self.assertEqual(self.text.get('1.0', 'end'), 'hel1\n2\n3\n4\n5lo\n')
        self.text.delete('1.3', '5.1')
        self.assertEqual(self.text.get('1.0', 'end'), 'hello\n')

    def test_compare(self):
        compare = self.text.compare
        Equal = self.assertEqual
        self.text.insert('1.0', 'First\nSecond\nThird\n')
        self.assertRaises(TclError, compare, '2.2', 'op', '2.2')
        for op, less1, less0, equal, greater0, greater1 in (('<',
          True,
          True,
          False,
          False,
          False),
         ('<=',
          True,
          True,
          True,
          False,
          False),
         ('>',
          False,
          False,
          False,
          True,
          True),
         ('>=',
          False,
          False,
          True,
          True,
          True),
         ('==',
          False,
          False,
          True,
          False,
          False),
         ('!=',
          True,
          True,
          False,
          True,
          True)):
            Equal(compare('1.1', op, '2.2'), less1, op)
            Equal(compare('2.1', op, '2.2'), less0, op)
            Equal(compare('2.2', op, '2.2'), equal, op)
            Equal(compare('2.3', op, '2.2'), greater0, op)
            Equal(compare('3.3', op, '2.2'), greater1, op)


class MockTextTest(TextTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from idlelib.idle_test.mock_tk import Text
        cls.Text = Text

    def test_decode(self):
        decode = self.text._decode
        Equal = self.assertEqual
        self.text.insert('1.0', self.hw)
        Equal(decode('end', -1), (2, 5))
        Equal(decode('3.1', -1), (2, 5))
        Equal(decode('end', 0), (2, 6))
        Equal(decode('3.1', 0), (2, 6))


class TkTextTest(TextTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        requires('gui')
        from Tkinter import Tk, Text
        cls.Text = Text
        cls.root = Tk()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()
        del cls.root


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\idle_test\test_text.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.08.04 19:59:50 St�edn� Evropa (letn� �as)
