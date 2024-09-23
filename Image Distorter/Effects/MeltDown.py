import random

amplitude_num = "amount of distortion (in pixels) (maximum must be smaller than the height of the image): "
blockSize_num = "block size (in pixels): "

def execute(img):
    #amplitude = input("how much should the image be distorted (max should be smaller than the image pixel height)? ")
    #blockSize = input("how big should the blocks be? ")
    amplitude = random.randint(1, img.size[1])
    blockSize = random.randint(1, int(img.size[1]/8))
    yCounter = 0
    rAmp = 0
    for x in range(img.size[0]):
        if yCounter % int(blockSize) == 0:
            rAmp = random.randint(0, int(amplitude))
        for y in range(img.size[1]):
            pixelHeightToEdit = rAmp + y
            if pixelHeightToEdit >= img.size[1]:
                pixelHeightToEdit = pixelHeightToEdit - img.size[1]
            pixelAmp = img.getpixel((x, pixelHeightToEdit))
            currentPixel = img.getpixel((x,y))
            img.putpixel((x,y),pixelAmp)
            img.putpixel((x, pixelHeightToEdit),currentPixel)
        yCounter += 1
    return img