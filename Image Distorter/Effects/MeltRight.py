import random

amplitude_num = "amount of distortion (in pixels) (maximum must be smaller than the height of the image)"
blockSize_num = "block size (in pixels)"

def execute(img):
    #amplitude = input("how much should the image be distorted (max should be smaller than the image pixel width)? ")
    #blockSize = input("how big should the blocks be? ")
    amplitude = random.randint(1, img.size[0])
    blockSize = random.randint(1, int(img.size[0]/8))
    xCounter = 0
    rAmp = 0
    for y in range(img.size[1]):
        if xCounter % int(blockSize) == 0:
            rAmp = random.randint(0, int(amplitude))
        for x in range(img.size[0]):
            pixelWidthToEdit = rAmp + x
            if pixelWidthToEdit >= img.size[0]:
                pixelWidthToEdit = pixelWidthToEdit - img.size[0]
            pixelAmp = img.getpixel((pixelWidthToEdit, y))
            currentPixel = img.getpixel((x,y))
            img.putpixel((x,y),pixelAmp)
            img.putpixel((pixelWidthToEdit, y),currentPixel)
        xCounter += 1
    #Saving     
    return img
    