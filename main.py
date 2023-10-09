import sys 
import pygame
from PIL import Image 

WIDTH = 500 
HEIGHT = 500 

class Main: 
    def __init__(self): 
        pygame.init() 
        pygame.display.set_caption("Estimator")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock() 

    def run(self): 
        while True: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
            self.screen.fill('white')    
            pygame.draw.line(self.screen, "black", (0, 0), (40, 40))
            pygame.display.update() 
            self.clock.tick(60) 
                    

if __name__ == "__main__": 
    params = sys.argv[1:]
    img_path, = params # Extend for further customization 
    with Image.open(img_path) as im: 
        im.thumbnail((WIDTH, HEIGHT), Image.LANCZOS)
        im.show()
    
    main = Main()
    main.run() 

# MAIN TODOS 
# 1) Define neighboring state space for current position of shapes 
# 2) Define evaluation function 
# 3) Implement hill descent   