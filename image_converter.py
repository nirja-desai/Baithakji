from PIL import Image
import os

# Specify the directory path
directory = "images/"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (i.e. not a directory)
    if os.path.isfile(os.path.join(directory, filename)):
        # Check if the file extension is .gif
        if filename.endswith('.gif'):
        # Load the GIF image
            with Image.open(directory + filename) as im:
        
                # Convert the image to JPEG
                rgb_im = im.convert('RGB')
                
                # Save the JPEG image
                rgb_im.save(directory + filename[:-4] + ".jpg")
                
