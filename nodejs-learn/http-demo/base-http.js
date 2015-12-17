var http = require("http");

var app = http.createServer(
	function(request, response){
		response.writeHead(200, {"Content-Type": "text/plain"});
		response.end("This is a http server");
	}
);

app.listen(3000, "localhost");
