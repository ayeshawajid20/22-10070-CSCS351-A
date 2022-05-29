import unittest
import cal

class TestCal(unittest.TestCase):

    def test_add(self):
        result= cal.add(10,5)
        self.assertEqual(result,15)
        self.assertEqual(cal.add(-1,1),0)
        self.assertEqual(cal.add(-1,-1),-2)


              
    def test_subtract(self):
        self.assertEqual(cal.subtract(-1,1),-2)
        self.assertNotEqual(cal.subtract(-1,-1),2)

    def test_multiply(self):
        self.assertEqual(cal.multiply(-1,1),-1)
        self.assertIs(cal.multiply(-1,-1),1)

    def test_divide(self):
        self.assertEqual(cal.divide(-1,1),-1)
        self.assertIsNotNone(cal.divide(-1,-1),1)
        
        
        with self.assertRaises(ValueError):
            cal.divide(10,2)

    def test_boolcheck(self):
        self.assertTrue(cal.boolcheck(1,1))
        
           


     

    


if __name__ == '__main__':
    unittest.main()

