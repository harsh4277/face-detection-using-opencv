import os
from image_utils import save_temporary_image

def upload_photo(file):
    if file:
        # Save the uploaded photo to a temporary folder
        temp_folder = 'temp_photos'
        os.makedirs(temp_folder, exist_ok=True)
        temp_photo_path = os.path.join(temp_folder, file.filename)
        file.save(temp_photo_path)
        return temp_photo_path
