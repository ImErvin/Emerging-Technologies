angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, APIFactory) {
    var uploadFromFile;
    var uploadFromURL;
    var uploadOptions = [true,false];

    function message(){
        APIFactory.response.getImage().then(function(data){
            console.log(data);
        });
    }

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
    $scope.message = message;
});