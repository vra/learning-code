var express = require("express");
var http = require("http");

var app = express();

app.use("/$", function(req, res, next){
		res.writeHead(200, {"Content-Type": "text/plain"});
		res.end("This is root dir");
	});

app.use("/about", function(req, res, next){
		res.writeHead(200, {"Content-Type": "text/plain"});
		res.end("This is about page");
	});

app.use(function(req, res){
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end("This is 404 page");
	});

http.createServer(app).listen(1337);
