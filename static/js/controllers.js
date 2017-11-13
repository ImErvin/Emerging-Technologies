angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, APIFactory) {

    var uploadOption = [true,false,false]; // 0 from URL, 1 from File, 2 from Canvas
    var imageUrl = undefined;
    var rendered = {
        fileName: "sampleImage.jpg",
        message: "Image was processed successfully.",
        icon: "fa fa-thumbs-up text-dark",
        bgColor: "bg-success",
        prediction: "9",
    };
    var feedbackButtons = true;
    var predictionCorrection = false;
    var feedbackSent = false;
    var imageFile;
    var canvas = document.getElementById("drawImageCanvas");
    var ctx = canvas.getContext("2d");
    canvas.height = canvas.height+100;
     // Set the fill colour to bright red.
     ctx.fillStyle = "whitesmoke";
     // Create a filled rectangle at co-ordinates (10,10)
     // with height and width set to 100.
     ctx.fillRect(0, 0, canvas.width, canvas.height);
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
                $scope.uploadOption = [false, false, true];
                break;
            default:
                $scope.uploadOption = [false,false,false];
                break;
        }
    }

    function uploadImage(file){
        $scope.rendered.fileName = file;
        console.log(APIFactory.response.postImage($scope.imageFile));
    }

    $scope.uploadOption = uploadOption;
    $scope.imageUrl = imageUrl;
    $scope.uploadOptionSelected = uploadOptionSelected;
    $scope.rendered = rendered;
    $scope.feedbackButtons = feedbackButtons;
    $scope.predictionCorrection = predictionCorrection;
    $scope.feedbackSent = feedbackSent;
    $scope.uploadImage = uploadImage;
    $scope.imageFile = imageFile;
});