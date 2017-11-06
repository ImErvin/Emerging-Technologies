from flask import Flask
from flask import request
from flask import json 

app = Flask(__name__)

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

@app.route('/image', methods=['GET','POST'])
def uploadImage():
    return json.dumps("hey")


#Main method.
if __name__ == "__main__":  
    #Run the app.
    app.run()