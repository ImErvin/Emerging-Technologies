# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin

import keras as kr
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers import Flatten, Dense
(training_images, training_labels), (testing_images, testing_labels) = mnist.load_data()
print("How many values in a training image?", len(training_images[7]) * len(training_images[7][0]))
print("What the 8th training image looks like:")
print(training_images[7])
print()
print("What the 8th training image looks like as a sequence of dots and hashes:")
for x in training_images[7]:
    print()
    for y in x:
        if(y != 0):
            print("#", end="")
        else:
            print(".", end="")
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
model = Sequential()
model.add(Convolution2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28, 28,1 )))
print("Model Input Shape @ Conv Layer:",model.input_shape)
print("Model Output Shape @ Conv Layer:",model.output_shape,"<--- Changed by Convolution layer")
model.add(Convolution2D(32, kernel_size=(3, 3),activation='relu'))
print("Model Input Shape @ Conv Layer 2:",model.input_shape)
print("Model Output Shape @ Conv Layer 2:",model.output_shape,"<--- Changed by Convolution layer")
model.add(MaxPooling2D(pool_size=(2, 2)))
print("Model Input Shape @ Pooling layer:",model.input_shape)
print("Model Output Shape @ Pooling layer:",model.output_shape,"<--- Changed by Max Pool")
model.add(Flatten())
print("Model Input Shape @ Flatten layer:",model.input_shape)
print("Model Output Shape @ Flatten layer:",model.output_shape,"<--- Changed by Flatten")
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.summary()
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(training_images_rs, training_labels_cats, batch_size = 128, epochs = 20, verbose = 1, validation_split = 0.1)
evaluation = model.evaluate(training_images_rs, training_labels_cats, verbose=1)
print('Test loss:', evaluation[0])
print('Test accuracy:', evaluation[1]*100,"%")
model.save('mnist_cnn.h5')
