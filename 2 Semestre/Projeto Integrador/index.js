const express = require('express');
const app = express();
const path = require("path");
app.use(express.static(__dirname + '/public'));
const {addNoBanco} = require("./public/scripts/app.js");
const {addCompras} = require("./public/scripts/app.js");
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

app.post('/comprar', async (req, res) => {
    const produtosSelecionados = req.body.produtos;
    const idC = req.body.cartao;

    if (produtosSelecionados.length > 0 && idC > 0) {
        console.log(parseInt(idC));
        console.log(produtosSelecionados);
        let result = await addCompras(idC, produtosSelecionados);
        if (result === 1) {
            res.json({success: true, message: "Compra realizada com sucesso!"});
        } else if (result === 0) {
            res.json({success: false, message: "Erro na compra. Cartão Inválido."});
        }
    } else {
        res.json({success: false, message: "Erro na compra. Nenhum produto selecionado."});
    }
});

app.listen(8081, function (){
    console.log("Servidor Rodando!");

});
