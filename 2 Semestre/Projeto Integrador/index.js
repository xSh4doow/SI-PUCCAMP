const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const { addNoBanco, addCompras } = require('./public/scripts/app.js');

// Configuração do servidor Express
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
const port = process.env.PORT || 3000;

// Rota para a página inicial
app.get('/', function (req, res) {
    const htmlPath = path.join(__dirname, 'html', 'iniciar.html');
    res.sendFile(htmlPath);
});

// Rota para a página de usuário
app.get('/usuario.html', function (req, res) {
    const htmlPath = path.join(__dirname, 'html', 'usuario.html');
    res.sendFile(htmlPath);
});

// Rota para gerar um novo cartão
app.get('/gerar-cartao', async (req, res) => {
    const informacao = await addNoBanco();
    res.json({ informacao });
});

// Rota para processar uma compra
app.post('/comprar', async (req, res) => {
    const produtosSelecionados = req.body.produtos;
    const idCartao = req.body.cartao;

    if (produtosSelecionados.length > 0 && idCartao > 0) {
        console.log(parseInt(idCartao));
        console.log(produtosSelecionados);

        let result = await addCompras(idCartao, produtosSelecionados);

        if (result === 1) {
            res.json({ success: true, message: 'Compra realizada com sucesso!' });
        } else if (result === 0) {
            res.json({ success: false, message: 'Erro na compra. Cartão Inválido.' });
        }
    } else {
        res.json({ success: false, message: 'Erro na compra. Nenhum produto selecionado.' });
    }
});

// Inicia o servidor na porta 8081
app.listen(port, function () {
    console.log('Servidor Rodando!');
});