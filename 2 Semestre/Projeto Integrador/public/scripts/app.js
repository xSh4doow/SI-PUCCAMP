const Sequelize = require("sequelize");

// Loga no Banco de Dados
const db = new Sequelize("heroku_44f6983cc34c2f8", "b6340d84628fe2", "993dd2ea", {
    host: "us-cdbr-east-06.cleardb.net",
    dialect: "mysql"
});

// Conecta ao banco de dados e trata erros
db.authenticate()
    .then(() => {
        console.log("Conectado!");
    })
    .catch((erro) => {
        console.log(erro);
    });

// Define os modelos de dados usando o Sequelize
const Cartoes = db.define('cartoes', {
    idCartao: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: false
    }
}, {
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

// Define relacionamentos entre os modelos
Compras.belongsTo(Cartoes, { foreignKey: 'idCartao' });
conteudoCompra.belongsTo(Compras, { foreignKey: 'idCompra' });
conteudoCompra.belongsTo(Produtos, { foreignKey: 'idProduto' });

// Sincroniza os modelos com o banco de dados - CREATE IF NOT EXISTS
Cartoes.sync();
Produtos.sync();
Compras.sync();
conteudoCompra.sync();

// Gera um número de seis dígitos aleatório
function gerarNumeroDeSeisDigitos() {
    // Gera um número aleatório entre 100000 e 999999
    return Math.floor(Math.random() * 900000) + 100000;
}

// Verifica se um código existe no banco de dados
async function verificarCodigo(codigo) {
    try {
        const { count, rows } = await Cartoes.findAndCountAll({
            where: {
                idCartao: codigo
            }
        });
        return count; // retorna 0 ou 1
    } catch (error) {
        console.error('Erro ao verificar o código:', error);
        throw error;
    }
}

// Adiciona um novo cartão ao banco de dados
async function addNoBanco() {
    while (true) {
        const codigo = gerarNumeroDeSeisDigitos();

        if (await verificarCodigo(codigo) === 0) {
            console.log("O código não existe, adicionando no banco", codigo);
            await Cartoes.create({ idCartao: codigo });
            return parseInt(codigo, 10);
        } else {
            console.log("O código existe, não adicionando no banco");
        }
    }
}

// Obtém o ID da compra mais recente
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

// Obtém o ID de um produto pelo nome
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

// Adiciona compras com base no cartão e na lista de itens
async function addCompras(card, itens) {
    if (await verificarCodigo(card) === 1) {
        console.log("Esse cartão existe");
        await Compras.create({ idCartao: card });
        const idCompra = await getIdCompraMaisRecente();
        for (let i = 0; i < itens.length; i++) {
            const idProduto = await getIdProdutoPorNome(itens[i]);
            await conteudoCompra.create({ idCompra: idCompra, idProduto: idProduto, usou: false });
            console.log("added", itens[i], idProduto);
        }
        console.log(idCompra);
        return 1;
    } else {
        console.log("O código não existe");
        return 0;
    }
}


// Exporta as funções
module.exports = { addNoBanco, addCompras };