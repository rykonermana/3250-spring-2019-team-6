import unittest
from unittest.mock import mock_open, patch
from jvpm.constant_table import ConstantTable


class TestClassFile(unittest.TestCase):

    def setUp(self):
        self.data = b'\xca\xfe\xba\xbe\x00\x00\x004\x00\x1b\n\x00\x05\x00\x0e\t\x00\x0f\x00\x10\n\x00\x11\x00\x12\x07\x00\x13\x07\x00\x14\x01\x00\x06<init>\x01\x00\x03()V\x01\x00\x04Code\x01\x00\x0fLineNumberTable\x01\x00\x04main\x01\x00\x16([Ljava/lang/String;)V\x01\x00\nSourceFile\x01\x00\x0fHelloWorld.java\x0c\x00\x06\x00\x07\x07\x00\x15\x0c\x00\x16\x00\x17\x07\x00\x18\x0c\x00\x19\x00\x1a\x01\x00\nHelloWorld\x01\x00\x10java/lang/Object\x01\x00\x10java/lang/System\x01\x00\x03out\x01\x00\x15Ljava/io/PrintStream;\x01\x00\x13java/io/PrintStream\x01\x00\x07println\x01\x00\x04(I)V\x00!\x00\x04\x00\x05\x00\x00\x00\x00\x00\x02\x00\x01\x00\x06\x00\x07\x00\x01\x00\x08\x00\x00\x00\x1d\x00\x01\x00\x01\x00\x00\x00\x05*\xb7\x00\x01\xb1\x00\x00\x00\x01\x00\t\x00\x00\x00\x06\x00\x01\x00\x00\x00\x01\x00\t\x00\n\x00\x0b\x00\x01\x00\x08\x00\x00\x00%\x00\x02\x00\x01\x00\x00\x00\t\xb2\x00\x02\x10\x07\xb6\x00\x03\xb1\x00\x00\x00\x01\x00\t\x00\x00\x00\n\x00\x02\x00\x00\x00\x03\x00\x08\x00\x04\x00\x01\x00\x0c\x00\x00\x00\x02\x00\r'
        self.count = 26
        self.constant_table_pre = {
            1: {'constant_code': 10, 'message': b'\x00\x05\x00\x0e', 'decrypted_message': 'java/lang/Object.<init>:()V'},
            2: {'constant_code': 9, 'message': b'\x00\x0f\x00\x10', 'decrypted_message': 'java/lang/System.out:Ljava/io/PrintStream;'},
            3: {'constant_code': 10, 'message': b'\x00\x11\x00\x12', 'decrypted_message': 'java/io/PrintStream.println:(I)V'},
            4: {'constant_code': 7, 'message': b'\x00\x13', 'decrypted_message': 'HelloWorld'},
            5: {'constant_code': 7, 'message': b'\x00\x14', 'decrypted_message': 'java/lang/Object'},
            6: {'constant_code': 1, 'message': b'\x00\x06', 'decrypted_message': '<init>'},
            7: {'constant_code': 1, 'message': b'\x00\x03', 'decrypted_message': '()V'},
            8: {'constant_code': 1, 'message': b'\x00\x04', 'decrypted_message': 'Code'},
            9: {'constant_code': 1, 'message': b'\x00\x0f', 'decrypted_message': 'LineNumberTable'},
            10: {'constant_code': 1, 'message': b'\x00\x04', 'decrypted_message': 'main'},
            11: {'constant_code': 1, 'message': b'\x00\x16', 'decrypted_message': '([Ljava/lang/String;)V'},
            12: {'constant_code': 1, 'message': b'\x00\n', 'decrypted_message': 'SourceFile'},
            13: {'constant_code': 1, 'message': b'\x00\x0f', 'decrypted_message': 'HelloWorld.java'},
            # How does <init> end up in quotes???
            14: {'constant_code': 12, 'message': b'\x00\x06\x00\x07', 'decrypted_message': '<init>:()V'},
            15: {'constant_code': 7, 'message': b'\x00\x15', 'decrypted_message': 'java/lang/System'},
            16: {'constant_code': 12, 'message': b'\x00\x16\x00\x17', 'decrypted_message': 'out:Ljava/io/PrintStream;'},
            17: {'constant_code': 7, 'message': b'\x00\x18', 'decrypted_message': 'java/io/PrintStream'},
            18: {'constant_code': 12, 'message': b'\x00\x19\x00\x1a', 'decrypted_message': 'println:(I)V'},
            19: {'constant_code': 1, 'message': b'\x00\n', 'decrypted_message': 'HelloWorld'},
            20: {'constant_code': 1, 'message': b'\x00\x10', 'decrypted_message': 'java/lang/Object'},
            21: {'constant_code': 1, 'message': b'\x00\x10', 'decrypted_message': 'java/lang/System'},
            22: {'constant_code': 1, 'message': b'\x00\x03', 'decrypted_message': 'out'},
            23: {'constant_code': 1, 'message': b'\x00\x15', 'decrypted_message': 'Ljava/io/PrintStream;'},
            24: {'constant_code': 1, 'message': b'\x00\x13', 'decrypted_message': 'java/io/PrintStream'},
            25: {'constant_code': 1, 'message': b'\x00\x07', 'decrypted_message': 'println'},
            26: {'constant_code': 1, 'message': b'\x00\x04', 'decrypted_message': '(I)V'}
        }

    def test_get_constant_pool_table(self):
        test = ConstantTable(self.data, self.count)
        for i in self.constant_table_pre:
            self.assertEqual(
                test.constant_table[i]['constant_code'], self.constant_table_pre[i]['constant_code'])
            self.assertEqual(
                test.constant_table[i]['message'], self.constant_table_pre[i]['message'])

    def test_get_constant_messages(self):
        test = ConstantTable(self.data, self.count)
        for i in self.constant_table_pre:
            self.assertEqual(
                self.constant_table_pre[i]['decrypted_message'], test.constant_table[i]['decrypted_message'])
