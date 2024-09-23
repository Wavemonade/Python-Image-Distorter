from PIL import ImageFilter

radius_num = "the Radius of the Gaussian Blur (in pixels): "

def execute(img):
    radius = input(radius_num)
    blur = img.filter(ImageFilter.GaussianBlur(radius=int(radius)))
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r1 = 0
            g1 = 0
            b1 = 0
            a1 = 0
            r2 = 0
            g2 = 0
            b2 = 0
            a2 = 0
            if img.format == "PNG":
                r1, g1, b1, a1 = img.getpixel((x, y))
                r2, g2, b2, a2 = blur.getpixel((x,y))
                a2 = 0
            else:
                r1, g1, b1 = img.getpixel((x, y))
                r2, g2, b2 = blur.getpixel((x,y))
                a1 = 1
                a2 = 0
            img.putpixel((x,y),(r1-r2, g1-g2 , b1-b2, a1-a2))
    return img
