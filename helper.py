import numpy as np 
import pygame 
import math 
import copy

def neighbors(border_box, shapes, shape_type, color): 
    """Obtain current state space neighbors

    Parameters
    ----------
    border_box: tuple 
        (width, height) of screen to bound the shapes within 
    shapes: list 
        list of parameters for required shape 
    shape: str 
        shape type 
    color: bool 
        color on or off
    
    Returns
    -------
    shapes: list 
        next state space of list of parameters for required shape

    """
    m = len(shapes)
    shapes = copy.deepcopy(shapes)
    # ind = np.random.randint(0, m)
    ind = np.random.permutation(m)[:10]
    if shape_type == "line": 
        # ([x1, y1], [x2, y2], pygame.Color)
        for i in ind:
            vertex = np.random.randint(0, 2)
            color_channel = np.random.randint(0, 3)
            angle = np.random.randint(0, 360)
            x = shapes[i][int(not vertex)][0] + math.cos(math.radians(angle)) * 100 
            y = shapes[i][int(not vertex)][1] + math.sin(math.radians(angle)) * 100
            # Keep generating if outside of border_box
            while not inBorder(border_box, (x, y)): 
                angle = np.random.randint(0, 360)
                x = shapes[i][int(not vertex)][0] + math.cos(math.radians(angle)) * 100 
                y = shapes[i][int(not vertex)][1] + math.sin(math.radians(angle)) * 100
            shapes[i][vertex][0] = x
            shapes[i][vertex][1] = y
            if color:     
                if color_channel == 0:
                    shapes[i][2].r = np.random.randint(0, 256)
                elif color_channel == 1:
                    shapes[i][2].g = np.random.randint(0, 256)
                else:
                    shapes[i][2].b = np.random.randint(0, 256)
    return shapes 

def inBorder(border_box, pos): 
    """Return true if pos is within border_box

    Parameters 
    ---------- 
    border_box: tuple 
        (width, height) of screen to bound the shapes within 
    pos: tuple
        (x, y)

    Returns
    -------
    Whether the position remains in the given border_box 
    """
    return (0 <= pos[0] and pos[0] <= border_box[0]) and (0 <= pos[1] and pos[1] <= border_box[1])

def cost(screen, y): 
    """Return the scalar cost between prediction (yhat) and true image (y)
    """
    yhat = pygame.surfarray.array3d(screen)
    yhat = yhat.swapaxes(0, 1)
    yhat = yhat.flatten() 
    y = y.flatten() 
    m = len(yhat)
    cost = np.sum(np.square(y - yhat), keepdims=False) 
    cost = 1/m * cost 
    return cost 

def generate_shapes(border_box, shape_type="line", count=100, color=False): 
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
    if shape_type == "line": 
        # ((start pos), (end pos))
        line_length = 100 # Default line length 
        line_width = 3  # Default line width 

        for i in range(count): 
            # Random orientation 
            x1, y1 = np.random.randint(0, border_box[0]), np.random.randint(0, border_box[1])
            angle = np.random.randint(0, 360)
            x2 = x1 + math.cos(math.radians(angle)) * line_length
            y2 = y1 + math.sin(math.radians(angle)) * line_length
            # Keep generating if outside of border_box
            while not inBorder(border_box, (x2, y2)): 
                angle = np.random.randint(0, 360)
                x2 = x1 + math.cos(math.radians(angle)) * line_length
                y2 = y1 + math.sin(math.radians(angle)) * line_length
            if color: 
                r, g, b = np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)
                shapes.append(([x1, y1], [x2, y2], pygame.Color(r, g, b)))
            else: 
                shapes.append(([x1, y1], [x2, y2], pygame.Color("black")))



    return shapes  
