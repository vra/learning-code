var express = require("express");
var http = require("http");

var app = express();

app.use(function(req, res, next){
	console.log("In comes a " + req.method + " to " + req.url);
	next();
});

app.use(function(req, res, next){
	res.writeHead(200, {"Content-Type": "text/plain"});
	res.end("Hello world!\n");
});

http.createServer(app).listen(1337);
