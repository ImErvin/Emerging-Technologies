from flask import Flask
from flask import request
from flask import json 
from flask import jsonify

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

@app.route('/image', methods=['GET','POST'])
def uploadImage():
    image = Image("blah blah blah", "blah blah blaah", "blah blah blahhh")
    return json.dumps(image.serialize())


#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()