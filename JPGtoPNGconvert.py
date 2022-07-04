import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('finshed!')


#pictures in /pics folder are converted JPG to PNG, folder "newformat" created if it doesn't exist

#Run CMD, go (cd) to current directory where this .py is located
#example path: C:\Users\Username\Desktop\Python>
#Run -> python3 JPGtoPNGconvert.py pics\ newformat\
#C:\Users\Username\Desktop\Python> python3 JPGtoPNGconvert.py pics\ newformat\