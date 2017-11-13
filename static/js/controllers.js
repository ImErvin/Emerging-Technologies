angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, APIFactory) {

    var uploadOption = [true,false,false]; // 0 from URL, 1 from File, 2 from Canvas
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
    var canvas = document.getElementById("drawImageCanvas");
    var ctx = canvas.getContext("2d");


    function setUpCanvas(){
        canvas.height = canvas.height+100;
        ctx.fillStyle = "whitesmoke";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
    }
    
    function uploadOptionSelected(uploadoption){
        console.log(uploadoption);
        switch(uploadoption){
            case 0:
                $scope.uploadOption = [true,false,false];
                break;
            case 1:
                $scope.uploadOption = [false, true, false];
                break;
            case 2:
                setUpCanvas();
                $scope.uploadOption = [false, false, true];
                break;
            default:
                $scope.uploadOption = [false,false,false];
                break;
        }
    }

    function uploadFromUrl(url){
        var image = new Image();
        APIFactory.response.getImage(url).then(function(data) {
            image = data.data;
            $scope.displayImageFile = image;
        });
    }

    function uploadFromFile(file){
        uploadImage(file);
    }

    function uploadFromCanvas(){
        var pngUrl = canvas.toDataURL();
        uploadImage(pngUrl);
    }

    function uploadImage(base64){
        $scope.displayImageFile = $scope.imageFile;
        APIFactory.response.postImage(base64).then(function(data) {
            $scope.displayImageFile = base64;
            $scope.rendered = data.data;
        });
    }

    $scope.uploadFromFile = uploadFromFile;
    $scope.uploadFromUrl = uploadFromUrl;
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
});