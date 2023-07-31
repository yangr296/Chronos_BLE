from BLEMessage import BLEMessage
import unittest

class TestStringMethods(unittest.TestCase):

    def test_P1(self):
        message = BLEMessage(300, 100, 100)
        expected = 1
        actual = ord(message.b1)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(5000, 100, 100)
        expected = 19
        actual = ord(message.b1)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(10, 100, 100)
        expected = 0
        actual = ord(message.b1)
        self.assertEqual(expected, actual)
        
        with self.assertRaises(Exception):
            message = BLEMessage(8, 100, 100)
        
        with self.assertRaises(Exception):
            message = BLEMessage(5001, 100, 100)

        message = BLEMessage(300, 100, 100)
        expected = 44
        actual = ord(message.b2)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(5000, 100, 100)
        expected = 136
        actual = ord(message.b2)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(10, 100, 100)
        expected = 10
        actual = ord(message.b2)
        self.assertEqual(expected, actual)

    def test_p2(self):
        message = BLEMessage(300, 25, 100)
        expected = 12
        actual = ord(message.b3)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(5000, 500, 100)
        expected = 250
        actual = ord(message.b3)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(10, 200, 100)
        expected = 100
        actual = ord(message.b3)
        self.assertEqual(expected, actual)
    
    def test_p3(self):
        message = BLEMessage(300, 25, 20)
        expected = 20
        actual = ord(message.b4)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(5000, 500, 200)
        expected = 200
        actual = ord(message.b4)
        self.assertEqual(expected, actual)
        
        message = BLEMessage(10, 200, 100)
        expected = 100
        actual = ord(message.b4)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()

