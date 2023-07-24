# You can add utility functions related to image processing here, if needed.
import os
import uuid
from PIL import Image

def save_temporary_image(file):
    # Generate a unique filename for the temporary image
    temp_folder = 'temp_photos'
    os.makedirs(temp_folder, exist_ok=True)
    filename = f"{str(uuid.uuid4())}.jpg"
    temp_photo_path = os.path.join(temp_folder, filename)

    # Save the uploaded photo to the temporary folder
    image = Image.open(file)
    image.save(temp_photo_path)

    return temp_photo_path
