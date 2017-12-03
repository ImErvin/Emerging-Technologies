angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        var request = {};

        request.postImage = function (file) {
            var deferred = $q.defer();

            image = JSON.stringify(file);

            console.log(image)

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
            console.log(deferred.promise);
            return deferred.promise;
        }

        request.postFeedback = function (feedback) {
            var deferred = $q.defer();

            image = JSON.stringify(feedback);
            console.log(image)
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
            console.log(deferred.promise);
            return deferred.promise;
        }

        request.getNoTrained = function () {
            var deferred = $q.defer();

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
            console.log(deferred.promise);
            return deferred.promise;
        }

        return {
            request: request
        }


    });

