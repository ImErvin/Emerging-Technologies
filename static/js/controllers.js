angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, APIFactory) {

    var uploadOption = [true,false]; // 0 from URL, 1 from File, 2 from Canvas
    var imageUrl = undefined;
    var rendered = {
        fileName: null,
        message: null,
        icon: null,
        bgColor: null,
        prediction: null,
    };
    var feedbackButtons = true;
    var predictionCorrection = false;
    var feedbackSent = false;
    var imageFile;
    var displayImageFile;
    var canvasTouched = false;
    var message;
    var canvas = document.getElementById("drawImageCanvas");
    var ctx = canvas.getContext("2d");
    var outputValue = null;
    canvas.height = canvas.height+100;

    function setUpCanvas(){
        ctx.fillStyle = "Black";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    
    function uploadOptionSelected(uploadoption){
        console.log(uploadoption);
        $scope.message = undefined;
        switch(uploadoption){
            case 0:
                $scope.uploadOption = [true,false];
                break;
            case 1:
                setUpCanvas();
                $scope.canvasTouched = false;
                $scope.message = undefined;
                $scope.uploadOption = [false, true];
                break;
            default:
                $scope.uploadOption = [true,false];
                break;
        }
    }

    function uploadFromFile(file){
        if(file){
            uploadImage(file);
            $scope.message = undefined;
        }else{
            $scope.message = "Upload an image before uploading!"
        }
        
    }

    function uploadFromCanvas(){
        if($scope.canvasTouched){
            var pngUrl = canvas.toDataURL();
            uploadImage(pngUrl);
            $scope.message = undefined;
        }else{
            $scope.message = "Draw on the canvas before uploading!"
        }
        
    }

    function uploadImage(base64){
        resetFeedback();
        $scope.displayImageFile = $scope.imageFile;
        APIFactory.request.postImage(base64).then(function(data) {
            $scope.displayImageFile = base64;
            $scope.rendered = data.data;
        });
    }

    function uploadFeedback(outputvalue, base64){
        $scope.displayImageFile = $scope.imageFile;

        APIFactory.request.postFeedback(outputvalue, base64);
    }

    function feedback(correct){
        if(correct){
            $scope.feedbackButtons = false;
            $scope.feedbackSent = true;

            uploadFeedback($scope.rendered.prediction, $scope.displayImageFile)
        }else{
            $scope.feedbackButtons = false;
            $scope.predictionCorrection = true;
        }
    }

    function actualNumberFeedBack(number){
        $scope.predictionCorrection = false;
        $scope.feedbackSent = true;

        uploadFeedback(number, $scope.displayImageFile)        
    }

    function resetFeedback(){
        $scope.feedbackButtons = true;
        $scope.predictionCorrection = false;
        $scope.feedbackSent = false;
        $scope.predictionCorrection = false;
    }

    $scope.uploadFromFile = uploadFromFile;
    $scope.uploadFromCanvas = uploadFromCanvas;

    $scope.uploadOption = uploadOption;
    $scope.imageUrl = imageUrl;
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
});