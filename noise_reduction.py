import scipy
import numpy as np

def gaussian_filter(img):
    gaussian = np.array([[1,4,7,4,1], 
                         [4,16,26,16,4],
                         [7,26,41,26,7],
                         [4,16,26,16,4],
                         [1,4,7,4,1]],
                        dtype=np.float32)/273
    return abs(scipy.signal.convolve2d(img, gaussian))

def mean_filter(img):
    mean = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]],
                    dtype=np.float32)/9
    return abs(scipy.signal.convolve2d(img, mean))

def cone_filter(img):
    cone = np.array([[0,1,0],
                     [1,2,1],
                     [0,1,0]], 
                    dtype=np.float32)/6
    return abs(scipy.signal.convolve2d(img, cone))

def same_size(one,two): # Configure two matrices to the same siz e
    min_rows = min(one.shape[0], two.shape[0])
    min_cols = min(one.shape[1], two.shape[1])
    one = one[:min_rows, :min_cols]
    two = two[:min_rows, :min_cols]
    return one, two


 # Noise Reduction Evaluation
def psnr(original, denoised):
    original, denoised = same_size(original, denoised)
    mse = np.mean((original - denoised) ** 2)
    return 20 * np.log10(255.0 / np.sqrt(mse)) #max_pixel = 255.0


