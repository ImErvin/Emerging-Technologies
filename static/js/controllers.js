// Create controllers module
angular.module('app.controllers', [])

// Single controllers called main controller implements $scope and APIFactory
.controller('mainCtrl', function($scope, APIFactory) {
    // Declare variables 
    var uploadOption = [true,false]; // 0 from URL, 1 from File, 2 from Canvas
    var rendered = { // Object that mimics the dict on python side.
        fileName: null,
        prediction: null,
    };
    var feedbackButtons = true; // Used to display/hide the feedback buttons
    var predictionCorrection = false; // Used to display/hide the buttons 0-9 to correct the prediction
    var feedbackSent = false; // Used to catch when feedback is sent to display message
    var imageFile; // This is used to catch the base64 of the input file on html
    var displayImageFile; // This is used to display the image from input and canvas 
    var canvasTouched = false; // This is used for error handling ensuring people don't send up black canvases
    var message; // This is the error message if users don't upload file or draw on canvas
    var noTrained = null; // This is to display the amount of times the model has been trained

    // Retrieve the amount of times the model has been trained on loadup
    APIFactory.request.getNoTrained().then(function(data){
        $scope.noTrained = data.data;
    });

    // Set the canvas height
    var canvas = document.getElementById("drawImageCanvas");
    var ctx = canvas.getContext("2d");
    canvas.height = canvas.height+100;

    // Function to reset the canvas
    function setUpCanvas(){
        ctx.fillStyle = "Black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    
    // Function to handle if the user sees file input card or canvas card
    function uploadOptionSelected(uploadoption){
        console.log(uploadoption);
        $scope.message = undefined;
        switch(uploadoption){
            case 0:
                $scope.uploadOption = [true,false]; // Show file input card
                break;
            case 1:
                setUpCanvas(); // reset canvas
                $scope.canvasTouched = false; // set canvas to pristine
                $scope.uploadOption = [false, true]; // Show canvas input card
                break;
            default:
                $scope.uploadOption = [true,false]; // Show file input card
                break;
        }
    }

    // Function to handle upload from file input
    function uploadFromFile(){
        if($scope.imageFile){
            // Set file to the object the directive sets it to - base64 and filename
            var file = $scope.imageFile
            // Pass file into uploadImage
            uploadImage(file);
            // Reset message
            $scope.message = undefined;
        }else{
            // Warn the user they need to upload an image before uploading
            $scope.message = "Upload an image before uploading!"
        }
        
    }

    // Function to handle upload from canvas
    function uploadFromCanvas(){
        // Check to see if the canvas has been touched
        if($scope.canvasTouched){
            // Conver the canvas image into b64
            var pngUrl = canvas.toDataURL();
            // Set file to the object - base64 and file name
            var file = {
                imageBase64: pngUrl,
                imageFileName: "CanvasImage.png"
            }
            // Pass file into uploadImage
            uploadImage(file);
            // Reset message
            $scope.message = undefined;
        }else{
            // Warn the user they must draw on the canvas first
            $scope.message = "Draw on the canvas before uploading!"
        }
        
    }

    // Function to send the file data to the server by calling the api service
    function uploadImage(file){
        // Reset the feedback buttons etc.
        resetFeedback();
        
        // Invoke the api service by passing file into postImage - once the promise is returned
        // set the display image to the base64 of the file sent up and set rendered to the data returned from server
        APIFactory.request.postImage(file).then(function(data) {
            $scope.displayImageFile = file.imageBase64;
            $scope.rendered = data.data;
        });
    }

    // Function to send the feedback to the server by calling the api service
    function uploadFeedback(outputvalue, base64){
        // Create the feedback object on the controller side - this object mimics the one on python
        var feedback = {
            outputValue: outputvalue,
            imageBase64: base64
        }
        // Invoke the api service by passing file into postImage - once the promise is returned
        // set the amount of times trained to the data returned.
        APIFactory.request.postFeedback(feedback).then(function(data){
            $scope.noTrained = data.data;
        });;
    }

    // Function to handle the ng-show/ng-hide of the feedback stuff
    function feedback(correct){
        // If the prediction is correct
        if(correct){
            $scope.feedbackButtons = false; // Hide buttons
            $scope.feedbackSent = true; // Show final feedback message

            // Send the input and output to uploadFeedback , if it's correct we can assume the prediction is the output.
            uploadFeedback($scope.rendered.prediction, $scope.displayImageFile)
        }else{
            // Else hide the buttons and show the next step of feedback correction.
            $scope.feedbackButtons = false;
            $scope.predictionCorrection = true;
        }
    }

    // Function to catch the actual number of the file
    function actualNumberFeedBack(number){
        // Hide everything else and show final message
        $scope.predictionCorrection = false;
        $scope.feedbackSent = true;

        // Send the input and output to uploadFeedback , the number passed in is the output.
        uploadFeedback(number, $scope.displayImageFile);   
    }

    // Reset the feedback state - this is invoked everytime a new image is uploaded
    function resetFeedback(){
        $scope.feedbackButtons = true;
        $scope.predictionCorrection = false;
        $scope.feedbackSent = false;
        $scope.predictionCorrection = false;
    }


    // Use the functions and variables in my view by adding a $scope prefix to enable observation.
    $scope.uploadFromFile = uploadFromFile;
    $scope.uploadFromCanvas = uploadFromCanvas;
    $scope.uploadOption = uploadOption;
    $scope.uploadOptionSelected = uploadOptionSelected;
    $scope.rendered = rendered;
    $scope.feedbackButtons = feedbackButtons;
    $scope.predictionCorrection = predictionCorrection;
    $scope.feedbackSent = feedbackSent;
    $scope.imageFile = imageFile;
    $scope.displayImageFile = displayImageFile;
    $scope.canvasTouched = canvasTouched;
    $scope.message = message;
    $scope.feedback = feedback;
    $scope.actualNumberFeedBack = actualNumberFeedBack;
    $scope.setUpCanvas = setUpCanvas;
    $scope.noTrained = noTrained;
});