# SHAPESHIFT

<!-- ABOUT THE PROJECT -->
## About The Project 
In this project, I implemented two algorithms, hill climbing and simulated annealing, that estimates input image based on shapes. Through different experimentation, the project aimed to understand the intricacies of these algorithms in the context of image estimation. Both methods are optimization techniques that starts with an arbitrary solution to a problem, then attempts to find a better solution by making incremental changes to the solution. The results of this project not only showcase the effectiveness of these algorithms in estimating input images from shapes but also lay the groundwork for potential future extensions. 


True Image             |  Estimated Image
:-------------------------:|:-------------------------:
<img src="https://github.com/Goddrew/shapeshift/blob/main/images/bird.jpg" alt="bird" width="350"/>  |  <img src="https://github.com/Goddrew/shapeshift/blob/main/demo/hill_bird.gif" alt="bird_hill_descent" width="350"/>
<img src="https://github.com/Goddrew/shapeshift/blob/main/images/feelsgoodman.jpg" alt="pepe" width="350"/> | <img src="https://github.com/Goddrew/shapeshift/blob/main/demo/hill_pepe.gif" alt="pepe_hill_descent" width="350" />
<img src="https://github.com/Goddrew/shapeshift/blob/main/images/car.jpg" alt="car" width="350"/> | <img src="https://github.com/Goddrew/shapeshift/blob/main/demo/hill_car.gif" alt="car_hill_descent" width="350"/>

### Built With 

* [![Pillow][pillow-icon]][pillow-url]
* [![Pygame][pygame-icon]][pygame-url]
* [![Numpy][numpy-icon]][numpy-url]
* [![Opencv][cv-icon]][cv-url]

<!-- GETTING STARTED -->
## Getting Started 

### Prerequisites
1. **Clone the repo** 
    ```sh
    git clone https://github.com/Goddrew/shapeshift.git
    ```
2. **Install packages**
    ```sh
    pip install -r requirements.txt
    ```
### Running The Project
1. **To run the code**
    ```sh
    python main.py image-path shape-type algo-type
    ```
    ```sh
    # Example to run bird picture  
    python main.py .\images\bird.jpg line 0
    ```
    image-path: Path of the image 

    shape-type: circle | line 

    algo-type: hill climbing (0) | simulated annealing (1)
2. **User input** 
    Answer the provided user input for the size of the shape and number of shapes  


<!-- LIMITATIONS -->
## Limitations 
When dealing with images featuring intricate backgrounds and multiple subjects, the effectiveness of the proposed solution diminishes due to the abundance of local optima. Hill climbing, being prone to getting trapped in local optima, may struggle in such scenarios. While simulated annealing has the potential to break free from local optima, its success depends on the complexity of the given image. Nonetheless, hill climbing and simulated annealing works well when applied to images with a well-defined subject.

<!-- FUTURE -->
## Future 
This project can be extended in many directions. One potential direction invovles exploring image estimation in 3D space as an alternative method to the current one. Another potential direction invovles improving the image estimation accuracy by incorporating a broader range of shapes and classes of hill climbing algorithm. 

[pillow-url]: https://pillow.readthedocs.io/en/stable/
[pillow-icon]: https://img.shields.io/badge/Pillow-pink
[pygame-url]: https://www.pygame.org/wiki/about
[pygame-icon]: https://img.shields.io/badge/Pygame-green?link=https%3A%2F%2Fwww.pygame.org%2Fwiki%2Fabout
[numpy-url]: https://numpy.org/
[numpy-icon]: https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white
[cv-url]: https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
[cv-icon]: https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white

