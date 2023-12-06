import sys, os
import pygame
import numpy as np
import cv2 as cv
from PIL import Image 
from helper import cost 
from helper import generate_shapes
from helper import neighbors
from helper import preprocess_image

# Max width / height for the true image 
WIDTH = 500 
HEIGHT = 500 

class Main: 
    def __init__(self, true_y, param): 
        pygame.init() 
        pygame.display.set_caption("Estimator")
        self.screen = pygame.display.set_mode((true_y.shape[1], true_y.shape[0]))
        self.clock = pygame.time.Clock() 

        self.true_y = true_y 
        self.param = param 
        self.shape_type = param["shape_type"]
        self.colorOn = param["colorOn"]
        self.shapes = generate_shapes(self.screen.get_size(), param=param)
        self.draw(self.shapes)
        self.best_cost = cost(self.screen, self.true_y) # Initial cost 
        if param["algo_type"] == 1: 
            self.temp = 0.05
            self.decay = 0.98 
            self.resetTimer = 0 

    def draw(self, shapes): 
        """Paint current screen with shapes

        Parameters 
        ----------
        shapes: list
            list of shapes to draw onto the screen 
        
        Returns 
        -------
        None
        """
        self.screen.fill('white')
        for shape in shapes: 
            if self.shape_type == "line": 
                pygame.draw.line(self.screen, shape[3], shape[0], shape[1], width=3)
            elif self.shape_type == "circle": 
                pygame.draw.circle(self.screen, shape[2], shape[0], shape[1], width=3)

    def run(self): 
        """ Control game loop"""
        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
            
            # Hill-climbing 
            if self.param["algo_type"] == 0: 
                neighbor_state = neighbors(self.screen.get_size(), self.shapes, param=self.param)
                self.draw(neighbor_state)
                current_cost = cost(self.screen, self.true_y) 
                if current_cost < self.best_cost: 
                    self.best_cost = current_cost
                    self.shapes = neighbor_state
            # Simulated Annealing 
            elif self.param["algo_type"] == 1: 
                neighbor_state = neighbors(self.screen.get_size(), self.shapes, param=self.param)
                self.draw(neighbor_state)
                current_cost = cost(self.screen, self.true_y) 
                if current_cost < self.best_cost: 
                    self.best_cost = current_cost
                    self.shapes = neighbor_state
                elif current_cost > self.best_cost and np.random.uniform() < (np.exp(-(current_cost - self.best_cost) / self.temp)): 
                    self.best_cost = current_cost
                    self.shapes = neighbor_state
                elif current_cost >= self.best_cost: 
                    self.resetTimer += 1
                    # Increasing temp to escape local minima 
                    if self.resetTimer > 10000:
                        self.resetTimer = 0 
                        self.temp = 0.001

                self.temp = self.temp * self.decay

            self.draw(self.shapes)

            pygame.display.update() 
            self.clock.tick(60) 
                    

if __name__ == "__main__": 
    params = sys.argv[1:]
    img_path, shape_type, algo_type = params 
    assert os.path.isfile(img_path)

    with Image.open(img_path) as im: 
        im.thumbnail((WIDTH, HEIGHT), Image.LANCZOS)
        im.show()

    # GOAL Image 
    edges = preprocess_image(im)

    # Debug purposes
    # cv.imshow('edge', edges)
    # cv.waitKey(0)    
    
    param = dict()

    if shape_type == "circle": 
        param["radius"] = int(input("Radius of circle: "))
        param["count"] = int(input("Number of circles: "))
    else: 
        param["length"] = int(input("Length of line: ")) 
        param["count"] = int(input("Number of lines: "))
    param["shape_type"] = shape_type
    param["colorOn"] = False 
    param['algo_type'] = int(algo_type) # 0 --> Hill descent, 1 --> simulated annealing 

    main = Main(edges, param)
    main.run() 

