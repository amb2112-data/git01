import sys
import os
from PIL import Image, ImageFilter

source_folder = sys.argv[1]
output_folder = sys.argv[2]

source_path = f'.{source_folder}'
output_path = f'.{output_folder}'

print(os.path.exists(source_path))
print(os.path.exists(output_path))

input_imgs_list = os.listdir(source_path)

print(input_imgs_list)

for i in input_imgs_list:
    i_split = os.path.splitext(i)[0]
    i_path = f'{source_path}/{i}'
    with Image.open(i_path) as im:
        im_dt = im.filter(ImageFilter.DETAIL)
        im_bw = im.convert('L')
        im_bw.save(f'{output_path}/{i_split}.png', "png")

