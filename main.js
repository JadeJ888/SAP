const express = require('express'); //import server

var server = express(); //declare a server variable
server.use(express.static(__dirname)) //tell server to host index.html as a static webpage

var port = 8000; //set port to 8000
server.listen(port, function() { //tell server to listen on port 8000
    console.log('(SAP): Listening on port ' + port); //after server is done, tell console that it's up
});