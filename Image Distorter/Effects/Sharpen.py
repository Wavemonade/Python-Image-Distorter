from PIL import ImageFilter

def execute(img):
    #have to do this, or the original file gets lost
    sharp = img.filter(ImageFilter.SHARPEN())
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r = 0
            g = 0
            b = 0
            a = 0
            if img.format == "PNG":
                r, g, b, a = sharp.getpixel((x, y))
            else:
                r, g, b = sharp.getpixel((x, y))
                a = 1
            img.putpixel((x,y),(r, g , b, a))   
    return img
