Strength_percent = "Strength(in %): "

def execute(img):
    im = img.convert("L")
    for x in range(img.size[0]):
        for y in range(img.size[1]):       
            r = 0
            if img.format == "PNG":
                r = im.getpixel((x, y))
            else:
                r = im.getpixel((x, y))
            
            img.putpixel((x,y),(r,0,255-r,255))
    return img