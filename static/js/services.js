angular.module('app.services', [])

    .factory("APIFactory", function ($http, $q) {

        var response = {};

        response.getImage = function () {
            var deferred = $q.defer();
            url = 123;
            $http({
                method: 'GET',
                url: 'http://127.0.0.1:5000/uploadImage',
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

            $http({
                data: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAIAAAD9b0jDAAABq0lEQVR4nO2VO4vCQBDH545LQBHEWEgaFSwFq/Ri76MR/ByCD0ivldraaWEVRAn2FoIkFiK4IIKVXdTOJorriMWCyMlFiSkO7v7VzoPfzLAvgD+tD+twoVBwuVyxWCybzQJAs9nUdb3T6dgvqCgKPmi1WgWDQQeIi8Wi0WioqspMWZbtECVJOp1OiEgICYfDHo8HAHien81miFir1exAU6kUpZQQIorizSnL8vF4RMREImEHCgChUEgQhHvPfD5n49uHflOxWDwcDoioaZrb7XaAmEwmGdEwjHg8/jT/8xWoJEk8zwOAoiij0ejdHgFAVVXTNBGx3W6zY/CuRFHc7XaIuN1uI5GIA0QA0DSN7Xi9XneGmE6n2cEcDofODO73+yeTicNtVqtVRuz1es60CQBscES8v6kv6utphiAIlNKbud/vKaUcx3m9XgDw+Xz5fJ6FELFcLpum+RxKCLk3u92uYRiBQCCXyz0mbzabSqXy48vf7/czmYx1vfP5fLlcAGAwGEynUwAYj8e6rlt9J6VSieM4to5Go7fWWq3Wer1mhZfLpXXhf/1iXQEBYPmer6PclwAAAABJRU5ErkJggg==",                
                method: 'POST',
                url: 'http://127.0.0.1:8080/uploadImage',
                headers: {
                    'Content-Type': 'text/plain',
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

