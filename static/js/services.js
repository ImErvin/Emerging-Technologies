angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        // Create request object - this is where all the $http functions will go
        var request = {};

        // Aynchronous call to send image file to server
        request.postImage = function (file) {
            // Create a promise
            var deferred = $q.defer();

            image = JSON.stringify(file);

            // Use angular's $http with POST method, the url and 1 header (content-type), send json data.
            $http({
                method: 'POST',
                url: 'http://127.0.0.1:5000/postImage',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: image,
            }).then(function success(response) {
                deferred.resolve(response)
            }).catch(function (error) {
                deferred.reject(error);
            });
            
            // Return that promise to the controller
            return deferred.promise;
        }

        // Aynchronous call to send training data to server
        request.postFeedback = function (feedback) {
            // Create a promise
            var deferred = $q.defer();

            // Use angular's $http with POST method, the url and 1 header (content-type), send json data.
            image = JSON.stringify(feedback);
            $http({
                method: 'POST',
                url: 'http://127.0.0.1:5000/postFeedback',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: image,
            }).then(function success(response) {
                deferred.resolve(response)
            }).catch(function (error) {
                deferred.reject(error);
            });

            // Return that promise to the controller
            return deferred.promise;
        }

        // Aynchronous call to get no of times trained data from server
        request.getNoTrained = function () {
            // Create a promise
            var deferred = $q.defer();

            // Use angular's $http with GET method, the url and 1 header (content-type), recieve json data.
            $http({
                method: 'GET',
                url: 'http://127.0.0.1:5000/getNoTrained',
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(function success(response) {
                deferred.resolve(response)
            }).catch(function (error) {
                deferred.reject(error);
            });

            // Return that promise to the controller
            return deferred.promise;
        }
        
        // Return request functions to be used in the controller.
        return {
            request: request
        }


    });

