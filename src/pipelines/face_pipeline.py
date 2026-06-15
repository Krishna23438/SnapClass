import dlib
import numpy as np
import face_recognition_models 
from sklearn.svm import SVC 
import streamlit as st

from src.database.db import get_all_students

@st.cache_resource  #it makes to run only one time bcz for big function contains big data consumes big time
def load_dlib_models():
  detector = dlib.get_frontal_face_detector()  #it gives the no of faces and their positions in the picture

  sp = dlib.shape_predictor(
    face_recognition_models.pose_predictor_model_location
  )

  facerec = dlib.face_recognition_model_v1(
    face_recognition_models.face_recognition_model_location()
  )

  return detector, sp, facerec

def get_face_embeddings(image_np):
  detector, sp, facerec = load_dlib_models()
  faces  = detector(image_np, 1)

  encodings = []

  for face in faces:
    shape = sp(image_np, face)
    face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1) #128 embedding

    encodings.appen(np.array(face_descriptor))
  return encodings

@st.cache_resource
def get_trained_model():
  X = []
  y = []

  student_db  = get_all_students()

  if not student_db:
    return False
  
  for student in student_db:
    embedding = student.get('face_embedding')
    if embedding:
      X.append(np.array(embedding))
      y.append(student.get('student_id'))

  if len(X) == 0:
    return 0
  clf = SVC(kernel='linear',probability=True, class_weight='balanced')

  try:
    clf.fit(X,y)
  except ValueError:
    pass

  return {'clf':clf, 'X':X, 'y':y}


def train_classifier():
  st.cache_resource.clear()
  model_data = get_trained_model()
  return bool(model_data)

def predict_attendance(class_image_np):
  encodings = get_face_embeddings(class_image_np)

  detect_student = {}

  model_data = get_trained_model()

  if not model_data:
    return detect_student, [], len(encodings) # we return 1.the values of students/their embeddings, 2.lists of students 3.No. of students
  
  clf = model_data['clf']
  X = model_data['X']
  y_train = model_data['y']

  all_students = sorted(list(set(y_train)))