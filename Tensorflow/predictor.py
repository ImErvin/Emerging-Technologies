# 808 - Handwritten Recognition. Written by Ervin Mamutov - github.com/imervin

# Use keras.models to import a model
from keras.models import load_model

# load the model in using Keras's load_model function
model = load_model("mnist_cnn.h5")

# Prints out the same model architecture as the one i've created in the jupyter notebook 
# meaning it loads the model successfully
model.summary()
