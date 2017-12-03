angular.module('app.directives', [])

// Ripped from https://stackoverflow.com/questions/17063000/ng-model-for-input-type-file
.directive("fileread", [function () {
    return {
        scope: {
            fileread: "="
        },
        link: function (scope, element, attributes) {
            element.bind("change", function (changeEvent) {
                var reader = new FileReader();
                
                reader.onload = function (loadEvent) {
                    scope.$apply(function () {
                        scope.fileread = loadEvent.target.result;
                    });
                }
                reader.readAsDataURL(changeEvent.target.files[0]);
            });
        }
    }
}])

// Ripped from https://stackoverflow.com/questions/16587961/is-there-already-a-canvas-drawing-directive-for-angularjs-out-there
.directive("drawing", function(){
    return {
      restrict: "A",
      link: function(scope, element){
        var ctx = element[0].getContext('2d');
        
  
        // variable that decides if something should be drawn on mousemove
        var drawing = false;
  
        // the last coordinates before the current move
        var lastX;
        var lastY;

        element.bind('mousedown', function(event){
          if(event.offsetX!==undefined){
            lastX = event.offsetX;
            lastY = event.offsetY;
          } else { // Firefox compatibility
            lastX = event.layerX - event.currentTarget.offsetLeft;
            lastY = event.layerY - event.currentTarget.offsetTop;
          }
  
          // begins new line
          ctx.beginPath();
  
          drawing = true;
        });
        element.bind('mousemove', function(event){
          if(drawing){
            // get current mouse position
            if(event.offsetX!==undefined){
              currentX = event.offsetX;
              currentY = event.offsetY;
            } else {
              currentX = event.layerX - event.currentTarget.offsetLeft;
              currentY = event.layerY - event.currentTarget.offsetTop;
            }
  
            draw(lastX, lastY, currentX, currentY);
  
            // set current coordinates to last one
            lastX = currentX;
            lastY = currentY;
          }
  
        });
        element.bind('mouseup', function(event){
          // stop drawing
          drawing = false;
        });
  
        // canvas reset
        // function reset(){
        //  element[0].width = element[0].width; 
        // }
  
        function draw(lX, lY, cX, cY){
          ctx.lineWidth=5;
          // line from
          ctx.moveTo(lX,lY);
          // to
          ctx.lineTo(cX,cY);
          // color
          ctx.strokeStyle = "white";
          // draw it

          ctx.stroke();
        }
      }
    };
  });

