import cv2
import os

def search_photos(photo_path):
    # Load the uploaded photo
    uploaded_photo = cv2.imread(photo_path)

    # Define the directory containing the albums
    albums_folder = 'albums'

    # Initialize a list to store matching photos
    matching_photos = []

    # Loop through each album
    for album_name in os.listdir(albums_folder):
        album_path = os.path.join(albums_folder, album_name)

        # Loop through each photo in the album
        for photo_name in os.listdir(album_path):
            photo_path = os.path.join(album_path, photo_name)
            album_photo = cv2.imread(photo_path)

            # Convert both images to grayscale for face detection
            uploaded_gray = cv2.cvtColor(uploaded_photo, cv2.COLOR_BGR2GRAY)
            album_gray = cv2.cvtColor(album_photo, cv2.COLOR_BGR2GRAY)

            # Load a pre-trained face detector (Haar cascades)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Detect faces in the uploaded photo
            uploaded_faces = face_cascade.detectMultiScale(uploaded_gray, scaleFactor=1.1, minNeighbors=5)

            # Detect faces in the album photo
            album_faces = face_cascade.detectMultiScale(album_gray, scaleFactor=1.1, minNeighbors=5)

            # Compare the number of detected faces in both photos
            if len(uploaded_faces) == len(album_faces):
                # Add the album photo to matching photos list
                matching_photos.append(photo_path)

    return matching_photos
