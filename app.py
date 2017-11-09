from flask import Flask
from flask import request
from flask import json 
from flask import jsonify
import flask
import requests

app = Flask(__name__)

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