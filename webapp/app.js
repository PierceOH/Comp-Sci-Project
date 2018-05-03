var express = require("express");
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var server = require('http').createServer(app);
var io = require('socket.io')(server);
const cv = require('opencv');
var Jimp = require("jimp");
var pixel_total = 0;
var match_total = 0;

var image_detection = []
Jimp.read("texture1.png", function (err, image) {
    if (err) throw err;
    var i;
    var j;
    for (i = 0; i < 7; i++) {
      for (j = 0; j < 8; j++) {
        pixel = (image.getPixelColor(i,j));

        var flag = 1;
        for (k = 0; k < image_detection.length;k++){

            if (pixel == image_detection[k]){
              flag = 0;
            }
        }
        if (flag == 1){
          console.log("ADD TO ARRAY");
          image_detection.push(pixel);
        }
      }
    }

    console.log('\x1b[32m%s\x1b[0m', 'Initialisation fully complete');
});


Jimp.read("texture2.png", function (err, image) {
    if (err) throw err;
    var i;
    var j;
    for (i = 0; i < 7; i++) {
      for (j = 0; j < 3; j++) {
        pixel = (image.getPixelColor(i,j));

        var flag = 1;
        for (k = 0; k < image_detection.length;k++){

            if (pixel == image_detection[k]){
              flag = 0;
            }
        }
        if (flag == 1){
          console.log("ADD TO ARRAY");
          image_detection.push(pixel);
        }
      }
    }


console.log('\x1b[32m%s\x1b[0m', 'Initialisation 1 complete with the ammount of RBG values below ');
console.log(image_detection.length);
});


Jimp.read("texture3.png", function (err, image) {
    if (err) throw err;
    var i;
    var j;
    for (i = 0; i < 2; i++) {
      for (j = 0; j < 5; j++) {
        pixel = (image.getPixelColor(i,j));

        var flag = 1;
        for (k = 0; k < image_detection.length;k++){

            if (pixel == image_detection[k]){
              flag = 0;
            }
        }
        if (flag == 1){
          console.log("ADD TO ARRAY");
          image_detection.push(pixel);
        }
      }
    }


console.log('\x1b[32m%s\x1b[0m', 'Initialisation 1 complete with the ammount of RBG values below ');
console.log(image_detection.length);
});








router.use(function (req,res,next) {
  console.log("/" + req.method);
  next();
});

router.get("/",function(req,res){
  res.sendFile(path + "index.html");
});

router.get("/map",function(req,res){
  res.sendFile(path + "map.html");
});
app.use("/",router);

app.use("*",function(req,res){
  res.sendFile(path + "404.html");
});



server.listen(3000);
console.log("listening to port 3000:");


io.listen(server).on('connection', function (socket) {
      console.log("Connected");
       socket.on('message', function (msg) {
          if (msg == "Area") {
              console.log("Calculate area")


              Jimp.read("static2.png", function (err, image) {
                  if (err) throw err;
                  console.log((image.getPixelColor(0,0)));
                  pixel = (image.getPixelColor(0,0));
                  console.log(Jimp.intToRGBA(pixel));

              });








              console.log('sent "COMPLETE"')

              //https://www.npmjs.com/package/opencv  use for image detection! (RGB)

          } else {
            data_array = msg
            lat = data_array[0].toString();
            long = data_array[1].toString();
            pixel_total = 0;
            match_total = 0;
            console.log(lat,long);
            var fs = require('fs'),
            request = require('request');

            var download = function(uri, filename, callback){
                 request.head(uri, function(err, res, body){
                       request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
                       });
                 };
         download('https://maps.googleapis.com/maps/api/staticmap?center='+ lat + ',' + long+ '&zoom=16&size=520x550', 'static1.png', function(){
         console.log('done1');
 });
 //'https://maps.googleapis.com/maps/api/staticmap?center=' + str(lat)+',' + str(long)+ ' &zoom=' + str(zoom)+'&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false'
 download('https://maps.googleapis.com/maps/api/staticmap?center='+ lat + ',' + long+ '&zoom=16&size=520x550&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false', 'static2.png', function(){
 console.log('done2');
 Jimp.read("static2.png", function (err, image) {
     if (err) throw err;

 for (k = 0;k < 520;k++){

    for (p = 0; p < 520;p++){
        pixel_total = pixel_total + 1
        pixel = (image.getPixelColor(p,k));
        for (i = 0; i < image_detection.length;i++){
            if (pixel == image_detection[i]){
              match_total = match_total + 1;

            }
        }
          }
    }
metres = (match_total/pixel_total)*1000000
console.log(metres);

 });
 });
//When RGB image processing only count down to pixel 520. as I have extended the request image to avoid the google logo!.

const delay = require('delay');
console.log("DELAY")
delay(1200)
    .then(() => {
        metres = (match_total/pixel_total)*1000000
        console.log("Delay complete")
        socket.emit('message', JSON.stringify(metres));
    });


          }


 });

});

//socket setup
