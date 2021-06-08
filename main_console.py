import glob
import os
from PIL import Image

# convert all images in folder ./photos to pdf
image_list = []
images = glob.glob('./photos/*.jpg')

for i in images:
    image1 = Image.open(i)
    im1 = image1.convert('RGB')
    image_list.append(im1)
image = image_list.pop(0)
image.save('./photos/test.pdf', save_all=True, append_images=image_list)

# delete all jpg file in folder ./photos
files = glob.glob('./photos/*.jpg')
for f in files:
    os.remove(f)
