import os
import moviepy.video.io.ImageSequenceClip
from random import randint

# the paths to the txt files containing text (words and sentences)
files = [
        'C:/Users/nazri/Desktop/CIS522/words_no_doubles.txt', 
        'C:/Users/nazri/Desktop/CIS522/words_with_doubles.txt',
        'C:/Users/nazri/Desktop/CIS522/phrases_no_doubles.txt',
        'C:/Users/nazri/Desktop/CIS522/phrases_with_doubles.txt'
        ]

# create folders for storing videos
os.mkdir('C:/Users/nazri/Desktop/ASL_Videos')
os.mkdir('C:/Users/nazri/Desktop/ISL_Videos')

for file in files:

    # get the name of the category
    name = file.split('/')[-1].strip('.txt')

    # make folders for storing videos of this category
    os.mkdir('C:/Users/nazri/Desktop/ASL_Videos/' + name)
    os.mkdir('C:/Users/nazri/Desktop/ISL_Videos/' + name)

    # read in text data and convert into list split by ' ' and replace with '_'
    with open(file) as file_object:
        content = file_object.read()
        lines = content.split('\n')
    content = [line.replace(' ', '_').upper() for line in lines]

    # process for creating asl videos. make sure to use the resized vid images
    for text in content:
        images = []
        for letter in text:
            for i in range(1, 25):
                num = str(i)
                images.append('C:/Users/nazri/Desktop/asl_vid_resized/' + letter + '/' + letter + num + '.jpg')
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps=24)
        clip.write_videofile('C:/Users/nazri/Desktop/ASL_Videos/' + name + '/ASL_{}.mp4'.format(''.join(text)))

    # process for creating isl videos. make sure to use the resized vid images
    for text in content:
        images = []
        for letter in text:
            for i in range(0, 24):
                num = str(i)
                images.append('C:/Users/nazri/Desktop/isl_vid_resized/' + letter + '/' + letter + num + '.jpg')
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(images, fps=24)
        clip.write_videofile('C:/Users/nazri/Desktop/ISL_Videos/' + name + '/ISL_{}.mp4'.format(''.join(text)))
    
