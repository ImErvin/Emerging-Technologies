angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, APIFactory) {

    var uploadOption = [true,false,false]; // 0 from URL, 1 from File, 2 from Canvas
    var imageUrl = undefined;
    var rendered = {
        fileName: "sampleImage.jpg",
        message: "Image was processed successfully.",
        icon: "fa fa-smile-o",
        bgColor: "bg-success",
        prediction: "9",
    };
    var incorrect;

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

    function feedback(userFeedback){
        console.log(userFeedback);
        
    }

    $scope.uploadOption = uploadOption;
    $scope.imageUrl = imageUrl;
    $scope.uploadOptionSelected = uploadOptionSelected;
    $scope.rendered = rendered;
});