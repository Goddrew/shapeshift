import numpy as np 
import pygame 
import math 
import copy

def neighbors(shapes, shape): 
    """Obtain current state space neighbors

    Parameters
    ----------
    shapes: list 
        list of parameters for each required shape 
    shape: str 
        shape type 

    """
    m = len(shapes)
    copied_shapes = copy.deepcopy(shapes)
    if shape == "line": 
        pass 
    pass 

def cost(yhat, y): 
    """Return the scalar cost between prediction (yhat) and true image (y)
    """
    yhat = yhat.flatten() 
    y = y.flatten() 
    m = len(yhat)
    cost = np.sum(np.square(y - yhat), keepdims=False) 
    cost = 1/m * cost 
    return cost 

def generate_shapes(border_box, shape="line", count=100): 
    """Generate the starting state of shapes  

    Parameters
    ----------
    border_box: tuple 
        (width, height) of screen to bound the shapes within 
    shape: str 
        shape to generate 
    count: int 
        number of shapes to generate
    
    Returns
    -------
    shapes: list 
        list of parameters for each required shape 
    """
    shapes = []
    if shape == "line": 
        # ((start pos), (end pos))
        line_length = 100 # Default line length 
        line_width = 3  # Default line width 

        for i in range(count): 
            # Random orientation 
            x1, y1 = np.random.randint(0, border_box[0]), np.random.randint(0, border_box[1])
            angle = np.random.randint(0, 360)
            x2 = x1 + math.cos(math.radians(angle)) * line_length
            y2 = y1 + math.sin(math.radians(angle)) * line_length
            shapes.append(([x1, y1], [x2, y2]))

    return shapes  

def hill_climb(): 
    pass
