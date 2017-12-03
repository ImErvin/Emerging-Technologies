# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin

# Import numpy to use np.around and np.expand_dims for prediction
import numpy as np
# Use keras.models to import a model
from keras.models import load_model
import keras as kr

# load the model in using Keras's load_model function
model = load_model("Tensorflow/mnist_cnn.h5")



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
    print("\n Prediction:",prediction)

    return prediction

def train(input_image, output_label):

    input_image_rs = reshapeData(input_image)
    print(input_image_rs)
    output_label_cats = kr.utils.to_categorical(output_label,  num_classes=10)
    print(output_label_cats)
    # Normalize the data by diving every value by the highest one
    input_image_rs /= np.max(input_image_rs)
    #model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    model.fit(input_image_rs, output_label_cats, verbose=0)
    evaluation = model.evaluate(input_image_rs, output_label_cats, verbose=0)

    # Display evaluation metrics
    #print('Test loss:', evaluation[0],'Test accuracy:', evaluation[1]*100,"%")

    model.save("Tensorflow/updated_mnist_cnn.h5")

#makePrediction(x_train[20])