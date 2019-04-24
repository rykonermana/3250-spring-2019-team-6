"""Unittest to be used with ClassFile.py"""
import unittest
from unittest.mock import mock_open, patch
from unittest.mock import MagicMock
from ..ClassFile import OpCodes

NONE, T_INT, T_LONG, T_FLOAT, T_DOUBLE = 0, 1, 2 ,3, 4

class TestOpCodes(unittest.TestCase):
    """Unittest for opcodes"""

    # def test_not_implemented(self):
    #   self.assertEqual(OpCodes().interpret(0), 'not implemented')
    #   with self.assertRaises(KeyError):
    #   OpCodes().interpret(1)

    def test_iadd_simple(self):
<<<<<<< HEAD
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(2)
        op_code.add()
        self.assertEqual(op_code.pop_from_stack(), 4)

    def test_int_overflow_positive(self):
        op_code = OpCodes()
        op_code.type = T_INT
        self.assertRaises(ValueError, op_code.push_int_to_stack, 2147483648)

    def test_int_overflow_negative(self):
        op_code = OpCodes()
        op_code.type = T_INT
        self.assertRaises(ValueError, op_code.push_int_to_stack, -2147483649)

    def test_int_max_positive(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.push_int_to_stack(2147483647)
        self.assertEqual(op_code.stack.pop(), 2147483647)

    def test_int_min_negative(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.push_int_to_stack(-2147483648)
        self.assertEqual(op_code.stack.pop(), -2147483648)

    def test_iand_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.stack.append(3)
        op_code.opcode_and()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_iconst_m1_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_m1()
        self.assertEqual(op_code.stack.pop(), -1)

    def test_iconst_0_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_0()
        self.assertEqual(op_code.stack.pop(), 0)

    def test_iconst_1_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_1()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_iconst_2_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_2()
        self.assertEqual(op_code.stack.pop(), 2)

    def test_iconst_3_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_3()
        self.assertEqual(op_code.stack.pop(), 3)

    def test_iconst_4_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_4()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_iconst_5_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.const_5()
        self.assertEqual(op_code.stack.pop(), 5)

    def test_idiv_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(4)
        op_code.div()
        self.assertEqual(op_code.stack.pop(), 2)

    def test_imul_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(4)
        op_code.mul()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_ineg_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.neg()
        self.assertEqual(op_code.stack.pop(), -5)

    def test_ior_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(6)
        op_code.stack.append(2)
        op_code.opcode_or()
        self.assertEqual(op_code.stack.pop(), 6)

    def test_irem_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(7)
        op_code.rem()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_ishl_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shl()
        self.assertEqual(op_code.stack.pop(), 64)

    def test_ishr_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shr()
        self.assertEqual(op_code.stack.pop(), 1)

    def test_isub_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.stack.append(6)
        op_code.sub()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_iushr_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(3)
        op_code.stack.append(8)
        op_code.shr()

    def test_ixor_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(7)
        op_code.stack.append(3)
        op_code.xor()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_invokeVirtual(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(7)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(I)V"), 7)
        op_code.stack.append(1)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'true')
        op_code.stack.append(0)
        self.assertEqual(op_code.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'false')
        op_code.stack.append("HelloWorld")
        self.assertEqual(op_code.invoke_virtual("java/io/PrintStream.println:"
                                               "(Ljava/lang/String;)V"), 'HelloWorld')
        self.assertRaises(NotImplementedError, op_code.invoke_virtual, "java/util/Stack.push:")

    def test_i2b_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-128)
        op_code.convert_byte()
        self.assertEqual(op_code.stack.pop(), b'\x80')

    def test_i2b_simpletest(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(127)
        op_code.convert_byte()
        self.assertEqual(op_code.stack.pop(), b'\x7f')

    def test_i2b_showerror(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(128)
        self.assertRaises(OverflowError, op_code.convert_byte)

    def test_showError(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-129)
        self.assertRaises(OverflowError, op_code.convert_byte)

    def test_i2c_simpletest(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(0)
        print('char?',op_code.stack)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x00')

    def test_i2c_simpletest2(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(127)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x7f')

    def test_i2c_simpletest3(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(65)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), 'A')

    def test_i2c_simpletest4(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-128)
        self.assertRaises(ValueError, op_code.convert_char)

    def test_i2c_simple5(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(128)
        op_code.convert_char()
        self.assertEqual(op_code.stack.pop(), '\x80')

    def test_i2d_simpletest(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2**20-1)
        op_code.convert_float()
        self.assertAlmostEquals(op_code.stack.pop(), 2**20-1)

    def test_i2d_simpletest2(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2**20)
        op_code.convert_float()
        self.assertAlmostEquals(op_code.stack.pop(), -2**20)

    def test_i2f_simpletest(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2**10-1)
        op_code.convert_float()
        self.assertAlmostEquals(op_code.stack.pop(), 2**10-1)

    def test_i2f_simpletest2(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2**10)
        op_code.convert_float()
        self.assertAlmostEquals(op_code.stack.pop(), -2**10)

    def test_i2s_valueTooLarge(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2**16)
        self.assertRaises(ValueError, op_code.convert_short)

    def test_i2s_value_too_small(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2**16-1)
        self.assertRaises(ValueError, op_code.convert_short)

    def test_i2l_valueTooLarge(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2**64)
        self.assertRaises(ValueError, op_code.convert_long)

    def test_i2l_value_too_small(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(-2**64-1)
        self.assertRaises(ValueError, op_code.convert_long)

    def test_iload1_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(1, 8)
        op_code.load_1()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_iload0_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(0, 8)
        op_code.load_0()
        self.assertEqual(op_code.stack.pop(), 8)

    def test_iload2_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(2, 6)
        op_code.load_2()
        self.assertEqual(op_code.stack.pop(), 6)

    def test_iload3_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.localvar.insert(3, 4)
        op_code.load_3()
        self.assertEqual(op_code.stack.pop(), 4)

    def test_istore0_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.store_0()
        self.assertEqual(op_code.localvar[0], 5)

    def test_istore1_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(5)
        op_code.store_1()
        self.assertEqual(op_code.localvar[1], 5)

    def test_istore2_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(4)
        op_code.store_2()
        self.assertEqual(op_code.localvar[2], 4)

    def test_istore3_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        op_code.stack.append(2)
        op_code.store_3()
        self.assertEqual(op_code.localvar[3], 2)

    def test_strscanner_simple(self):
        op_code = OpCodes()
        with unittest.mock.patch('builtins.input', return_value="Testing"):
            self.assertEqual(op_code.invoke_virtual(
                "java/util/Scanner.nextString:()Ljava.lang/String"), "Testing")

    def test_intscanner_simple(self):
        op_code = OpCodes()
        op_code.type = T_INT
        with unittest.mock.patch('builtins.input', return_value=2):
            assert op_code.invoke_virtual(
                "java/util/Scanner.nextInt:()I") == 2

    def test_floatscanner_simple(self):
        op_code = OpCodes()
        op_code.type = T_FLOAT
        with unittest.mock.patch('builtins.input', return_value = 1.0):
            assert op_code.invoke_virtual("java/util/Scanner.nextDouble:()D") == 1.0

    def test_lshl(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(),10)

    def test_lshl_neg(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(-1)
        op_code.push_long_to_stack(5)
        self.assertRaises(ValueError, op_code.shl)

    def test_lshl_zeros(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(0)
        op_code.push_long_to_stack(5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), 5)

    def test_lshl_max(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(2**62-1)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(),2**63-2)

    def test_lshl_min(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-(2 ** 62)+1)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 63-2) )

    def test_lshl_longNeg(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-5)
        op_code.shl()
        self.assertEqual(op_code.pop_long_from_stack(),-10)

    def test_lshr(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(),1)

    def test_lshr_neg(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(-1)
        op_code.push_long_to_stack(3)
        self.assertRaises(ValueError, op_code.shr)

    def test_lshr_zeros(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(0)
        op_code.push_long_to_stack(3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), 3)

    def test_lshr_max(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(2**63-1)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(),2**62-1)

    def test_lshr_min(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-(2 ** 63))
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(), -(2 ** 62) )

    def test_push_pop_long(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-(2 ** 63))
        self.assertEqual(op_code.pop_long_from_stack(), -(2**63))

    def test_lshr_longNeg(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.stack.append(1)
        op_code.push_long_to_stack(-3)
        op_code.shr()
        self.assertEqual(op_code.pop_long_from_stack(),-2)

    def test_ladd(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.push_long_to_stack(1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_ladd_negs(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-1)
        op_code.push_long_to_stack(-1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), -2)

    def test_ladd_maximum(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2**63 - 2)
        op_code.push_long_to_stack(1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), (2**63-1))

    def test_ladd_minimum(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-(2**63-2))
        op_code.push_long_to_stack(-1)
        op_code.add()
        self.assertEqual(op_code.pop_long_from_stack(), -(2**63) +1)

    def test_land(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(3)
        op_code.push_long_to_stack(2)
        op_code.opcode_and()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lconst_m1(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_m1()
        self.assertEqual(op_code.pop_long_from_stack(), -1)

    def test_lconst_0(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_0()
        self.assertEqual(op_code.pop_long_from_stack(), 0)

    def test_lconst_1(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_1()
        self.assertEqual(op_code.pop_long_from_stack(), 1)

    def test_lconst_2(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_2()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lconst_3(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_3()
        self.assertEqual(op_code.pop_long_from_stack(), 3)

    def test_lconst_4(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_4()
        self.assertEqual(op_code.pop_long_from_stack(), 4)

    def test_lconst_5(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.const_5()
        self.assertEqual(op_code.pop_long_from_stack(), 5)

    def test_ldiv_0(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(0)
        op_code.push_long_to_stack(4)
        self.assertRaises(ZeroDivisionError, op_code.div)

    def test_ldiv(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2)
        op_code.push_long_to_stack(4)
        op_code.div()
        self.assertEqual(op_code.pop_long_from_stack(), 2)

    def test_lmul(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(2)
        op_code.push_long_to_stack(4)
        op_code.mul()
        self.assertEqual(op_code.pop_long_from_stack(), 8)

    def test_lneg_NtoP(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(-1)
        op_code.neg()
        self.assertEqual(op_code.pop_long_from_stack(), 1)

    def test_lneg_PtoN(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.neg()
        self.assertEqual(op_code.pop_long_from_stack(), -1)

    def test_lor(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(1)
        op_code.push_long_to_stack(8)
        op_code.opcode_or()
        self.assertEqual(op_code.pop_long_from_stack(), 9)

    def test_lrem(self):
        op_code = OpCodes()
        op_code.type = T_LONG
        op_code.push_long_to_stack(5)
        op_code.push_long_to_stack(12)
        op_code.rem()
        self.assertEqual(op_code.pop_long_from_stack(), 2)
=======
        """Tests iadd method"""
        testiadd = OpCodes()
        testiadd.stack.append(2)
        testiadd.stack.append(2)
        testiadd.iadd()
        self.assertEqual(testiadd.stack.pop(), 4)

    def test_int_overflow_positive(self):
        """Tests for possible integer overflow"""
        testiadd = OpCodes()
        self.assertRaises(ValueError, testiadd.push_int_to_stack, 2147483648)

    def test_int_overflow_negative(self):
        """Tests for possible negative integer overflow"""
        testiadd = OpCodes()
        self.assertRaises(ValueError, testiadd.push_int_to_stack, -2147483649)

    def test_int_max_positive(self):
        """Tests that the possible max integer in java is allowed"""
        testop = OpCodes()
        testop.push_int_to_stack(2147483647)
        self.assertEqual(testop.stack.pop(), 2147483647)

    def test_int_min_negative(self):
        """Tests that the possible minimum integer in java is allowed"""
        testop = OpCodes()
        testop.push_int_to_stack(-2147483648)
        self.assertEqual(testop.stack.pop(), -2147483648)

    def test_iand_simple(self):
        """As method name implies"""
        testiand = OpCodes()
        testiand.stack.append(5)
        testiand.stack.append(3)
        testiand.iand()
        self.assertEqual(testiand.stack.pop(), 1)

    def test_iconst_m1_simple(self):
        """As method name implies"""
        testiconst_m1 = OpCodes()
        testiconst_m1.iconst_m1()
        self.assertEqual(testiconst_m1.stack.pop(), -1)

    def test_iconst_0_simple(self):
        """As method name implies"""
        testiconst_0 = OpCodes()
        testiconst_0.iconst_0()
        self.assertEqual(testiconst_0.stack.pop(), 0)

    def test_iconst_1_simple(self):
        """As method name implies"""
        testiconst_1 = OpCodes()
        testiconst_1.iconst_1()
        self.assertEqual(testiconst_1.stack.pop(), 1)

    def test_iconst_2_simple(self):
        """As method name implies"""
        testiconst_2 = OpCodes()
        testiconst_2.iconst_2()
        self.assertEqual(testiconst_2.stack.pop(), 2)

    def test_iconst_3_simple(self):
        """As method name implies"""
        testiconst_3 = OpCodes()
        testiconst_3.iconst_3()
        self.assertEqual(testiconst_3.stack.pop(), 3)

    def test_iconst_4_simple(self):
        """As method name implies"""
        testiconst_4 = OpCodes()
        testiconst_4.iconst_4()
        self.assertEqual(testiconst_4.stack.pop(), 4)

    def test_iconst_5_simple(self):
        """As method name implies"""
        testiconst_5 = OpCodes()
        testiconst_5.iconst_5()
        self.assertEqual(testiconst_5.stack.pop(), 5)

    def test_idiv_simple(self):
        """As method name implies"""
        test1 = OpCodes()
        test1.stack.append(2)
        test1.stack.append(4)
        test1.idiv()
        self.assertEqual(test1.stack.pop(), 2)

    def test_imul_simple(self):
        """As method name implies"""
        test2 = OpCodes()
        test2.stack.append(2)
        test2.stack.append(4)
        test2.imul()
        self.assertEqual(test2.stack.pop(), 8)

    def test_ineg_simple(self):
        """As method name implies"""
        test3 = OpCodes()
        test3.stack.append(5)
        test3.ineg()
        self.assertEqual(test3.stack.pop(), -5)

    def test_ior_simple(self):
        """As method name implies"""
        test4 = OpCodes()
        test4.stack.append(6)
        test4.stack.append(2)
        test4.ior()
        self.assertEqual(test4.stack.pop(), 6)

    def test_irem_simple(self):
        """As method name implies"""
        test5 = OpCodes()
        test5.stack.append(3)
        test5.stack.append(7)
        test5.irem()
        self.assertEqual(test5.stack.pop(), 1)

    def test_ishl_simple(self):
        """As method name implies"""
        test6 = OpCodes()
        test6.stack.append(3)
        test6.stack.append(8)
        test6.ishl()
        self.assertEqual(test6.stack.pop(), 64)

    def test_ishr_simple(self):
        """As method name implies"""
        test7 = OpCodes()
        test7.stack.append(3)
        test7.stack.append(8)
        test7.ishr()
        self.assertEqual(test7.stack.pop(), 1)

    def test_isub_simple(self):
        """As method name implies"""
        test8 = OpCodes()
        test8.stack.append(2)
        test8.stack.append(6)
        test8.isub()
        self.assertEqual(test8.stack.pop(), 4)

    # I wasn't sure about iushr so i commented it out for now - Christian
    # def test_iushr_simple(self):
    # test9 = OpCodes()
    # test9.stack.append(3)
    # test9.stack.append(8)
    # test9.ishr()

    def test_ixor_simple(self):
        """As method name implies"""
        test10 = OpCodes()
        test10.stack.append(7)
        test10.stack.append(3)
        test10.ixor()
        self.assertEqual(test10.stack.pop(), 4)

    def test_invokeVirtual(self):
        """Tests invokeVirtual method java/io/PrintStream with various inputs"""
        test11 = OpCodes()
        test11.stack.append(7)
        self.assertEqual(test11.invoke_virtual(
            "java/io/PrintStream.println:(I)V"), 7)
        # test11.stack.append(4.321)
        # self.assertEqual(test11.invokeVirtual("Method java/io/PrintStream.println:(D)V"), 4.321)
        test11.stack.append(1)
        self.assertEqual(test11.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'true')
        test11.stack.append(0)
        self.assertEqual(test11.invoke_virtual(
            "java/io/PrintStream.println:(Z)V"), 'false')
        test11.stack.append("HelloWorld")
        self.assertEqual(test11.invoke_virtual("java/io/PrintStream.println:"
                                               "(Ljava/lang/String;)V"), 'HelloWorld')
        self.assertEqual(test11.invoke_virtual("java/util/Stack.push:"
                                               "(Ljava/lang/Object;)Ljava/lang/Object"),
                         'not implemented')

    def test_i2b_simple(self):
        """As method name implies"""
        test = OpCodes()
        test.stack.append(-128)
        test.i2b()
        self.assertEqual(test.stack.pop(), b'\x80')

    def test_i2b_simpletest(self):
        """As method name implies"""
        test = OpCodes()
        test.stack.append(127)
        test.i2b()
        self.assertEqual(test.stack.pop(), b'\x7f')

    def test_i2b_showerror(self):
        """Tests that OverFlow error is thrown when the value is too large to be a byte"""
        test = OpCodes()
        test.stack.append(128)
        self.assertRaises(OverflowError, test.i2b)

    def test_show_error(self):
        """Tests that OverFlow error is thrown when the value is too small to be a byte"""
        test = OpCodes()
        test.stack.append(-129)
        self.assertRaises(OverflowError, test.i2b)

    def test_i2c_simpletest(self):
        """Tests that the number given returns as the correct char type"""
        test = OpCodes()
        test.stack.append(0)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x00')

    def test_i2c_simpletest2(self):
        """Tests that the number given returns as the correct char type"""
        test = OpCodes()
        test.stack.append(127)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x7f')

    def test_i2c_simpletest3(self):
        """Tests that the number given returns as the correct char type"""
        test = OpCodes()
        test.stack.append(65)
        test.i2c()
        self.assertEqual(test.stack.pop(), 'A')

    def test_i2c_simpletest4(self):
        """Tests that a ValueError exception is thrown when an unacceptable
        value is inputed"""
        test = OpCodes()
        test.stack.append(-128)
        # test.i2c()
        self.assertRaises(ValueError, test.i2c)

    def test_i2c_simple5(self):
        """Tests that the number given returns as the correct char type"""
        test = OpCodes()
        test.stack.append(128)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x80')

    def test_i2d_simpletest(self):
        """Tests that a double integer in java is returned as a float
        in python because there is no double in python"""
        test = OpCodes()
        test.stack.append(2 ** 63 - 1)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))

    def test_i2d_simpletest2(self):
        """Tests that a double value in java is returned as a float
        in python because there is no double in python"""
        test = OpCodes()
        test.stack.append(-2 ** 63)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))

    def test_i2f_simpletest(self):
        """Tests that an integer is returned as a float"""
        test = OpCodes()
        test.stack.append(2 ** 31 - 1)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))

    def test_i2f_simpletest2(self):
        """Tests that an integer is returned as a float"""
        test = OpCodes()
        test.stack.append(-2 ** 31)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))

    def test_i2s_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is to large
         to a short type"""
        test = OpCodes()
        test.stack.append(2 ** 16)
        self.assertRaises(ValueError, test.i2s(test.stack.pop()))

    def test_i2s_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is to large
         to a short type"""
        test = OpCodes()
        test.stack.append(-2 ** 16 - 1)
        self.assertRaises(ValueError, test.i2s)

    def test_i2l_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is to large
         to a long type"""
        test = OpCodes()
        test.stack.append(2 ** 64)
        self.assertRaises(ValueError, test.i2l(test.stack.pop()))

    def test_i2l_value_too_large(self):
        """Tests that a ValueError is thrown when trying to cast an integer that is to large
         to a long type"""
        test = OpCodes()
        test.stack.append(-2 ** 64 - 1)
        self.assertRaises(ValueError, test.i2l)

    def test_iload1_simple(self):
        """As method name implies"""
        testiload1 = OpCodes()
        testiload1.localvar.insert(1, 8)
        testiload1.iload_1()
        self.assertEqual(testiload1.stack.pop(), 8)

    def test_iload0_simple(self):
        """As method name implies"""
        testiload0 = OpCodes()
        testiload0.localvar.insert(0, 8)
        testiload0.iload_0()
        self.assertEqual(testiload0.stack.pop(), 8)

    def test_iload2_simple(self):
        """As method name implies"""
        testiload2 = OpCodes()
        testiload2.localvar.insert(2, 6)
        testiload2.iload_2()
        self.assertEqual(testiload2.stack.pop(), 6)

    def test_iload3_simple(self):
        """As method name implies"""
        testiload3 = OpCodes()
        testiload3.localvar.insert(3, 4)
        testiload3.iload_3()
        self.assertEqual(testiload3.stack.pop(), 4)

    def test_istore0_simple(self):
        """As method name implies"""
        testistore0 = OpCodes()
        testistore0.stack.append(5)
        testistore0.istore_0()
        self.assertEqual(testistore0.localvar[0], 5)

    def test_istore1_simple(self):
        """As method name implies"""
        testistore1 = OpCodes()
        testistore1.stack.append(5)
        testistore1.istore_1()
        self.assertEqual(testistore1.localvar[1], 5)

    def test_istore2_simple(self):
        """As method name implies"""
        testistore2 = OpCodes()
        testistore2.stack.append(4)
        testistore2.istore_2()
        self.assertEqual(testistore2.localvar[2], 4)

    def test_istore3_simple(self):
        """As method name implies"""
        testistore3 = OpCodes()
        testistore3.stack.append(2)
        testistore3.istore_3()
        self.assertEqual(testistore3.localvar[3], 2)

    def test_strscanner_simple(self):
        """As method name implies"""
        teststrscanner = OpCodes()
        with unittest.mock.patch('builtins.input', return_value="Testing"):
            self.assertEqual(teststrscanner.invoke_virtual(
                "java/util/Scanner.nextString:()Ljava.lang/String"), "Testing")

    def test_intscanner_simple(self):
        """As method name implies"""
        testintscanner = OpCodes()
        with unittest.mock.patch('builtins.input', return_value=2):
            assert testintscanner.invoke_virtual(
                "java/util/Scanner.nextInt:()I") == 2

    def test_floatscanner_simple(self):
        """As method name implies"""
        testfloatscanner = OpCodes()
        with unittest.mock.patch('builtins.input', return_value=1.0):
            assert testfloatscanner.invoke_virtual(
                "java/util/Scanner.nextDouble:()D") == 1.0
>>>>>>> fb647eb88b6cdfb6c8f1b0f60bc61b677fcac99c
