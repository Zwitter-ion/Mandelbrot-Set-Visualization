
# Title for CLI

print("#### Mandlebrot Set (v1.0.0) - ZwitterIon0 ####")

# Predefining questions with some value

questionData = {"Enter the minimum value of x (Default = -2): ": -2, "Enter the maximum value of x (Default = 1): ":1, "Enter the minimum value of y (Default = -1.5): ":-1.5, "Enter the maximum value of y (Default = 1.5): ":1.5, "Enter the value of width (Default = 1000): ": 1000,"Enter the value of height (Default = 1000): ":1000, "Enter the maximum number of Iteration (Default = 100): ": 100,"Enter initial value of Z (Default = 0): ":0}

# Asking The questions and updating that data 

for questions in range(0,8):
    value = input(list(questionData)[questions])

    if value == "":
        pass
    elif value.isnumeric() == True  or value.lstrip('-').isdigit() == True :
        questionData[list(questionData)[questions]] = int(value)
    else:
        exit()


# Importing necessary functions from the required module

from numpy import zeros, linspace
from matplotlib.pyplot import xlabel, ylabel, figure, imshow, title, show

# Defining the following values

minimumValueOfX, maximumValueOfX, minimumValueOfY, maximumValueOfY,width,height, maxIteration, Z = questionData.get(list(questionData)[0]), questionData.get(list(questionData)[1]), questionData.get(list(questionData)[2]), questionData.get(list(questionData)[3]), questionData.get(list(questionData)[4]), questionData.get(list(questionData)[5]), questionData.get(list(questionData)[6]), questionData.get(list(questionData)[7])

# Class for Generating data for Mandelbrot set

class mandelbrotSet():

    def mandelbrotSetFunction(c, maxIteration, Z):
        for iter in range(maxIteration):
            if 2 > abs(Z) > -1.5:
                Z = Z**2 + c
            else:
                return iter
        return 

    def dataGeneration(minimumValueOfX, maximumValueOfX, minimumValueOfY, maximumValueOfY, width, height):
        x = linspace(minimumValueOfX, maximumValueOfX, width)
        y = linspace(minimumValueOfY, maximumValueOfY, height)
        mset = zeros((height,width))

        for i in range(height):
            for j in range(width):
                mset[i,j] = mandelbrotSet.mandelbrotSetFunction(complex(x[j], y[i]),maxIteration, 0)
        
        return mset

# Generating the data for making the image.  

image = mandelbrotSet.dataGeneration(minimumValueOfX,maximumValueOfX,minimumValueOfY,maximumValueOfY,width,height)

# Class for Image Generation

class imageGeneration():
    
    def generateImage():

        figure(figsize=(10,10), dpi=100) 
        imshow(image, extent=(minimumValueOfX,maximumValueOfX,minimumValueOfY,maximumValueOfY), cmap = 'inferno')
        title("Mandelbrot Set") 
        xlabel("Real Axis") 
        ylabel('Complex Axis')
        show()

# Generating the Image

imageGeneration.generateImage()

# Waiting for user to exit

wantToExit = input('Thank you for using my programme \nGithub Profile: https://github.com/Zwitter-ion \nPress enter to exit.')

exit()