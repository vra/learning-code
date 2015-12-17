//test.js
var express = require('express');
var app = express();

//This is '/' path routing
app.get('/', function(req, res) {
	res.send('Hello world!');
	});

app.get('/customer', function(req, res) {
	res.send('customer page');
	});

app.get('/admin', function(req, res) {
	res.send('admin page');
	});

app.listen(3000);

