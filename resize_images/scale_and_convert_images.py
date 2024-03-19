import os
from PIL import Image

source_path = 'example-images'  # Specify the path to your folder
target_path = 'icons'
x=0

# Iterate through each file in the folder
for filename in os.listdir(source_path):
    file_path = os.path.join(source_path, filename)

    #Generate new path where to save the image and add number tot he name
    #.jpeg has to be in the name for Widnows OS, I beleive on Ubuntu works with converting it to RGB and then just format='JPEG'
    new_path = os.path.join(target_path, "pic{}.jpeg".format(x))
    x=x+1
    
    image = Image.open(file_path)
    new_image = image.resize((128, 128)).rotate(90).convert('RGB')
    
    #Save image on specific path and in format
    new_image.save(new_path, format='JPEG')
