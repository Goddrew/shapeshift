import unittest 
import helper
import numpy as np 
import pygame

class TestHelper(unittest.TestCase): 
    def test_inBorder(self): 
        """Test if point is within the given border"""
        borderBox = (500, 500) # Screen size 
        self.assertEqual(helper.inBorder(borderBox, (-250, -250)), False)
        self.assertEqual(helper.inBorder(borderBox, (-250, 250)), False)
        self.assertEqual(helper.inBorder(borderBox, (250, -250)), False)
        self.assertEqual(helper.inBorder(borderBox, (0, 0)), True)
        self.assertEqual(helper.inBorder(borderBox, (250, 250)), True)
        self.assertEqual(helper.inBorder(borderBox, borderBox), True)

    def test_cost(self): 
        """Test if cost between screen and real image make sense"""
        screen = pygame.Surface((500, 500))
        y = np.zeros((500, 500, 3))
        # Exactly the same so cost should be 0 
        self.assertEqual(helper.cost(screen, y), 0)
        # Shouldn't be the same so cost should be non 0
        y = np.random.rand(500, 500, 3)
        self.assertNotEqual(helper.cost(screen, y), 0)
        # Make sure MSE calcuation is correct (MSE between 1s and 0s vector should be 1)
        y = np.ones((500, 500, 3))
        self.assertEqual(helper.cost(screen, y), 1)

    def test_generate_shapes(self): 
        """Test if correctly generating shapes to draw"""
        borderBox = (500, 500)
        shapes = helper.generate_shapes(borderBox, shape_type="line", count=100, color=False)
        self.assertEqual(len(shapes), 100)
        for s in shapes: 
            # Check if each vertex of the line is within borderBox
            self.assertEqual(helper.inBorder(borderBox, s[0]), True)
            self.assertEqual(helper.inBorder(borderBox, s[1]), True)

    def test_neighbors(self): 
        """Test if generating neighbors state correctly"""
        borderBox = (500, 500)
        shapes = helper.generate_shapes(borderBox, shape_type="line", count=100, color=False)
        neighbors = helper.neighbors(borderBox, shapes, shape_type="line", color=False)
        self.assertEqual(len(shapes), len(neighbors))
        self.assertNotEqual(shapes, neighbors)
        for s in neighbors: 
            self.assertEqual(helper.inBorder(borderBox, s[0]), True)
            self.assertEqual(helper.inBorder(borderBox, s[1]), True)
            
if __name__ == "__main__": 
    unittest.main()