import unittest
from unittest.mock import mock_open, patch
from jvpm.classfile import ClassFile


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
        self.assertEqual(self.cf.get_constant_pool(), 42)
