const express = require('express');
const app = express();
const path = require("path");

app.use(express.static(__dirname + '/public'));

app.get("/", function (req, res){
    let _html = path.join(__dirname, 'html', 'iniciar.html');
    res.sendFile(_html);
});

app.get("/usuario.html", function (req, res){
    let _html = path.join(__dirname, 'html', 'usuario.html');
    res.sendFile(_html);
});

app.listen(8081, function (){
    console.log("Servidor Rodando!");

});
