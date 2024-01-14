'''
TASK 3: Develop an AI application that can detect and recognize faces in
images or videos. Use pre-trained face detection models like Haar cascades 
or deep learning-based face detectors, and optionally add face recognition 
capabilities using techniques like Siamese networks or ArcFace.

'''
'''
Face Detection and Recognition using OpenCV, Face-Recognition and NumPy. 
The program takes an image and detects faces that it already knows along 
with captions which are the names of the faces. 
First the program computes the encodings of the images in actors_known folder
and then it compares it with the encodings of the input image. 
Next it displays the input image with the detected faces along with captions 
which is the file name of the images in actors_known folder.
Here, the Oppenheimer movie cast images are used as an example, the actors_known
folder contains individual images of some actors. These images have the name of 
the actor as a file name. The input image is a image of all actors from Oppenheimer.
The input image is displayed again with detected faces and captions given to those
whose faces are recognized, others have caption of 'unknown'.

'''

import cv2
import face_recognition
import os
import numpy as np

def read_img(path):
    
    #Read the image
    img = cv2.imread(path)

    #Extract image features and resize
    (h, w) = img.shape[:2]
    width = 500
    ratio = width / float(w)
    height = int(h * ratio)
    return cv2.resize(img, (width, height))

def detect_and_draw_faces(image_path, dataset_encodings, dataset_names, display_scale=0.5):
    
    #Read the image
    image = cv2.imread(image_path)

    #Resize image
    display_height = int(image.shape[0] * display_scale)
    display_width = int(image.shape[1] * display_scale)
    resized_image = cv2.resize(image, (display_width, display_height))

    #Locate all faces and extract face encodings
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    matched_names = []
    for i, (face_location, face_encoding) in enumerate(zip(face_locations, face_encodings)):
        top, right, bottom, left = face_location

        #Compare with actors_known encodings
        matches = face_recognition.compare_faces(dataset_encodings, face_encoding)
        name = "Unknown"

        #If match is found, use the name from the actors_known folder
        if True in matches:
            first_match_index = matches.index(True)
            name = dataset_names[first_match_index]
            matched_names.append(name)

        #Create rectangles and captions for matched faces
        color = (0, 255, 0)
        cv2.rectangle(image, (left, top), (right, bottom), color, 2)
        caption = f'{name}'
        cv2.putText(image, caption, (left, bottom+20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)

    #Image resize for display
    resized_image = cv2.resize(image, (display_width, display_height))

    #Display the entire image with captions for matched faces
    cv2.imshow('Detected Faces', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return matched_names

if __name__ == "__main__":
    
    #Load actors_known images and compute encodings
    known_encodings = []
    known_names = []
    known_dir = 'actors_known'

    for file in os.listdir(known_dir):
        img = read_img(os.path.join(known_dir, file))
        img_enc = face_recognition.face_encodings(img)[0]
        known_encodings.append(img_enc)
        known_names.append(file.split('.')[0])

    #Input image
    image_path = 'movie_cast.webp'

    #Call function
    matched_names = detect_and_draw_faces(image_path, known_encodings, known_names, display_scale=0.75)

    #Display the names of matched faces
    print("Matched Names:")
    for i, name in enumerate(matched_names):
        print(f"Person {i+1}: {name}")
