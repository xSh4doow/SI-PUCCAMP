// Informações para Login no Banco
const Sequelize = require("sequelize");
const sequelize = new Sequelize("heroku_44f6983cc34c2f8", "b6340d84628fe2", "993dd2ea", {
    host: "us-cdbr-east-06.cleardb.net",
    dialect: "mysql"
})

const Cartoes = sequelize.define('cartoes',
    {
        id:
            {
                type: Sequelize.INTEGER,
                primaryKey: true,
                autoIncrement: false
            }
    },
    {
        updatedAt: false
    }
);

const Compras = sequelize.define({});

async function autenticar()
{
// Testando Conexão com o Banco
    sequelize.authenticate().then(function () {
        console.log("Conectado!");
    }).catch(function (erro) {
        console.log(erro);
    });
}

// Gerando um cartão //

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
            Cartoes.create({ id: codigo });
            return parseInt(codigo, 10);
        } else {
            console.log("O código existe, não adicionando no banco", codigo);
        }
    }
}


module.exports = addNoBanco;