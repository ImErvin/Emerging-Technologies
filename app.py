# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin


# Adapted Code From -
#   [1] Regular Expression Delete everything before - https://stackoverflow.com/questions/7793950/regex-to-remove-all-text-before-a-character
#   [2] Reading byte array into image on the fly- 
#   [3] Resizing image using PIL - https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

# Import flask and helpful flask libraries
import flask
from flask import Flask, request, json, abort

# Import Python's Image Library to resize images
import PIL.Image
import io

# Import base64 to work with base64 encoded images
import base64

# Import re to use Regular Expressions
import re

app = Flask(__name__)

# This class is used to mimic the "rendered" object on the front end.
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
    
    # Create serialize function to serialize the data to be be sent as JSON.
    def serialize(self):
        return{
            'fileName':self.fileName,
            'message':self.message,
            'icon':self.icon,
            'bgColor':self.bgColor,
            'prediction':self.prediction,
        }

# Function to resize an image from a byte array
def resizeImage(byteArray, fileName):
    # Use PIL to extract the image from the bytearray
    image = PIL.Image.open(io.BytesIO(byteArray))

    # Try out all the resize filters to see which works best.
    # nearestRS = image.resize((28,28), PIL.Image.NEAREST)
    # bilinearRS = image.resize((28,28), PIL.Image.BILINEAR)
    # bicubicRS = image.resize((28,28), PIL.Image.BICUBIC)
    # lanczosRS = image.resize((28,28), PIL.Image.LANCZOS)

    # nearestRS.save("uploads/nearestRS.png")
    # bilinearRS.save("uploads/bilinearRS.png")
    # bicubicRS.save("uploads/bicubicRS.png")
    # lanczosRS.save("uploads/lanczosRS.png")

    # After trying each filter out using canvas and upload from file
    # Nearest performed the worst in both canvas and file
    # Cubic performed the best with canvas images and file - they all kind of tied.
    # So through trial and error I decided to use bicubic
    
    # Apply the resize using PIL's .resize with the Bicubic filter
    bicubicRS = image.resize((28,28), PIL.Image.BICUBIC)
    # Save the output as 
    bicubicRS.save("uploads/"+fileName)
    

# Root hosts the index.html file
@app.route('/')
def homepage():
    return app.send_static_file('index.html')

# /uploadImage route is used to save an image file locally
@app.route('/uploadImage', methods=['POST'])
def uploadImage():
    if flask.request.method == 'POST':
        data = request.json # Read the request.data (JSON from requqest)

        if(data['imageBase64'] != 'undefined'):
            # The value of the imageBase64 key in the dictionary results in something like "data:image/png;base64,iVBOR.."
            # I just want the "iVBOR.." part of the result above so I use a regular expression to remove everything before the ','.
            dataRegex = re.sub('^[^_]*,', '', str(data['imageBase64'])) # [1]
            #print(data)
            # The above regular expression turned the base64 byte data from byte-like object to string.
            # To use the base64.decodebytes function below, I must encode the string into bytes again.
            dataRegex = str.encode(dataRegex)

            # Call resizeImage and pass in the decoded image byte array
            resizeImage(base64.decodebytes(dataRegex), data['imageFileName'])

            image = Image(data['imageFileName'], "Image was saved successfully", "fa fa-thumbs-up text-dark", "badge badge-warning", "9")

            return json.dumps(image.serialize())
        else:
            abort(500)
        

@app.errorhandler(500)
def internal_error(error):
    return json.dumps('Error loading image - ensure you have attached an image file'), 500


#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()