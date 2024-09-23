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
            
            r = int(r - (abs(x/2 - img.size[0]/4)+abs(y/2 - img.size[1]/4)))
            g = int(g - (abs(x/2 - img.size[0]/4)+abs(y/2 - img.size[1]/4)))
            b = int(b - (abs(x/2 - img.size[0]/4)+abs(y/2 - img.size[1]/4)))
            
            img.putpixel((x,y),(r, g , b, a))   
    return img
