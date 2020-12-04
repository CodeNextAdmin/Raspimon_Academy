import os, io
from google.cloud import vision
import cv2
import my_raspimon

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'RASPSA.json'
client = vision.ImageAnnotatorClient()

def get_object(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image) #full response from Google cloud vision
    label_annotations = response.label_annotations #array of objects labeled
    description = label_annotations[0].description #get description of one object
    if description:
        return description
    else:
        return 'could not detect object'

def get_emotion(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image) #full response from Google cloud vision
    face_annotations = response.face_annotations #array of faces detected
    if len(face_annotations) > 0:
        face = face_annotations[0] #get only one face detected
        #return likely emotion (there's also sorrow and surprise)
        if str(face.joy_likelihood) == 'Likelihood.LIKELY' or str(face.joy_likelihood) == 'Likelihood.VERY_LIKELY':
            return 'happy'
        elif str(face.anger_likelihood) == 'Likelihood.LIKELY' or str(face.anger_likelihood) == 'Likelihood.VERY_LIKELY':
            return 'angry'
        elif str(face.sorrow_likelihood) == 'Likelihood.LIKELY' or str(face.sorrow_likelihood) == 'Likelihood.VERY_LIKELY':
            return 'sad'
        elif str(face.surprise_likelihood) == 'Likelihood.LIKELY' or str(face.surprise_likelihood) == 'Likelihood.VERY_LIKELY':
            return 'surprised'
        else:
            return 'could not detect emotion'
    else: #no faces detected
        return 'could not detect face'

def get_writing(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image) #full response from Google cloud vision
    text = response.full_text_annotation.text #text detected
    if text:
        return text
    else:
        return 'could not detect text'

def get_image_from_frame(cap):
    ret, frame = cap.read()
    file = 'frame.png'
    cv2.imwrite(file,frame)
    cv2.imshow('frame',frame) #show camera output
    return file

def see_obj(obje):
    from stage_3_simple import see_object
    see_object(obje)

def start_camera():#capture camera feed
    cap = cv2.VideoCapture(0)
    while True:
        img = get_image_from_frame(cap)
        key = cv2.waitKey(0) #press 0 to move through frames
        if key == ord('q'): #press q to quit
            break
        elif key == ord('e'): #press e to detect emotion in current frame
            emotion = get_emotion(img)
            my_raspimon.see_emotion(emotion)
        elif key == ord('y'): #press y to detect object in current frame
            obj = get_object(img)
            my_raspimon.see_object(obj)
        elif key == ord('w'): #press w to detect writing in current frame
            text = get_writing(img)
            my_raspimon.see_writing(text)
    cap.release()
    cv2.destroyAllWindows()