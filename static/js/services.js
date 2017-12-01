angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        var response = {};

        response.postImage = function(base64) {
            var deferred = $q.defer();
            
            image = {
                imageFileName: "imageFile1.png",
                imageBase64: ""+base64
            }

            user = JSON.stringify(image);

            $http({
                method: 'POST',
                url: 'http://127.0.0.1:5000/uploadImage',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: user,
            }).then(function success(response) {

                deferred.resolve(response)
            }).catch(function(error) {
                deferred.reject(error);
            });
            console.log(deferred.promise);
            return deferred.promise;
        }

        return {
            response: response
        }

    
    });

