import keras as kr #importing keras
import numpy as np #importing numpy
# Use keras's dataset mnist
from keras.datasets import mnist
# Import all necessary libraries for models
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers import Flatten, Dense

# Initiate two tuples, the first with uint8 array of grayscale image data, the other with integers between 0-9
(training_images, training_labels), (testing_images, testing_labels) = mnist.load_data()

print("How many values in a training image?", len(training_images[7]) * len(training_images[7][0]))
print("What the 8th training image looks like:")
print(training_images[7])
print()
print("What the 8th training image looks like as a sequence of dots and hashes:")
# Visualize a training image by printing out it's RGB value as a #
for x in training_images[7]:
    print()
    for y in x:
        if(y != 0):
            print("#", end="")
        else:
            print(".", end="")

# Print out the shapes of the images and set variables values to the shapes
print("Training/testing Images shape:",training_images.shape,"/",testing_images.shape)
print("Training/testing Labels shape:",training_labels.shape,"/",testing_labels.shape)
print("First 5 training labels and testing labels:", training_labels[:5], "/", testing_labels[:5])

no_rows = training_images.shape[1]
no_cols = training_images.shape[2]

print("There are",no_rows,"rows and",no_cols,"columns in an image")

training_images_rs = training_images.reshape(training_images.shape[0],28,28,1).astype("float32")
print("Training images shape after reshape =",training_images.shape)
testing_images_rs = testing_images.reshape(testing_images.shape[0],28,28,1).astype("float32")
print("Testing images shape after reshape =",testing_images_rs.shape)

print("Maximum value in our training/testing images =", np.max(training_images_rs),np.max(testing_images_rs))
print("Maximum value in training images before normalization:", np.max(training_images_rs))

training_images_rs /= 255
testing_images_rs /= 255

print("Maximum value in training images after normalization:", np.max(training_images_rs))

training_labels_cats = kr.utils.to_categorical(training_labels,  num_classes=10)
testing_labels_cats = kr.utils.to_categorical(testing_labels,  num_classes=10)

print("The figure",training_labels[500],"is represented as",training_labels_cats[500],"after one-hot encoding")

# Stacked layer model
model = Sequential()
# Add convolution2d layer 32 inputs, kernel size of 3x3 - activation = relu
model.add(Convolution2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28, 28,1 )))
print("Model Input Shape @ Conv Layer:",model.input_shape)
print("Model Output Shape @ Conv Layer:",model.output_shape,"<--- Changed by Convolution layer")
# Add another convolution2d layer 32 inputs, kernel size of 3x3 - activation = relu
model.add(Convolution2D(32, kernel_size=(3, 3),activation='relu'))
print("Model Input Shape @ Conv Layer 2:",model.input_shape)
print("Model Output Shape @ Conv Layer 2:",model.output_shape,"<--- Changed by Convolution layer")
# Add a MaxPooling2D pooling layer with pool size of 2x2
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Model Input Shape @ Pooling layer:",model.input_shape)
print("Model Output Shape @ Pooling layer:",model.output_shape,"<--- Changed by Max Pool")
# Flatten the data - (,12,12,32) into (,4608) - multiply each dimension to create 1 dimension only.
model.add(Flatten())
print("Model Input Shape @ Flatten layer:",model.input_shape)
print("Model Output Shape @ Flatten layer:",model.output_shape,"<--- Changed by Flatten")
# Add a hidden layer to process flattened image with relu Activation
model.add(Dense(128, activation="relu"))
# Add an output layer with softmax activation
model.add(Dense(10, activation="softmax"))

model.summary()

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(training_images_rs, training_labels_cats, batch_size = 128, epochs = 20, verbose = 1, validation_split = 0.1)

evaluation = model.evaluate(training_images_rs, training_labels_cats, verbose=1) # Evaluate the trained model on the test set!

print('Test loss:', evaluation[0])
print('Test accuracy:', evaluation[1]*100,"%")

model.save(mnist_cnn.h5)
