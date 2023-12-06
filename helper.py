import numpy as np 
import pygame 
import math 
import copy
import cv2 as cv

def neighbors(border_box, shapes, param): 
    """Obtain current state space neighbors

    Parameters
    ----------
    border_box: tuple 
        (width, height) of screen to bound the shapes within 
    shapes: list 
        list of shape elements  
    param: dict
        dictionary of parameters 
    
    Returns
    -------
    shapes: list 
        next state space of list of parameters for required shape
    """
    m = len(shapes)
    shapes = copy.deepcopy(shapes)
    ind = np.random.permutation(m)[:1]
    shape_type = param["shape_type"]
    colorOn = param["colorOn"]

    if shape_type == "line": 
        # ([x1, y1], [x2, y2], length, pygame.Color)
        for i in ind:
            # Getting random part of line to change 
            vertex = np.random.randint(0, 2) 
            color_channel = np.random.randint(0, 3)
            angle = np.random.randint(0, 360)
            x = shapes[i][int(not vertex)][0] + math.cos(math.radians(angle)) * shapes[i][2] 
            y = shapes[i][int(not vertex)][1] + math.sin(math.radians(angle)) * shapes[i][2]
            # Keep generating if outside of border_box
            while not inBorder(border_box, (x, y)): 
                angle = np.random.randint(0, 360)
                x = shapes[i][int(not vertex)][0] + math.cos(math.radians(angle)) * shapes[i][2]
                y = shapes[i][int(not vertex)][1] + math.sin(math.radians(angle)) * shapes[i][2]
            shapes[i][vertex][0] = x
            shapes[i][vertex][1] = y
            if colorOn:     
                if color_channel == 0:
                    shapes[i][2].r = np.random.randint(0, 256)
                elif color_channel == 1:
                    shapes[i][2].g = np.random.randint(0, 256)
                else:
                    shapes[i][2].b = np.random.randint(0, 256)
    elif shape_type == "circle": 
        # ([x, y], radius, pygame.Color)
        for i in ind: 
            newX, newY = shapes[i][0][0] + np.random.randint(-100, 101), shapes[i][0][1] + np.random.randint(-100, 101)
            color_channel = np.random.randint(0, 3)
            while not inBorder(border_box, (newX + shapes[i][1], newY + shapes[i][1])) or not inBorder(border_box, (newX - shapes[i][1], newY - shapes[i][1])): 
                newX, newY = shapes[i][0][0] + np.random.randint(-100, 101), shapes[i][0][1] + np.random.randint(-100, 101)
            shapes[i][0][0] = newX
            shapes[i][0][1] = newY
            if colorOn:     
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
        (x, y) position  

    Returns
    -------
    Whether the position remains in the given border_box 
    """
    return (0 <= pos[0] and pos[0] <= border_box[0]) and (0 <= pos[1] and pos[1] <= border_box[1])

def cost(screen, y): 
    """Return the scalar cost (MSE) between prediction (yhat) and true image (y)

    Parameters 
    ----------
    screen: pygame.Surface 
        current main screen for pygame 
    y: np.array 
        true image of what we are estimating 
    
    Returns 
    ------- 
    MSE between screen and y 
    """
    yhat = pygame.surfarray.array3d(screen)
    yhat = yhat.swapaxes(0, 1)
    yhat = yhat.flatten() 
    y = y.flatten() 
    m = len(yhat)
    cost = np.sum(np.square(y - yhat), keepdims=False) 
    cost = 1/m * cost 
    return cost 

def generate_shapes(border_box, param): 
    """Generate the starting state of shapes  

    Parameters
    ----------
    border_box: tuple 
        (width, height) of screen to bound the shapes within 
    param: dict 
        dictionary of parameters 
    
    Returns
    -------
    shapes: list 
        list of parameters for each required shape 
    """
    shapes = []
    shape_type = param["shape_type"]
    count = np.clip(param["count"], a_min=1, a_max=500)
    colorOn = param["colorOn"]

    if shape_type == "line": 
        # ((start pos), (end pos), length, pygame.Color)
        line_length = param["length"] 
        for i in range(count): 
            # Random orientation of line 
            x1, y1 = np.random.randint(0, border_box[0]), np.random.randint(0, border_box[1])
            angle = np.random.randint(0, 360)
            x2 = x1 + math.cos(math.radians(angle)) * line_length
            y2 = y1 + math.sin(math.radians(angle)) * line_length
            # Keep generating if outside of border_box
            while not inBorder(border_box, (x2, y2)): 
                angle = np.random.randint(0, 360)
                x2 = x1 + math.cos(math.radians(angle)) * line_length
                y2 = y1 + math.sin(math.radians(angle)) * line_length
            if colorOn: 
                r, g, b = np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)
                shapes.append(([x1, y1], [x2, y2], line_length, pygame.Color(r, g, b)))
            else: 
                shapes.append(([x1, y1], [x2, y2], line_length, pygame.Color("black")))
    elif shape_type == "circle": 
        # ((center), radius, pygame.Color)
        radius = param["radius"]
        
        for i in range(count): 
            x, y = np.random.randint(0, border_box[0]), np.random.randint(0, border_box[1])
            while (not inBorder(border_box, (x+radius, y)) or 
                   not inBorder(border_box, (x-radius, y)) or 
                   not inBorder(border_box, (x, y+radius)) or 
                   not inBorder(border_box, (x, y-radius))): 
                x, y = np.random.randint(0, border_box[0]), np.random.randint(0, border_box[1])
            if colorOn: 
                r, g, b = np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)
                shapes.append(([x, y], radius, pygame.Color(r, g, b)))
            else: 
                shapes.append(([x, y], radius, pygame.Color("black")))




    return shapes  

def preprocess_image(img): 
    """Preprocess the input image 
    PIL -> np.array -> opencv format -> grayscale -> Canny -> dilate -> bitwise flip -> merge 

    Parameters 
    ----------
    img: PIL.Image 
        input image 
    
    Returns
    -------
    transformed input image
    """
    opencvImage = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR) 
    grayImage = cv.cvtColor(opencvImage, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(grayImage, 100, 200)
    kernel = np.ones((5,5), np.uint8)
    edges = cv.dilate(edges, kernel, iterations=1)
    edges = cv.bitwise_not(edges)
    edges = cv.merge((edges, edges, edges))
    return edges 
