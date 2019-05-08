"""Class to test that class file returns the correct items"""
import unittest
import io
import sys
from unittest.mock import mock_open, patch
from jvpm.class_file import *


class TestClassFile(unittest.TestCase):
    """test class of reading java byte code"""

    def setUp(self):
        """finds the class file"""
        self.cf = ClassFile('jvpm/files/HelloWorld.class')

    def test_magic(self):
        """Make sure the magic number is 'CAFEBABE'"""
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        """Make sure minor version is 0"""
        self.assertEqual(self.cf.get_minor(), 0)

    def test_major(self):
        """Make sure major version is 52"""
        self.assertEqual(self.cf.get_major(), 52)

    def test_count_pool(self):
        """Confirms the count pool is 29"""
        self.assertEqual(self.cf.get_constant_pool(), 29)

    def test_hello_world(self):
        """Test to see if jvpm can return a print statement correctly"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        class_reader = ClassFile('jvpm/files/HelloWorld.class')
        class_reader.run_opcodes()
        val = captured_output.getvalue()
        self.assertEqual('Hello World!\n', val)

    def test_add_two(self):
        """Test to see if jvpm can run a simple calculator class correctly"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        class_reader = ClassFile('jvpm/files/AddTwo.class')
        with unittest.mock.patch('builtins.input', return_value=2):
            class_reader.run_opcodes()
        val = captured_output.getvalue()
        self.assertEqual('4\n', val)
