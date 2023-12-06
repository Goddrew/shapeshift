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
        # Same between screen and input image 
        self.assertEqual(helper.cost(screen, y), 0)
        # Different between screen and input image
        y = np.random.rand(500, 500, 3)
        self.assertNotEqual(helper.cost(screen, y), 0)
        # MSE between 1s and 0s vector should be 1
        y = np.ones((500, 500, 3))
        self.assertEqual(helper.cost(screen, y), 1)

    def test_generate_shapes(self): 
        """Test if correctly generating shapes to draw"""
        borderBox = (500, 500)
        # Line 
        param = {"shape_type": "line", "count": 100, "colorOn": False, "length": 100}
        shapes = helper.generate_shapes(borderBox, param=param)
        self.assertEqual(len(shapes), 100)
        for s in shapes: 
            # Check if each vertex of the line is within borderBox
            self.assertEqual(helper.inBorder(borderBox, s[0]), True)
            self.assertEqual(helper.inBorder(borderBox, s[1]), True)

        # Circle 
        param = {"shape_type": "circle", "count": 100, "colorOn": False, "radius": 8}
        shapes = helper.generate_shapes(borderBox, param=param)
        self.assertEqual(len(shapes), 100)
        for s in shapes: 
            # Check if each circle within borderBox
            self.assertEqual(helper.inBorder(borderBox, (s[0][1]+s[1], s[0][1])), True) # Center + radius 
            self.assertEqual(helper.inBorder(borderBox, (s[0][1]-s[1], s[0][1])), True)  
            self.assertEqual(helper.inBorder(borderBox, (s[0][1], s[0][1]+s[1])), True)  
            self.assertEqual(helper.inBorder(borderBox, (s[0][1], s[0][1]-s[1])), True) 



    def test_neighbors(self): 
        """Test if generating neighbors state correctly"""
        borderBox = (500, 500)
        # Line 
        param = {"shape_type": "line", "count": 100, "colorOn": False, "length": 100}
        shapes = helper.generate_shapes(borderBox, param)
        neighbors = helper.neighbors(borderBox, shapes, param)
        self.assertEqual(len(shapes), len(neighbors))
        # Check current state and neighbor state are not actually the same
        self.assertNotEqual(shapes, neighbors)
        for s in neighbors: 
            self.assertEqual(helper.inBorder(borderBox, s[0]), True)
            self.assertEqual(helper.inBorder(borderBox, s[1]), True)
        
        # Circle 
        param = {"shape_type": "circle", "count": 100, "colorOn": False, "radius": 8}
        shapes = helper.generate_shapes(borderBox, param=param)
        neighbors = helper.neighbors(borderBox, shapes, param)
        self.assertEqual(len(shapes), len(neighbors))
        self.assertNotEqual(shapes, neighbors)
        for s in neighbors: 
            self.assertEqual(helper.inBorder(borderBox, (s[0][1]+s[1], s[0][1])), True)
            self.assertEqual(helper.inBorder(borderBox, (s[0][1]-s[1], s[0][1])), True)  
            self.assertEqual(helper.inBorder(borderBox, (s[0][1], s[0][1]+s[1])), True)  
            self.assertEqual(helper.inBorder(borderBox, (s[0][1], s[0][1]-s[1])), True)     

if __name__ == "__main__": 
    unittest.main()