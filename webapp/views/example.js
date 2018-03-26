$(function(){
           var iosocket = io.connect();
           iosocket.on('connect', function () {
                  alert("Connected")
      });
      $('#confirm').click(function(event) {
               event.preventDefault();
               iosocket.send("PENIS");
          }
      });
  });
