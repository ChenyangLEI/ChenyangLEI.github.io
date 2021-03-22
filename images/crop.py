import imageio
import numpy as np
from glob import glob 

img_names = sorted(glob("*png")) + sorted(glob("*jpg")) + sorted(glob("*PNG")) + sorted(glob("*JPG"))

print(len(img_names))
for idx, img_name in enumerate(img_names):
    img = imageio.imread(img_name)
    h, w = img.shape[:2]
    if h < w :
        new_img = img[:,w//2 - h//2:w//2 + h//2]
    elif h > w :
        new_img = img[h//2 - w//2:h//2 + w//2, :]
    else:
        new_img = img
    new_h, new_w = new_img.shape[:2]
    imageio.imwrite(img_name, new_img)
    print(idx, img_name, h, w, new_h, new_w)
