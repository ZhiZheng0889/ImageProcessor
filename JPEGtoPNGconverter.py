import sys
import os
from PIL import Image

#Grab both source of jpg and destination for png exists
source = sys.argv[1]
destination = sys.argv[2]

#Check if the destination folder exist, if not then create it
if not os.path.exists(destination):
    os.makedirs(destination)

#Loop through each image in source folder to convert jpg to png and save into destination folder
for filename in os.listdir(source):
    #Grabbing the jpg from the source folder
    img = Image.open(f'{source}{filename}')

    # splitext to make sure the filename doesn't contain .jpg when converting
    clean_name = os.path.splitext(filename)[0]

    #Converting the jpg to png and saving it to the destination
    img.save(f'{destination}{clean_name}.png', 'png')
    print(f'Image {filename} is convert to {clean_name}.png')
print('all done!')