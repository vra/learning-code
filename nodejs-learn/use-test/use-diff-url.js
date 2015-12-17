var express = require("express");
var http = require("http");

var app = express();

app.use(function(req, res, next){
	if (req.url == "/"){
		res.writeHead(200, {"Content-Type": "text/plain"});
		res.end("Welcome to root dir");
	}
	else{
		next();
	}
});

app.use(function(req, res, next){
	if (req.url == "/about"){
		res.writeHead(200, {"Content-Type": "text/plain"});
		res.end("This is about page");
	}
	else{
		next();
	}
});

app.use(function(req, res){
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end("404 not found");
});

http.createServer(app).listen(1337);
