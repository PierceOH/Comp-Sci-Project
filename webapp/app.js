var express = require("express");
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var server = require('http').createServer(app);
var io = require('socket.io')(server);





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

router.get("/confirm",function(req,res){
  res.sendFile(path + "confirm.html");
});

router.get("/contact",function(req,res){
  res.sendFile(path + "contact.html");
});

router.get("/load",function(req,res){
  res.sendFile(path + "load.html");
});
router.get("/results",function(req,res){
  res.sendFile(path + "results.html");
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
              socket.emit('message', msg);
              console.log('sent "COMPLETE"')

              //https://www.npmjs.com/package/opencv  use for image detection! (RGB)

          } else {
            data_array = msg
            lat = data_array[0].toString();
            long = data_array[1].toString();
            console.log(lat,long);
            var fs = require('fs'),
            request = require('request');

            var download = function(uri, filename, callback){
                 request.head(uri, function(err, res, body){
                       request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
                       });
                 };
         download('https://maps.googleapis.com/maps/api/staticmap?center='+ lat + ',' + long+ '&zoom=16&size=600x640', 'static1.png', function(){
         console.log('done1');
 });
 //'https://maps.googleapis.com/maps/api/staticmap?center=' + str(lat)+',' + str(long)+ ' &zoom=' + str(zoom)+'&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false'
 download('https://maps.googleapis.com/maps/api/staticmap?center='+ lat + ',' + long+ '&zoom=16&size=530x640&scale=1&style=visibility:off&style=feature:road|element:geometry|color:99ff30|visibility:on&sensor=false', 'static2.png', function(){
 console.log('done2');
 });

          }


 });

});

//socket setup
