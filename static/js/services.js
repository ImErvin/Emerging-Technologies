angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        var response = {};

        response.getImage = function () {
            var deferred = $q.defer();
            url = 123;
            $http({
                method: 'GET',
                url: 'http://127.0.0.1:5000/image/'+url,
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(function success(response) {
                deferred.resolve(response)
            }).catch(function (error) {
                deferred.reject(error);
            });

            return deferred.promise;
        }

        response.postImage = function (file) {
            var deferred = $q.defer();


            url = "123";

            $http({
                method: 'POST',
                url: 'http://127.0.0.1:8080/uploadImage',
                headers: {
                    'Content-Type': 'application/json'
                },
            }).then(function success(response) {

                deferred.resolve(response)
            }).catch(function (error) {
                deferred.reject(error);
            });

            return deferred.promise;
        }

        return {
            response: response
        }

    });

