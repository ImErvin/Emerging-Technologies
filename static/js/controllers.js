angular.module('app.controllers', [])

.controller('mainCtrl', function($scope) {
    var uploadFromFile;
    var uploadFromURL;
    var uploadOptions = [true,false];

    console.log("woo");

    function uploadFromFile(uploadMethod){
        switch(uploadMethod){
            case 0:
                $scope.uploadOptions = [true,false];
            case 1:
                $scope.uploadOptions = [false,true];
        }
    }

    $scope.random = function(){
        console.log("working");
    }

    $scope.uploadFromFile = uploadFromFile;
    $scope.uploadFromURL = uploadFromURL;
    $scope.uploadOptions = uploadOptions;
});

console.log("woo");