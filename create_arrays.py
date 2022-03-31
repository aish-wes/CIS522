import os
from matplotlib.image import imread
import numpy as np

# paths to the resized image files
path = 'C:/Users/nazri/Desktop/asl_resized/'
# path = 'C:/Users/nazri/Desktop/isl_resized/'

# create list of letters for iterating through folders
letters = [chr(i) for i in range(65, 91)]
letters.insert(0, '_')

# process for collecting the image files into a list
image_files = []
for letter in letters:
    files = os.listdir(path + letter + '/')
    for file in files:
        image_files.append(file)

# create a dictionary for class labels: maps a letter (str) to a integer (int)
classes = {}
for i, letter in enumerate(letters):
    classes[letter] = i

# process for converting each image into a numpy array and storing them all in a list (and getting their label)
data = []
labels = []
for img in image_files:
    # append with appropriate class label
    labels.append(classes[img[0]])
    # convert image to np.array, perform min/max scaling, then flatten
    data.append((imread(path + img[0] + '/' + img) / 255).reshape(-1,))

# convert the list of arrays into one large array NxP for images and convert labels into an array
data = np.array(data)
data = np.stack(data)
labels = np.array(labels)
# save the arrays onto disk
path = 'C:/Users/nazri/Desktop/CIS522/Project/'
np.save(path + 'asl_data.npy', data)
np.save(path + 'asl_labels.npy', labels)
# np.save(path + 'isl_data.npy', data)
# np.save(path + 'isl_labels.npy', labels)