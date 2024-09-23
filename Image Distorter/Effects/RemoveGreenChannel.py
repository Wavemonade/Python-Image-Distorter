def execute(img):
    #Removes Green Channels
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
            img.putpixel((x,y),(r, 0 , b, a))
    return img