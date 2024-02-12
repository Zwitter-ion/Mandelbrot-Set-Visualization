# Importing Modules
import numpy as np
import matplotlib.pyplot as plt

# So basically these are the parameter for this specific set
# Formula : Z(n) = Z(n-1) + C
# Here 'Z' is the recursive function and 'C' is a random complex number

class mandelbortSet():
    def getComplex(realValue, imaginaryValue):

        complexNumber = np.complex64(realValue, imaginaryValue)
        return complexNumber
    
    def mandelbortSet(complexNumber, maxIteration, Z):

        complexNumber

        for iter in range(maxIteration):
            if 2 > abs(Z) > -1.5:
                Z = Z*Z + complexNumber
                print(complexNumber,iter)
            else:
                return iter
                     
        return 

print(mandelbortSet.mandelbortSet(complex(-1, 0), 100, 0))

def graphe(xmin, xmax, ymin, ymax, width, height):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            mset[i,j] = mandelbortSet.mandelbortSet(complex(x[j], y[i]),100, 0)
    
    return mset

xmin, xmax, ymin, ymax = -2, 1,-1.5,1.5
width,height = 1920*2,1080*2

image = graphe(xmin,xmax,ymin,ymax,width,height)

plt.imshow(image, extent=[xmin,xmax,ymin,ymax], cmap = 'hot')

plt.show()