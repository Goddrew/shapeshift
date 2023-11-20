import sys 
import pygame
import numpy as np
from PIL import Image 
from helper import cost 
from helper import generate_shapes
from helper import neighbors

# Max width / height for the true image 
WIDTH = 500 
HEIGHT = 500 

class Main: 
    def __init__(self, true_y, shape_type): 
        pygame.init() 
        pygame.display.set_caption("Estimator")
        self.true_y = true_y # Goal (np.array)
        self.screen = pygame.display.set_mode((self.true_y.shape[1], self.true_y.shape[0]))
        self.clock = pygame.time.Clock() 
        self.shape_type = shape_type
        self.colorOn = False
        self.shapes = generate_shapes(self.screen.get_size(), shape_type=self.shape_type, count=100, color=self.colorOn)
        self.prev_cost = self._init_prev_cost() # Initial cost 

    def _init_prev_cost(self): 
        for shape in self.shapes: 
                if self.shape_type == "line": 
                    pygame.draw.line(self.screen, shape[2], shape[0],  shape[1], 3)
        return cost(self.screen, self.true_y)

    def run(self): 
        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()

            # Hill-climbing 
            neighbor_state = neighbors(self.shapes, self.shape_type, self.colorOn)
            self.screen.fill('white')   
            for shape in neighbor_state: 
                if self.shape_type == "line": 
                    pygame.draw.line(self.screen, shape[2], shape[0],  shape[1], 3)
            current_cost = cost(self.screen, self.true_y) 
            if current_cost < self.prev_cost: 
                self.prev_cost = current_cost
                self.shapes = neighbor_state
                print("changed")
                print(current_cost, self.prev_cost)        
            else: 
                print("Didnt change")

            # Draw the shapes
            self.screen.fill('white')   
            for shape in self.shapes: 
                if self.shape_type == "line": 
                    pygame.draw.line(self.screen, shape[2], shape[0],  shape[1], 3)

            pygame.display.update() 
            self.clock.tick(60) 
                    

if __name__ == "__main__": 
    params = sys.argv[1:]
    img_path, shape_type = params # Extend for further customization 

    with Image.open(img_path) as im: 
        im.thumbnail((WIDTH, HEIGHT), Image.LANCZOS)
        im.show()
    true_y = np.array(im) # True image 
    main = Main(true_y, shape_type)
    main.run() 
