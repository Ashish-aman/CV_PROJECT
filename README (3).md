Blend-Invision:Object Segmentation and Blending with its background

## About The Project
Unwanted object removal is a common task in many computer vision and image processing systems. One of the
most popular techniques for object removal is image inpainting, which involves filling in the missing or damaged portions of a picture with information from the surrounding area. In this article, we provide a method for
removing objects from photos that is based on inpainting using two ways and compare the results. We focus
on cv2.INPAINT TELEA ,cv2.INPAINT NS and averaging
neighbouring pixel, two commonly used OpenCV picture
inpainting methods. We discuss the underlying principles
of these methods as well as their benefits and drawbacks
for eliminating things
## Built With
Here are the tools and software used while making this project:-
VsCode editor 
Python(PyCharm)
Google Colab
Climpchamp VideoEditor
MobileCamera
OBS studio
## Getting Started
PREREQUISITE
1. VScode editor
2. Operating System-Windows 7/10
3. i3/i5 PROCESSOR with 8 Gbram min

## Installation
Open VSCode Editor and Run the two .py files attached in the GitHub.
Install cv2 by writing following in the terminal
--pip3 install cv2
Install numpy by writing following in the terminal
--pip3 install numpy
Install numpy by writing following in the terminal
--pip3 install pandas
install ski-image by writing-
--pip3 install scikit


## Usage and Steps

1.After installing the module ,Set the input image location path in the codes from the local space
2.Execute the code for the Average function .py and inpaint function .py

########################


3.For the average function ,When it is run a new window will appear in which select the object you want to create the mask.
4.Click the start point and by seeing the appropriate region draw the rectangle of the blue colour and leave the cursor to the desired end point.
5.After it we will see that a new masked image is shown with that area as complete white and remaining black.
6.A new window which is final output image will also be displayed which shows the blended image after segmentation.
7.Press escape for closing all windows or stop the code to Execute.

#######################################

For the impaint function.py file
1.Run the code.
2.After it a new window will open to select the image.
3.we have to draw free hand from the mouse to the area which we want to remove from the image.
4.As you draw the red colour paint will be seen over the object.
5.Select the area and leave ,a new window will apear in which masked image will be shown and also a final output image will be shown.
6. Also the two final output images will be saved to your Vscode wporkspace folder.

#####################################

For obtaining the  results in the series of images kept in the folder.
PRESS THE 'S' Key to go to the next image ,A new image will be opened,Next Select using the mouse required area and then press s to go to next image.
After dealing with all the images ,
GO to the workspace of the File .You will see the All the required blended output image and Also a csv file which stores the PSNR and blending time  will be saved in the folder.

############################

1.For slic segmentation,Open the google colab and run the .ipynb file and Run the code ,get the desired Result.
## Deliverables/Output
1.Output Blend Image of all the supplied images in the folder.
2..csv file containing evaluation matrix and performance results of each output image.
3.Video Demonstration link
 - https://youtu.be/i2zeDTaWfxU
 
## Authors

- [@97shanu](https://www.github.com/97shanue)
- [Ashish.aman](https://www.github.com/Ashish.aman)



## Acknowledgements

 - [References-Inpainting](https://docs.opencv.org/4.x/df/d3d/tutorial_py_inpainting.html)
 - [Report -Latex](https://www.overleaf.com/project/6416d8951615a2069c04b006)
 - [References-Mouse Callback fn](https://docs.opencv.org/3.4/db/d5b/tutorial_py_mouse_handling.html)

