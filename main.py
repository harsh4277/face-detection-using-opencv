from flask import Flask, render_template, request
from upload_photo import upload_photo
from photo_search import search_photos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded photo and get its path
            photo_path = upload_photo(file)
            
            # Search for similar photos in albums
            result = search_photos(photo_path)
            
            return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
