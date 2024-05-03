# import pillow
from PIL import Image
import os

image1 = Image.open("./img/img_1.png")
#image1.show() # to open and show image

# we can save the image
#image1.save('rumah.png') # its will create a new image with the image

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))
        
