pixelHeight_num = "line thickness(in pixels): "

def execute(img):
    pixelHeight = input(pixelHeight_num)
    yCounter = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if yCounter % int(pixelHeight) != 0:        
                r = 0
                g = 0
                b = 0
                a = 0
                if img.format == "PNG":
                    r, g, b, a = img.getpixel((x, y))
                else:
                    r, g, b = img.getpixel((x, y))
                    a = 1
                img.putpixel((x,y),(0,0,0,255))
            yCounter += 1
    return img