import os
import flask
from flask import Flask, request, redirect, url_for, json, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Image(object):
    imageName = ""
    details = ""
    prediction = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, imageName, details, prediction):
        self.imageName = imageName
        self.details = details
        self.prediction = prediction
    
    def serialize(self):
        return{
            'imageName': self.imageName,
            'details': self.details,
            'prediction:': self.prediction,
        }


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploadImage', methods=['POST'])
def upload_image():


@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/image/<imageUrl>', methods=['GET','POST'])
def uploadImage(imageUrl):
    if flask.request.method == 'POST':
        return json.dumps(imageUrl)
    else:
        image = Image("blah blah blah", "blah blah blaah", "blah blah blahhh")
        if(imageUrl):
            return json.dumps(imageUrl)
        else:
            return json.dumps(1)
        

@app.route('/user_download')
def user_download():
    url = request.args['url']  # user provides url in query string
    r = requests.get(url)

    # write to a file in the app's instance folder
    # come up with a better file name
    with app.open_instance_resource('downloaded_file', 'wb') as f:
        f.write(r.content)

#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()