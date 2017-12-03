# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin

# Import numpy to use np.around and np.expand_dims for prediction
import numpy as np
# Use keras.models to import a model
from keras.models import load_model

# load the model in using Keras's load_model function
model = load_model("Tensorflow/mnist_cnn.h5")

# Prints out the same model architecture as the one i've created in the jupyter notebook 
# meaning it loads the model successfully
# model.summary()

def makePrediction(rgbValArray):
    # Reshape the numpy array to fit into the convolution2d model, i'm using .reshape to add 2 extra dimensions
    # because my Conv2d layer expects a 4 dimensional array
    rgbValArray = rgbValArray.reshape(1,28,28,1)

    # Make a prediction by feeding in the rgb value array and the output of this will be the result from the softmax function.
    prediction = model.predict(rgbValArray).astype(np.int)[0]
    print("\n",prediction)
    return prediction

def train(input_image, output_label):
    return input_image

#makePrediction(x_train[20])