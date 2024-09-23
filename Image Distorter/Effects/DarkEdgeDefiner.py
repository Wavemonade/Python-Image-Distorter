def execute(img):
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
            if r <= 50 and g <= 50 and b <= 50:
                r = 0
                g = 0
                b = 0
            img.putpixel((x,y),(r, g, b, a))
    return img