from PIL import Image
import os

# function for resizing images. just put the desired dimensions in resize method
def image_resize(input_path, output_path):
    img = Image.open(input_path)
    img = img.resize((36,36))
    img.save(output_path)

# various paths to image data

input_path = 'C:/Users/nazri/Desktop/Indian/'
# input_path = 'C:/Users/nazri/Desktop/isl_vid_images/'
# input_path = 'C:/Users/nazri/Desktop/asl_alphabet/'
# input_path = 'C:/Users/nazri/Desktop/asl_vid_images/'

output_path = 'C:/Users/nazri/Desktop/isl_resized/'
# output_path = 'C:/Users/nazri/Desktop/asl_resized/'
# output_path = 'C:/Users/nazri/Desktop/isl_vid_resized/'
# output_path = 'C:/Users/nazri/Desktop/asl_vid_resized/'


letters = [chr(i) for i in range(65, 91)]
letters.insert(0, '_')

# iterate through each letter folder and resize images to new destination (makes copies, doesn't effect old ones)
for letter in letters:
    files = os.listdir(input_path + letter + '/')
    for file in files:
        img = image_resize(input_path + letter + '/' + file, output_path + letter + '/' + file)
    print(letter, 'done.')