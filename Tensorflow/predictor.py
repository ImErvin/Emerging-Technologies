# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin

# Adapted code from -
# [1] Live fitting of the model - https://github.com/fchollet/keras/issues/1868

# Import numpy to use np.around and np.expand_dims for prediction
import numpy as np
# Use keras.models to import a model
from keras.models import load_model
# Import Keras to work the model
import keras as kr

# load the model in using Keras's load_model function
model = load_model("Tensorflow/updated_mnist_cnn.h5")

# To handle the live training I must use the SGD Optimiser 
sdg = kr.optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)
# Recompile with new optimiser
model.compile(optimizer=sdg, loss="categorical_crossentropy", metrics=["accuracy"])


# Function to reshape data into (1,28,28,1) to use with convolution layers
def reshapeData(array):
    # .reshape will reshape the array and format each value as a float
    array = array.reshape(1,28,28,1).astype("float32")
    
    # Return reshaped data.
    return array

def makePrediction(rgbValArray):
    # Reshape the numpy array to fit into the convolution2d model, i'm using .reshape to add 2 extra dimensions
    # because my Conv2d layer expects a 4 dimensional array
    rgbValArray_rs = reshapeData(rgbValArray)

    # Make a prediction by feeding in the rgb value array and the output of this will be the result from the softmax function.
    prediction = model.predict(rgbValArray_rs).astype(np.int)[0]

    # Convert back to integer from binary class matrix
    prediction = np.argmax(prediction, axis=0)

    # Return the prediction
    return prediction

def train(input_image, output_label):
    # Reshape the image array
    input_image_rs = reshapeData(input_image)

    # Turn the output label into a binary class matrix
    output_label_cats = kr.utils.to_categorical(output_label,  num_classes=10)

    # Normalize the data by diving every value by 255 - resulting in a number between 0-1
    input_image_rs /= 255

    # Train the model for that 1 image using default settings
    model.fit(input_image_rs, output_label_cats, verbose=0)

    # Save the model to be loaded in next session
    model.save("Tensorflow/updated_mnist_cnn.h5")