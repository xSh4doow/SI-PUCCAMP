const express = require('express');
const app = express();
const path = require("path");
app.use(express.static(__dirname + '/public'));
const addNoBanco = require("./public/scripts/app.js");
const bodyParser = require('body-parser');
app.use(bodyParser.json());

app.get("/", function (req, res){
    let _html = path.join(__dirname, 'html', 'iniciar.html');
    res.sendFile(_html);
});

app.get("/usuario.html", function (req, res){
    let _html = path.join(__dirname, 'html', 'usuario.html');
    res.sendFile(_html);
});

app.get('/gerar-cartao', async (req, res) => {
    const informacao = await addNoBanco();
    res.json({ informacao });
});

app.post('/comprar', (req, res) => {
    const produtosSelecionados = req.body.produtos;

    // Faça o processamento da compra aqui (por exemplo, salvar no banco de dados)
    // Dependendo do seu aplicativo, você pode precisar de um módulo de banco de dados para isso.

    // Simule uma resposta de sucesso (você deve personalizar isso)
    const compraBemSucedida = true;

    res.json({ success: compraBemSucedida });
});

app.listen(8081, function (){
    console.log("Servidor Rodando!");

});
