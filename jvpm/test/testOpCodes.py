import unittest
from unittest.mock import mock_open, patch
from unittest.mock import MagicMock
from jvpm.ClassFile import OpCodes


class TestOpCodes(unittest.TestCase):
    #def test_not_implemented(self):
    #    self.assertEqual(OpCodes().interpret(0), 'not implemented')
    #    with self.assertRaises(KeyError):
    #        OpCodes().interpret(1)
    def test_iadd_simple(self):
	      testiadd = OpCodes()
	      testiadd.stack.append(2)
	      testiadd.stack.append(2)
	      testiadd.iadd()
	      self.assertEqual(testiadd.stack.pop(), 4)
    def test_int_overflow_positive(self):
        testiadd = OpCodes()
        self.assertRaises(ValueError,testiadd.push_int_to_stack, 2147483648)
    def test_int_overflow_negative(self):
        testiadd = OpCodes()
        self.assertRaises(ValueError,testiadd.push_int_to_stack, -2147483649)
    def test_int_max_positive(self):
        testop = OpCodes()
        testop.push_int_to_stack(2147483647)
        self.assertEqual(testop.stack.pop(),2147483647)
    def test_int_min_negative(self):
        testop = OpCodes()
        testop.push_int_to_stack(-2147483648)
        self.assertEqual(testop.stack.pop(),-2147483648)
    def test_iand_simple(self):
        testiand = OpCodes()
        testiand.stack.append(5)
        testiand.stack.append(3)
        testiand.iand()
        self.assertEqual(testiand.stack.pop(), 1)
    def test_iconst_m1_simple(self):
        testiconst_m1 = OpCodes()
        testiconst_m1.iconst_m1()
        self.assertEqual(testiconst_m1.stack.pop(), -1)
    def test_iconst_0_simple(self):
        testiconst_0 = OpCodes()
        testiconst_0.iconst_0()
        self.assertEqual(testiconst_0.stack.pop(), 0)
    def test_iconst_1_simple(self):
        testiconst_1 = OpCodes()
        testiconst_1.iconst_1()
        self.assertEqual(testiconst_1.stack.pop(), 1)
    def test_iconst_2_simple(self):
        testiconst_2 = OpCodes()
        testiconst_2.iconst_2()
        self.assertEqual(testiconst_2.stack.pop(), 2)
    def test_iconst_3_simple(self):
        testiconst_3 = OpCodes()
        testiconst_3.iconst_3()
        self.assertEqual(testiconst_3.stack.pop(), 3)
    def test_iconst_4_simple(self):
        testiconst_4 = OpCodes()
        testiconst_4.iconst_4()
        self.assertEqual(testiconst_4.stack.pop(), 4)
    def test_iconst_5_simple(self):
        testiconst_5 = OpCodes()
        testiconst_5.iconst_5()
        self.assertEqual(testiconst_5.stack.pop(), 5)
    def test_idiv_simple(self):
        test1 = OpCodes()
        test1.stack.append(2)    # Pushes Y onto the stack
        test1.stack.append(4)    # Pushes X onto the stack
        test1.idiv()             # idiv divides the first item on the stack by the second and pushes X/Y onto stack
        self.assertEqual(test1.stack.pop(), 2) #Tests if answer pushed on stack is correct
    def test_imul_simple(self):
        test2 = OpCodes()
        test2.stack.append(2)    # Pushes Y onto the stack
        test2.stack.append(4)    # Pushes X onto stack
        test2.imul()             # Pops first two operands off stack and multiplies them and pushes X*Y
        self.assertEqual(test2.stack.pop(), 8) # Tests for correct X*Y on stack
    def test_ineg_simple(self):
        test3 = OpCodes()
        test3.stack.append(5)    # Pushes X onto the stack
        test3.ineg()             # Negates X
        self.assertEqual(test3.stack.pop(), -5) # Tests for -X pn stack
    def test_ior_simple(self):
        test4 = OpCodes()
        test4.stack.append(6)    # Pushes Y onto the stack
        test4.stack.append(2)    # Pushes X onto the stack
        test4.ior()              # Pops first two operands off stack and does bitwise OR between them
        self.assertEqual(test4.stack.pop(), 6) # Tests for correct X OR Y on stack
    def test_irem_simple(self):
        test5 = OpCodes()
        test5.stack.append(3)    # Pushes Y onto the stack
        test5.stack.append(7)    # Pushes X onto the stack
        test5.irem()             # Pops first two operands off stack and divides them then pushes the remainder to the stack
        self.assertEqual(test5.stack.pop(), 1) # Tests for correct remainder
    def test_ishl_simple(self):
        test6 = OpCodes()
        test6.stack.append(3)    # Pushes Y onto the stack
        test6.stack.append(8)    # Pushes X onto the stack
        test6.ishl()             # Pops first two operands off stack and pushs X*2^Y onto the stack
        self.assertEqual(test6.stack.pop(), 64) # Tests the answer of the shift
    def test_ishr_simple(self):
        test7 = OpCodes()
        test7.stack.append(3)    # Pushes Y onto the stack
        test7.stack.append(8)    # Pushes X onto the stack
        test7.ishr()             # Pops first two operands off stack and pushes X*2^(-Y)
        self.assertEqual(test7.stack.pop(), 1) # Tests the answer of the shift
    def test_isub_simple(self):
        test8 = OpCodes()
        test8.stack.append(2)    # Pushes Y onto the stack
        test8.stack.append(6)    # Pushes X onto the stack
        test8.isub()             # Pops first two operands off stack and pushes X-Y onto the stack
        self.assertEqual(test8.stack.pop(), 4) # Tests for correct answer of subtraction
    #I wasn't sure about iushr so i commented it out for now - Christian
    #def test_iushr_simple(self):
        #test9 = OpCodes()
        #test9.stack.append(3)    # Pushes Y onto the stack
        #test9.stack.append(8)    # Pushes X onto the stack
        #test9.ishr()             # Pops first two operands off stack and pushes X*2^(-Y)
    def test_ixor_simple(self):
	      test10 = OpCodes()
	      test10.stack.append(7)   # Pushes Y onto the stack
	      test10.stack.append(3)   # Pushes X onto the stack
	      test10.ixor()            # Pops first two operands off stack and pushes X XOR Y
	      self.assertEqual(test10.stack.pop(), 4) # Tests for correct answer of XOR
    def test_invokeVirtual(self):
	      test11 = OpCodes()
	      test11.stack.append(7)
	      self.assertEqual(test11.invokeVirtual("java/io/PrintStream.println:(I)V"), 7)
	      #test11.stack.append(4.321)
	      #self.assertEqual(test11.invokeVirtual("Method java/io/PrintStream.println:(D)V"), 4.321)
	      test11.stack.append(1)
	      self.assertEqual(test11.invokeVirtual("java/io/PrintStream.println:(Z)V"), 'true')
	      test11.stack.append(0)
	      self.assertEqual(test11.invokeVirtual("java/io/PrintStream.println:(Z)V"), 'false')
	      test11.stack.append("HelloWorld")
	      self.assertEqual(test11.invokeVirtual("java/io/PrintStream.println:(Ljava/lang/String;)V"), 'HelloWorld')
	      self.assertEqual(test11.invokeVirtual("java/util/Stack.push:(Ljava/lang/Object;)Ljava/lang/Object"), 'not implemented')
    def test_i2b_simple(self):
        test = OpCodes()
        test.stack.append(-128)
        test.i2b()
        self.assertEqual(test.stack.pop(), b'\x80')
    def test_i2b_simpletest(self):
        test = OpCodes()
        test.stack.append(127)
        test.i2b()
        self.assertEqual(test.stack.pop(), b'\x7f')
    def test_i2b_showerror(self):
        test = OpCodes()
        test.stack.append(128)
        self.assertRaises(OverflowError,test.i2b)
    def test_showError(self):
        test = OpCodes()
        test.stack.append(-129)
        self.assertRaises(OverflowError,test.i2b)
    def test_i2c_simpletest(self):
        test = OpCodes()
        test.stack.append(0)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x00')
    def test_i2c_simpletest2(self):
        test = OpCodes()
        test.stack.append(127)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x7f')
    def test_i2c_simpletest3(self):
        test = OpCodes()
        test.stack.append(65)
        test.i2c()
        self.assertEqual(test.stack.pop(), 'A')
    def test_i2c_simpletest4(self):
        test = OpCodes()
        test.stack.append(-128)
        # test.i2c()
        self.assertRaises(ValueError, test.i2c)
    def test_i2c_simple5(self):
        test = OpCodes()
        test.stack.append(128)
        test.i2c()
        self.assertEqual(test.stack.pop(), '\x80')
    def test_i2d_simpletest(self):
        test = OpCodes()
        test.stack.append(2**63-1)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))
    def test_i2d_simpletest2(self):
        test = OpCodes()
        test.stack.append(-2**63)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))
    def test_i2f_simpletest(self):
        test = OpCodes()
        test.stack.append(2**31-1)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))
    def test_i2f_simpletest2(self):
        test = OpCodes()
        test.stack.append(-2**31)
        test.i2f()
        self.assertTrue(isinstance(test.stack.pop(), float))
    def test_i2s_valueTooLarge(self):
        test = OpCodes()
        test.stack.append(2**16)
        self.assertRaises(ValueError, test.i2s(test.stack.pop()))
    def test_i2s_valueTooLarge(self):
        test = OpCodes()
        test.stack.append(-2**16-1)
        self.assertRaises(ValueError, test.i2s)
    def test_i2l_valueTooLarge(self):
        test = OpCodes()
        test.stack.append(2**64)
        self.assertRaises(ValueError, test.i2l(test.stack.pop()))
    def test_i2l_valueTooLarge(self):
        test = OpCodes()
        test.stack.append(-2**64-1)
        self.assertRaises(ValueError, test.i2l)
    def test_iload_simple(self):
        testiload = OpCodes()
        testiload.localvar.insert(5, 3)
        testiload.iload(5)
        self.assertEqual(testiload.stack.pop(), 3)
    def test_iload1_simple(self):
        testiload1 = OpCodes()
        testiload1.localvar.insert(1, 8)
        testiload1.iload_1(1)
        self.assertEqual(testiload1.stack.pop(), 8)
    def test_iload0_simple(self):
        testiload0 = OpCodes()
        testiload0.localvar.insert(0, 8)
        testiload0.iload_0(0)
        self.assertEqual(testiload0.stack.pop(), 8)
    def test_iload2_simple(self):
        testiload2 = OpCodes()
        testiload2.localvar.insert(2, 6)
        testiload2.iload_2(2)
        self.assertEqual(testiload2.stack.pop(), 6)
    def test_iload3_simple(self):
        testiload3 = OpCodes()
        testiload3.localvar.insert(3, 4)
        testiload3.iload_3(3)
        self.assertEqual(testiload3.stack.pop(), 4)
    def test_istore_simple(self):
        testistore = OpCodes()
        testistore.stack.append(1)
        testistore.istore(0)
        self.assertEqual(testistore.localvar[0], 1)
    def test_istore0_simple(self):
        testistore0 = OpCodes()
        testistore0.stack.append(5)
        testistore0.istore_0(0)
        self.assertEqual(testistore0.localvar[0], 5)
    def test_istore1_simple(self):
        testistore1 = OpCodes()
        testistore1.stack.append(5)
        testistore1.istore_1(1)
        self.assertEqual(testistore1.localvar[1], 5)
    def test_istore2_simple(self):
        testistore2 = OpCodes()
        testistore2.stack.append(4)
        testistore2.istore_2(2)
        self.assertEqual(testistore2.localvar[2], 4)
    def test_istore3_simple(self):
        testistore3 = OpCodes()
        testistore3.stack.append(2)
        testistore3.istore_3(3)
        self.assertEqual(testistore3.localvar[3], 2)
