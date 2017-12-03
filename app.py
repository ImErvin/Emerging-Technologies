# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin


# Adapted Code From -
#   [1] Regular Expression Delete everything before - https://stackoverflow.com/questions/7793950/regex-to-remove-all-text-before-a-character
#   [2] Reading byte array into image on the fly - https://stackoverflow.com/questions/18491416/pil-convert-bytearray-to-image
#   [3] Resizing image using PIL - https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
#   [4] Convert image to grayscale - https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
#   [5] Use numpy to retrieve RGB values - https://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
#   [6] Retrieve first index of an array - https://stackoverflow.com/questions/30062429/python-how-to-get-every-first-element-in-2-dimensional-list

# Import flask and helpful flask libraries
import flask
from flask import Flask, request, json, abort

# Import Python's Image Library to resize images and io to read bytes
import PIL.Image
import io

# Numpy to work with arrays
import numpy as np

# Import base64 to work with base64 encoded images
import base64

# Import re to use Regular Expressions
import re

# Import my local python files to use prediction and training
from Tensorflow.predictor import makePrediction, train, getNoTrained

# Init app as flask
app = Flask(__name__)

# This class is used to mimic the "rendered" object on the front end.
class Image(object):

    fileName = "" # Name of the file being uploaded
    prediction = "" # This is the prediction from Keras

    # Create a constructor for the class 
    def __init__(self, fileName, prediction):
        self.fileName = fileName
        self.prediction = prediction
    
    # Create serialize function to serialize the data to be be sent as JSON.
    def serialize(self):
        return{
            'fileName':self.fileName,
            'prediction':self.prediction,
        }

# Function to resize an image from a byte array
def resizeImage(byteArray):
    # Use PIL to extract the image from the bytearray
    image = PIL.Image.open(io.BytesIO(byteArray)) # [2]

    # After trying each filter out using canvas and upload from file
    # Nearest performed the worst in both canvas and file
    # Cubic performed the best with canvas images and file - they all kind of tied.
    # So through trial and error I decided to use bicubic
    # Apply the resize using PIL's .resize with the Bicubic filter
    bicubicRS = image.resize((28,28), PIL.Image.BICUBIC) # [3]

    # Convert the into grayscale to reduce its channel to 1 dimension (1 rgb value for each pixel)
    bicubicRS = bicubicRS.convert('LA') # [4]

    # Now I want to retrieve the RGB values of each pixel in the image
    # I'm using numpys asarray to convert the image to an array and reading each value as an int32
    rgbValueArray = np.asarray( bicubicRS, dtype="int32" ) #[5]

    # I just need it to be (28,28), so I will create a new array by retrieving the first index of the (2) part of that shape
    rgbValueArray_spliced = [[y[0] for y in x] for x in rgbValueArray] #[6]

    # Convert it to a numpy array
    rgbValueArray_spliced = np.array(rgbValueArray_spliced)

    return rgbValueArray_spliced

# Function is used to decode base64 into byte array
def extractB64(b64String):
    # The value of the imageBase64 key in the dictionary results in something like "data:image/png;base64,iVBOR.."
    # I just want the "iVBOR.." part of the result above so I use a regular expression to remove everything before the ','.
    dataRegex = re.sub('^[^_]*,', '', str(b64String)) # [1]

    # The above regular expression turned the base64 byte data from byte-like object to string.
    # To use the base64.decodebytes function below, I must encode the string into bytes again.
    dataRegex = str.encode(dataRegex)

    # Return the decoded bytes
    return base64.decodebytes(dataRegex)

# Root hosts the index.html file
@app.route('/')
def homepage():
    return app.send_static_file('index.html')

# /postImage route is used to recieve base64 encoded images
@app.route('/postImage', methods=['POST'])
def postImage():
    if flask.request.method == 'POST':
        data = request.json # Read the request.data (JSON from requqest)

        if(data['imageBase64'] != 'undefined'):
            # Call resizeImage and pass in the decoded image byte array
            # This will resize and convert the image into a numby array to make a prediction on.
            # Passing in a decoded byte array from base64.
            imageArray = resizeImage(extractB64(data['imageBase64']))

            # Make a prediction by passing the image array into the predictor function
            prediction = makePrediction(imageArray)

            # Build the image dictionary to send back as JSON
            image = Image(data['imageFileName'], str(prediction))

            # Serialize the image dict and send it as JSON
            return json.dumps(image.serialize())

# /postFeedback route is used to recieve the feedback on the prediction and train the model using the new input/output data
@app.route('/postFeedback', methods=['POST'])
def postFeedback():
    if flask.request.method == 'POST':
        # Init data as the json that is being passed in
        data = request.json
        
        if(data['imageBase64'] != 'undefined'):
            # Call resizeImage and pass in the decoded image byte array
            # This will resize and convert the image into a numby array to make a prediction on.
            # Passing in a decoded byte array from base64.
            imageArray = resizeImage(extractB64(data['imageBase64']))
            
            # Call the train method and pass in the input (imageArray) and output (data value)
            count = train(imageArray, data['outputValue'])
            
            # 
            return json.dumps(count)

# /getNoTrained is used to retrieve the amount of times the model has been trained by users
@app.route('/getNoTrained', methods=['GET'])
def returnNoTrained():
    # Use predictors getNoTrained method to return the number saved in the editedCount file.
    count = getNoTrained()

    # Return count as JSON
    return json.dumps(count)

#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()