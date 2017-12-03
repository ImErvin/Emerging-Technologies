angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        var request = {};

        request.postImage = function (base64) {
            var deferred = $q.defer();

            image = {
                imageFileName: "imageFile1.png",
                imageBase64: "" + base64
            }

            image = JSON.stringify(image);

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

        request.postFeedback = function (outputvalue, base64) {
            var deferred = $q.defer();

            image = {
                outputValue: outputvalue,
                imageBase64: "" + base64
            }

            image = JSON.stringify(image);

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

        return {
            request: request
        }


    });

