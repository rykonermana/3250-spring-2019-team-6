import unittest
from unittest.mock import mock_open, patch
from jvpm.ClassFile import OpCodes


class TestOpCodes(unittest.TestCase):
    def test_not_implemented(self):
        self.assertEqual(OpCodes().interpret(0), 'not implemented')
        with self.assertRaises(KeyError):
            OpCodes().interpret(1)
    def test_iadd_simple(self):
	    testiadd = OpCodes()
	    testiadd.stack.append(2)
	    testiadd.stack.append(2)
	    testiadd.iadd()
	    self.assertEqual(testiadd.stack.pop(), 4)
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