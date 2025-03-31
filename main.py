
from skimage import io
from filters import *
from edge_detection_metric import metrics
from noise_reduction import *
from plotting import plot
from skimage.feature import canny


GROUND_TRUTH = ['10905 JL Edges.bmp', '43590 AM Edges.bmp', '9343 AM Edges.bmp']
IMAGES = ['10905 JL.bmp', '43590 AM.bmp', '9343 AM.bmp']
NAME = ['10905 JL', '43590 AM', '9343 AM']
FILTERS = [robinson_edge, sobel_edge, prewitt_edge, kirsch_edge, gaussian_edge, canny]
NOISE_REDUCTION = [gaussian_filter, mean_filter, cone_filter]

def greyscaleFromGreen(img):
    return img[:,:,1]


def loadImages():
    images = []
    for gt, im, name in zip(GROUND_TRUTH, IMAGES, NAME):
        ground_truth = io.imread('cells/'+ gt)
        image = io.imread('cells/'+ im)
        images.append([name, ground_truth, image])
    return images

def loadedImagesToGrey(images):
    for set in images:
        set[1] = greyscaleFromGreen(set[1])
        set[2] = greyscaleFromGreen(set[2])
    return images

def toPlot(imagesSet, num, title, filter=None):
    if filter == None:
        plot(imagesSet[0][num],imagesSet[1][num] ,imagesSet[2][num] , title)
    else:
        plot(filter(imagesSet[0][num]),filter(imagesSet[1][num]) ,filter(imagesSet[2][num]) , title)

def applyFilter(imageSet, filterSet): 
    for f in filterSet:
        if f == canny:
            continue
        for set in imageSet:
            set.append(f(set[2]))
    return imageSet


def calculation(applied, imageSet):
    psnrValues = []
    for image in imageSet:
        val = psnr(image[2], image[applied])
        print (image[0], ":", val)
        psnrValues.append(val)
    print("Average PSNR", (sum(psnrValues)/len(psnrValues)))  

def inverseWithThreshold(imageSet, threshold=None):
    for image in imageSet:
        for i in range(3, len(image)):
            image[i] = inverse(thresholdCalc(image[i], threshold))
    return imageSet

def main():
    compareNoiseReduction = False
    applyNoiseReduction = False
    appliedNoiseReduction = gaussian_filter
    compareFilters = True

    images = loadImages()
    # toPlot(images, 2,"Colour Images")
    images = loadedImagesToGrey(images)
    # toPlot(images, 2, "Grey Scale")
    # toPlot(images, 1, "Ground Truth")


    if compareNoiseReduction:
        noisefiltered = applyFilter(images, NOISE_REDUCTION)
        i = 3
        for f in NOISE_REDUCTION:
            toPlot(noisefiltered, i, f.__name__)
            print("PSNR values for", f.__name__, "are:")
            calculation(i, noisefiltered)
            i+=1
        # The higher the PSNR, the better the quality 

    # pass in a noise reduced set before comparing filters 
    if applyNoiseReduction:
        for image in images:
            image[2] = appliedNoiseReduction(image[2])

    if compareFilters:
        filteredImages = inverseWithThreshold(applyFilter(images, FILTERS))
        for set in filteredImages:
            set.append(inverse((canny(set[2],sigma=1))))
            # change sigma = x for different thresholds

        i = 3
        for f in FILTERS:
            toPlot(filteredImages, i, f.__name__)
            print("edge detection metrics with", f.__name__)
            for image in filteredImages:
                print(image[0])
                metrics(image[1], image[i]) 
            i+=1

if __name__ == "__main__":
    main()

