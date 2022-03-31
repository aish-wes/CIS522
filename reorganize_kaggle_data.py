import os
import shutil

# list of directory names (letters and _ for space)
letters = [chr(i) for i in range(65, 91)]
letters.insert(0, '_')

# rename the space folder to _
asl_path = 'C:/Users/nazri/Desktop/asl_alphabet_train/'
os.rename(asl_path + 'space', asl_path + '_')

# rename the 5 folder to _
isl_path = 'C:/Users/nazri/Desktop/Indian/'
os.rename(isl_path + '5', isl_path + '_')

# for the isl data, add the letter (class) in front of the file name for organization. asl data is already like this
for letter in letters:
    for file in os.listdir(isl_path + letter + '/'):
        os.rename(isl_path + letter + '/' + file, isl_path + letter + '/' + letter + file)

# make the letter folders for the directory to contain the sample for making videos (the first 24 images of each letter)
asl_vid_images_path = 'C:/Users/nazri/Desktop/asl_vid_images/'
for letter in letters:
    os.mkdir(asl_vid_images_path + letter)

# move the first 24 images of each letter to different folder. asl images start counting at 1
for letter in letters:
    for i in range(1, 25):
        num = str(i)
        shutil.move(asl_path + letter + '/' + letter + num + '.jpg', asl_vid_images_path + letter + '/' + letter + num + '.jpg')

# make the letter folders for the directory to contain the sample for making videos (the first 24 images of each letter)
isl_vid_images_path = 'C:/Users/nazri/Desktop/isl_vid_images/'
for letter in letters:
    os.mkdir(isl_vid_images_path + letter)

# move the first 24 images of each letter to different folder. isl images start counting at 0
for letter in letters:
    for i in range(0, 24):
        num = str(i)
        shutil.move(isl_path + letter + '/' + letter + num + '.jpg', isl_vid_images_path + letter + '/' + letter + num + '.jpg')
    

