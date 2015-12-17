var express = require("express");
var http = require("http");

var app = express();

app.all("*", function(req, res,next){
	res.writeHead(200, {"Content-Type": "text/plain"});
	next();
});

app.get("/$", function(req, res){
	res.end("welcome to homepage!");
});

app.get("/about", function(req, res){
	res.end("welcome to about page!");
});

app.get("*", function(req, res){
	res.end("404");
});


http.createServer(app).listen(1337);
