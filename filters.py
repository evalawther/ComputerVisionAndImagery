import scipy
import numpy as np


def magnitude(x,y): 
    return np.sqrt(x**2 + y**2)

def robinson_edge(img):
    robinson_x = np.array([[1,1,1],
                           [1,-2,1],
                           [-1,-1,-1]])
    robinson_y = np.array([[-1,1,1],
                           [-1,-2,1],
                           [-1,1,1]]) # define kernels
    img_robinson_x = abs(scipy.signal.convolve2d(img, robinson_x))
    img_robinson_y = abs(scipy.signal.convolve2d(img, robinson_y))# apply convolution of each
    return magnitude(img_robinson_x, img_robinson_y) # calculate the magnitude of the convolution results

def sobel_edge(img):
    sobel_x = np.array([[1,2,1],
                        [0,0,0],
                        [-1,-2,-1]])
    sobel_y = np.array([[-1,0,1],
                        [-2,0,2],
                        [-1,0,1]])
    img_sobel_x = abs(scipy.signal.convolve2d(img, sobel_x))
    img_sobel_y = abs(scipy.signal.convolve2d(img, sobel_y))
    return magnitude(img_sobel_x, img_sobel_y)

def prewitt_edge(img):
    prewitt_x = np.array([[1,1,1],
                          [0,0,0],
                          [-1,-1,-1]])
    prewitt_y = np.array([[-1,0,1],
                          [-1,0,1],
                          [-1,0,1]])
    img_prewitt_x = abs(scipy.signal.convolve2d(img, prewitt_x))
    img_prewitt_y = abs(scipy.signal.convolve2d(img, prewitt_y))
    return magnitude(img_prewitt_x, img_prewitt_y)

def kirsch_edge(img):
    kirsch_x = np.array([[3,3,3],
                         [3,0,3],
                         [-5,-5,-5]])
    kirsch_y = np.array([[-5,3,3],
                         [-5,0,3],
                         [-5,3,3]])
    img_kirsch_x = abs(scipy.signal.convolve2d(img, kirsch_x))
    img_kirsch_y = abs(scipy.signal.convolve2d(img, kirsch_y))
    return magnitude(img_kirsch_x, img_kirsch_y)

def gaussian_edge(img):
    gaussian_x = np.array([[-1,-2,0,2,1],
                           [-4,-8,0,8,4],
                           [-6,-12,0,12,6],
                           [-4,-8,0,8,4],
                           [-1,-2,0,2,1]])
    gaussian_y = np.array([[-1,-4,-6,-4,-1],
                           [-2,-8,-12,-8,-2],
                           [0,0,0,0,0],
                           [2,8,12,8,2],
                           [1,4,6,4,1]])
    img_gaussian_x = abs(scipy.signal.convolve2d(img, gaussian_x))
    img_gaussian_y = abs(scipy.signal.convolve2d(img, gaussian_y))
    return magnitude(img_gaussian_x, img_gaussian_y)

def thresholdCalc(img, threshold=None):
    if (threshold == None): # threshold = np.mean(img)
        mean = np.mean(img)
        std = np.std(img)
        threshold = mean + 0.5 * std
    return img > threshold

def inverse(img): 
    return ~img