import random

pixelHeight_num = "Take the y height of the image (in pixels)"

def execute(img):
    pixelHeight = random.randint(3, 200)
    yHeight = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if y % int(pixelHeight) == 0:
                yHeight = y
            r = 0
            g = 0
            b = 0
            a = 0
            if img.format == "PNG":
                r, g, b, a = img.getpixel((x, y))
            else:
                r, g, b = img.getpixel((x, y))
                a = 1
            img.putpixel((x,y),img.getpixel((x, yHeight)))
    return img