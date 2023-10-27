const Sequelize = require("sequelize");
const db = new Sequelize("heroku_44f6983cc34c2f8", "b6340d84628fe2", "993dd2ea", {
    host: "us-cdbr-east-06.cleardb.net",
    dialect: "mysql"
})

db.authenticate().then(function () {
    console.log("Conectado!");
}).catch(function (erro) {
    console.log(erro);
});

const Cartoes = db.define('cartoes', {
        idCartao: {
            type: Sequelize.INTEGER,
            primaryKey: true,
            autoIncrement: false
            }
    },
    {
        updatedAt: false
});

const Produtos = db.define('produtos', {
    idProdutos: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    nomeProduto: {
        type: Sequelize.STRING(255),
    },
}, {
    timestamps: false
});

const Compras = db.define('compras', {
    idCompra: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    idCartao: {
        type: Sequelize.INTEGER,
    },
}, {
    timestamps: false
});

Compras.belongsTo(Cartoes, { foreignKey: 'idCartao' });

const conteudoCompra = db.define('conteudoCompra', {
    idCompra: {
        type: Sequelize.INTEGER,
    },
    idProduto: {
        type: Sequelize.INTEGER,
    },
    usou: {
        type: Sequelize.BOOLEAN,
    },
}, {
    createdAt: false
});

conteudoCompra.belongsTo(Compras, { foreignKey: 'idCompra' });
conteudoCompra.belongsTo(Produtos, { foreignKey: 'idProduto' });

Cartoes.sync();
Produtos.sync();
Compras.sync();
conteudoCompra.sync();

function gerarNumeroDeSeisDigitos() {
    // Gera um número aleatório entre 100000 e 999999
    return Math.floor(Math.random() * 900000) + 100000;
}

async function verificarCodigo(codigo)
{
    let {count, rows} = await Cartoes.findAndCountAll(
        {
            where: {
                idCartao: codigo
            }
        }
    );

    return count // retorna 0 ou 1
}

async function addNoBanco() {
    while (true) {
        let codigo = gerarNumeroDeSeisDigitos();

        if (await verificarCodigo(codigo) === 0) {
            console.log("O código não existe, adicionando no banco", codigo);
            await Cartoes.create({idCartao: codigo});
            return parseInt(codigo, 10);
        } else {
            console.log("O código existe, não adicionando no banco");
        }
    }
}

async function getIdCompraMaisRecente() {
    try {
        const compraMaisRecente = await Compras.findOne({
            order: [['idCompra', 'DESC']],
        });

        if (compraMaisRecente) {
            return compraMaisRecente.idCompra;
        } else {
            return null;
        }
    } catch (error) {
        console.error('Erro ao obter idCompra mais recente:', error);
        throw error;
    }
}

async function getIdProdutoPorNome(nomeProduto) {
    try {
        const produto = await Produtos.findOne({
            where: {
                nomeProduto: nomeProduto,
            },
        });

        if (produto) {
            return produto.idProdutos;
        } else {
            return null;
        }
    } catch (error) {
        console.error('Erro ao obter idProduto por nomeProduto:', error);
        throw error;
    }
}

async function addCompras(card, itens){
    if (await verificarCodigo(card) === 1) {
        console.log("Esse cartão existe");
        await Compras.create({idCartao: card})
        let idCompra = await getIdCompraMaisRecente();
        for (let i = 0; i < itens.length; i++) {
            let idProduto = await getIdProdutoPorNome(itens[i]);
            await conteudoCompra.create({idCompra: idCompra, idProduto: idProduto, usou: false})
            console.log("added", itens[i], idProduto);
        }
        console.log(idCompra);
        return 1
    } else {
        console.log("O código não existe");
        return 0
    }
}

module.exports = {addNoBanco, addCompras};