// Informações para Login no Banco
const Sequelize = require("sequelize");
const db = new Sequelize("heroku_44f6983cc34c2f8", "b6340d84628fe2", "993dd2ea", {
    host: "us-cdbr-east-06.cleardb.net",
    dialect: "mysql"
})

// Testando Conexão com o Banco
db.authenticate().then(function () {
    console.log("Conectado!");
}).catch(function (erro) {
    console.log(erro);
});

// Entidades
/*
const Cartoes = db.define('cartoes', {
        id: {
                type: Sequelize.INTEGER,
                primaryKey: true,
                autoIncrement: false
            }
    },
    {
        updatedAt: false
});

const Produtos = db.define('produtos', {
    idProduto: {
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

const Compras = db.define('Compras', {
    idCompra: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    idCartao: {
        type: Sequelize.INTEGER,
    },
    dataCompra: {
        type: Sequelize.DATE,
    },
});

Compras.belongsTo(Cartao, { foreignKey: 'idCartao' });

const conteudoCompra = sequelize.define('conteudoCompra', {
    updatedAt: {
        type: DataTypes.DATE,
        defaultValue: sequelize.literal('CURRENT_TIMESTAMP'),
    },
    usou: {
        type: DataTypes.BOOLEAN,
    },
});

conteudoCompra.belongsTo(Compras, { foreignKey: 'idCompra' });
conteudoCompra.belongsTo(Produtos, { foreignKey: 'idProduto' });
*/ Arrumar


// Criar entidades se não existem
Cartoes.sync();

// Gerando o Código do Cartão
function gerarNumeroDeSeisDigitos() {
    // Gera um número aleatório entre 100000 e 999999
    return Math.floor(Math.random() * 900000) + 100000;
}

// Verifica se o Código já existe
async function verificarCodigo(codigo)
{
    let {count, rows} = await Cartoes.findAndCountAll(
        {
            where: {
                id: codigo
            }
        }
    );

    return count // retorna 0 ou 1
}

// Adiciona no Banco
async function addNoBanco() {
    while (true) {
        let codigo = gerarNumeroDeSeisDigitos();

        if (await verificarCodigo(codigo) === 0) {
            console.log("O código não existe, adicionando no banco", codigo);
            await Cartoes.create({id: codigo});
            return parseInt(codigo, 10);
        } else {
            console.log("O código existe, não adicionando no banco", codigo);
        }
    }
}

// Adicionar as compras no Banco

module.exports = addNoBanco;