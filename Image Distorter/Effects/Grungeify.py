import random

def execute(img):
    #Maximises Blue Channels
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r = 0
            g = 0
            b = 0
            a = 0
            if img.format == "PNG":
                r, g, b, a = img.getpixel((x, y))
            else:
                r, g, b = img.getpixel((x, y))
                a = 1
            r = new_index = max(0, min(255, r + random.randint(5, 40),255))
            g = new_index = max(0, min(255, g + 10 + random.randint(5, 40),255))
            b = new_index = max(0, min(255, b+ random.randint(5, 40),255))
            img.putpixel((x,y),(r, g, b, 255))
    return img