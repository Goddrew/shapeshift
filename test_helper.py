import unittest 
import helper 

class TestHelper(unittest.TestCase): 
    def test_inBorder(self): 
        borderBox = (500, 500)
        self.assertEqual(helper.inBorder(borderBox, (-250, -250)), False)
        self.assertEqual(helper.inBorder(borderBox, (-250, 250)), False)
        self.assertEqual(helper.inBorder(borderBox, (250, -250)), False)
        self.assertEqual(helper.inBorder(borderBox, (0, 0)), True)
        self.assertEqual(helper.inBorder(borderBox, (250, 250)), True)
        self.assertEqual(helper.inBorder(borderBox, borderBox), True)

if __name__ == "__main__": 
    unittest.main()