import unittest
import io
import sys
from unittest.mock import mock_open, patch
from jvpm.ClassFile import *


class TestClassFile(unittest.TestCase):
    # test class of reading java byte code

    def setUp(self):
        self.cf = ClassFile('jvpm/files/HelloWorld.class')

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 0)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 52)

    def test_count_pool(self):
        self.assertEqual(self.cf.get_constant_pool(), 29)

    def test_hello_world(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        class_reader = ClassFile('jvpm/files/HelloWorld.class')
        class_reader.run_opcodes()
        val = captured_output.getvalue()
        self.assertEqual('Hello World!\n', val)

    def test_add_two(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        class_reader = ClassFile('jvpm/files/AddTwo.class')
        with unittest.mock.patch('builtins.input', return_value=2):
            class_reader.run_opcodes()
        val = captured_output.getvalue()
        self.assertEqual('4\n', val)