angular.module('app.controllers', [])

.controller('mainCtrl', function($scope, $http, $q) {
    var uploadFromFile;
    var uploadFromURL;
    var uploadOptions = [true,false];

    function message() {
        var deferred = $q.defer();

        $http({
            method: 'GET',
            url: 'http://127.0.0.1:5000/image',
            headers: {
                'Content-Type': 'application/json'
            },
        }).then(function success(response) {

            deferred.resolve(response)
        }).catch(function(error) {
            deferred.reject(error);
        });

        console.log(deferred.promise);
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