import sys 
from PIL import Image 

def main(): 
    pass 

if __name__ == "__main__": 
    params = sys.argv[1:]
    img_path, = params # Extend for further customization 
    with Image.open(img_path) as im: 
        im.show()
    main()

# MAIN TODOS 
# 1) Define neighboring state space for current position of shapes 
# 2) Define evaluation function 
# 3) Implement hill descent 
