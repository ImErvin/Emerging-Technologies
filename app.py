# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin


# Adapted Code From -
#   [1] Regular Expression Delete everything before - https://stackoverflow.com/questions/7793950/regex-to-remove-all-text-before-a-character
#   [2] Regular Expression Delete everything after - https://stackoverflow.com/questions/19367373/regex-for-remove-everything-after-with
#   []

import os
import flask
from flask import Flask, request, redirect, url_for, json, jsonify
from werkzeug.utils import secure_filename
import base64
from base64 import decodestring
import re

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class Image(object):

    fileName = "" # Name of the file being uploaded
    message = "" # The message shown to the user e.g: Successful upload etc.
    icon = "" # The icon for the message above (used for UX on the front end). E.g: "fa fa-thumbs" for a thumbs up
    bgColor = "" # Set the background color of the message above (again mainly for UX). E.g: "bg-danger" to indicate an error.
    prediction = "" # This is the prediction from Tensorflow

    # Create a constructor for the class 
    def __init__(self, fileName, message, icon, bgColor, prediction):
        self.fileName = fileName
        self.message = message
        self.icon = icon
        self.bgColor = bgColor
        self.prediction = prediction
    
    def serialize(self):
        return{
            'fileName':self.fileName,
            'message':self.message,
            'icon':self.icon,
            'bgColor':self.bgColor,
            'prediction':self.prediction,
        }


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/uploadImage', methods=['POST', 'GET'])
# def upload_image():
#     # if request.method == 'POST':
#     #     # check if the post request has the file part
#     #     if 'file' not in request.files:
#     #         flash('No file part')
#     #         return redirect(request.url)
#     #     file = request.files['file']
#     #     # if user does not select file, browser also
#     #     # submit a empty part without filename
#     #     if file.filename == '':
#     #         flash('No selected file')
#     #         return redirect(request.url)
#     #     if file and allowed_file(file.filename):
#     #         filename = secure_filename(file.filename)
#     #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     #         #return redirect(url_for('uploaded_file', filename=filename))
#     if request.method == 'POST':
#         return request.get_json()
#     else:
#         return request.method

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/uploadImage', methods=['GET','POST'])
def uploadImage():
    if flask.request.method == 'POST':
        data = request.json # Read the request.data (JSON from requqest)
        print(data)
        # The value of the imageBase64 key in the dictionary results in something like "data:image/png;base64,iVBOR.."
        # I just want the "iVBOR.." part of the result above so I use a regular expression to remove everything before the ','.
        dataRegex = re.sub('^[^_]*,', '', str(data['imageBase64'])) # [1]

        # The above regular expression turned the base64 byte data from byte-like object to string.
        # To use the base64.decodebytes function below, I must encode the string into bytes again.
        dataRegex = str.encode(dataRegex)

        with open('uploads/'+data['imageFileName'], "wb") as fh:
            fh.write(base64.decodebytes(dataRegex))
        
        image = Image(data['imageFileName'], "Image was saved successfully", "fa fa-thumbs-up text-dark", "bg-success", "9")

        return json.dumps(image.serialize())
    else:
        image = Image("sampleImage.jpg", "Image was processed successfully.", "fa fa-thumbs-up text-dark", "bg-success","9")
        return json.dumps(image)
        

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