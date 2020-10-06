import face_recognition
from PIL import Image
import cv2
import matplotlib.pyplot as plt

def face_detector(add, file):
    file_name = file.split('/')[-1]
    image = face_recognition.load_image_file(add + file)
    face_locations = face_recognition.face_locations(image)
    face_rois = []
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        face_rois.append(Image.fromarray(face_image).convert('LA').resize((48,48)))
        image = cv2.rectangle(image, (left, top), (right, bottom), (255,0 , 0), 15)
        image = Image.fromarray(image)
        image.save(add + '/media/' + 'processed_' + file_name)
    return 'processed_' + file_name
