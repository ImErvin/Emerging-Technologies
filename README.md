## Emerging Technologies Project
###### Written by Ervin Mamutov

For my emerging technologies module in college I built this application and named it 808. The specification of the project was to be to train a Neural Network(NN) using a popular library such as Tensorflow and use that trained NN to predict the what number is present on a file passed in from a front end web application.

This repository holds my solution to this project specification. This README shows you how to install the repository, the technologies I used, the features of my web application, the architecture of my files and some personal notes of my experience building this application. If you're looking for more detailed explanations on the code, check out my [Jupyter Notebook](https://github.com/ImErvin/Emerging-Technologies/blob/master/Tensorflow/mnist_model_training.ipynb) and any other code files (.py .js .html) for the comments.

### How to use this repository

1. Ensure you have Python 3.x, Jupyter, Tensorflow, Keras, Numpy and Git installed locally. (I'd recommend using Anaconda to install the python packages required to run this.)
2. Enter the following commands into your command line.
```bash
# Change directory to anywhere you desire
cd anywhere..

# Clone this repository using git
git clone https://github.com/ImErvin/Emerging-Technologies.git
cd Emergin-Technologies

# Install the node_modules using npm install
npm install

# Run the server
py app.py

# Now open your browser on localhost/5000 (For best results - use a modern browser)

```

### Thechnologies Used
The technologies I'm using in this project are:
1. Python
2. CSS/HTML/Javascript
3. Tensorflow with Keras
4. AngularJS
5. Bootstrap v4 - The latest as of Dec 2017
6. Flask

The reasoning behind the back-end technologies ( Python, Keras, Flask ) is outline is my notebooks - open my repositories and look out for the 📔 emoji. These are the problem-sheets I have done for this module and they contain a lot of the explanation about these technologies (Except for flask, I'm using flask because i've used it before and I needed to spin up a quick prototype). The reasoning behind the front-end technologies ( CHJS, Angular and Bootstrap ) is because I wanted to create an aesthetic front-end that is fully responsive and dynamic and what better technologies than the ones I have listed?!

### Features 
808 offers the following features
1. Upload an image from local files
2. Draw and upload an image from a HTML5 Canvas
3. Make a prediction on the uploaded file stated in 1. and 2.
4. Allow the user to train the model by providing feedback on the prediction
5. Display the amount of times the model has been trained by users

### Architecture
#### Front-End
The architecture of my front end is a basic MVC built in Angular which is made available using <scripts> in my index.html. I have one main view (index.html), one main controller (controllers.js) and one main model (services.js) - the idea is to have the controller provide functionality to the view as well as ating as a bridge between the view and the model. I used NPM to describe my application and add front-end dependencies (bootstrap, angular, animate.css, font-awesome).

#### Back End
The architecture of my back end is a basic back-end-esque design. I have a Flask acting as an API that processes and returns JSON supplied from my Model on the front end. I used a Jupyter Notebook to design and explain my model - I really enjoyed using Jupyter Notebook during the semester and decided this would be a great way to get a create the model all while justifying my code. 

My Jupyter Notebook sits in the directory named "Tensorflow", in that same directory you will find the raw code from my model (incase you don't want to ready all the explanations), a text-file named editedCount.txt, this is my local database for storing the amount of times the model as been train (displayed on the front end for extra features) and a python file named predictor which provides the flask API with functionality to predict on a model/ train the model and get/set the "local storage" file. 

I also have a copy of the original "model_cnn.h5" This was the model I train initially and a copy of "updated_mnist_cnn.h5" - This is the model that gets updated when users provide feedback on predictions.

### Conclusion
I thoroughly enjoyed working with neural networks - I feel like having done this project I can confidently say that I understand the absolute basics of the big world of machine learning. Not only that but I really enjoyed working with Python especially because any problem I encountered was solvable a click away. 

My personal aim of this project was to get to a good level of knowledge on neural network, I wanted to acquire the know-how to be able to develop my own out of college projects using neural networks. I also wanted to be able to train a model in real-time.

If I were to do this project again, I'd consider adding some extra features such as training another model with the CIFAR-10 dataset and allowing users to alter between hand-drawn images to images of trucks for example. I would also play around with the layers in my neural network and play around with some dropouts to take care of any overfittings that may happen on my current NN.

### Screenshots
**Homescreen**
![Homescreen](https://github.com/ImErvin/Emerging-Technologies/blob/master/uploads/8081.png)

**Canvas upload and prediction**
![Canvas](https://github.com/ImErvin/Emerging-Technologies/blob/master/uploads/8082.png)

**Correct prediction feedback**
![Correct prediction feedback](https://github.com/ImErvin/Emerging-Technologies/blob/master/uploads/8083.png)

**Incorrect prediction feedback**
![Incorrect prediction feedback](https://github.com/ImErvin/Emerging-Technologies/blob/master/uploads/8084.png)

**Responsive Design**
![Responsive](https://github.com/ImErvin/Emerging-Technologies/blob/master/uploads/8085.png)
