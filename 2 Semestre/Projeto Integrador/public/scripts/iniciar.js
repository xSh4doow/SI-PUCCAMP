import swal from 'https://cdn.jsdelivr.net/npm/sweetalert@2.1.2/+esm'
// Criação de Constantes
const cartaoDiv = document.querySelector(".cartao");
const comprarDiv = document.querySelector(".comprar");
const relatoriosDiv = document.querySelector(".relatorios");

const cartaoBtn = document.getElementById("cartao-btn");
const comprarBtn = document.getElementById("comprar-btn");
const relatoriosBtn = document.getElementById("relatorios-btn");
const btnCartao = document.getElementById("show2");
const btnComprar = document.getElementById("comprar-btn2");

const imagemParaSumir1 = document.getElementById("hidden1");
const imagemParaSumir2 = document.getElementById("hidden2");
const imagemParaSumir3 = document.getElementById("hidden3");

const imagemParaAparecer1 = document.getElementById("show1");
const imagemParaAparecer2 = document.getElementById("show2");
const imagemParaAparecer3 = document.getElementById("show3");
const produtos = [
    { nome: "Gasolina", imagem: "/media/li-gas.png" },
    { nome: "Óleo Motor", imagem: "/media/li-oil.png" },
    { nome: "Óleo Cambio", imagem: "/media/li-oil.png" },
    { nome: "Aditivos Radiador", imagem: "/media/li-oil.png" },
    { nome: "Lavagem", imagem: "/media/li-carwashing.png" },
    { nome: "Calibrar Pneu", imagem: "/media/li-carwashing.png" },
    { nome: "Polimento", imagem: "/media/li-carwashing.png" },
    { nome: "Filtro de Ar", imagem: "/media/li-filter.png" },
    { nome: "Filtro de Óleo", imagem: "/media/li-filter.png" },
    { nome: "Filtro de Combustível", imagem: "/media/li-filter.png" },
    { nome: "Baterias", imagem: "/media/li-battery.png" },
    { nome: "Kit Óleo", imagem: "/media/teste45.png" },
    { nome: "Kit Filtro", imagem: "/media/teste45.png" },
    { nome: "Kit Lavagem", imagem: "/media/teste45.png" }
];

function criarListaProdutos() {
    const produtosList = document.getElementById("produtos-list");

    produtos.forEach((produto, index) => {
        const li = document.createElement("li");
        const label = document.createElement("label");
        const checkbox = document.createElement("input");
        const img = document.createElement("img");
        const textoProduto = document.createTextNode(produto.nome);

        checkbox.type = "checkbox";
        checkbox.value = produto.nome;
        checkbox.className = "checkbox-grande";

        img.className = "li-img";
        img.src = produto.imagem;
        img.alt = produto.nome;

        label.appendChild(checkbox);
        label.appendChild(img);
        label.appendChild(textoProduto);

        li.appendChild(label);

        produtosList.appendChild(li);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    cartaoBtn.addEventListener("click", function() {
      cartaoDiv.style.display = "block";
      comprarDiv.style.display = "none";
      relatoriosDiv.style.display = "none";

      cartaoBtn.style.display = "none";
      imagemParaSumir1.style.display = "none";

      imagemParaAparecer1.style.display = "flex";
      imagemParaAparecer2.style.display = "flex";
    });

    comprarBtn.addEventListener("click", function() {
      cartaoDiv.style.display = "none";
      comprarDiv.style.display = "block";
      relatoriosDiv.style.display = "none";
        
      comprarBtn.style.display = "none";
      imagemParaSumir2.style.display = "none";

      imagemParaAparecer3.style.display = "initial";
      criarListaProdutos();
    });

    /*
    relatoriosBtn.addEventListener("click", function() {
      cartaoDiv.style.display = "none";
      comprarDiv.style.display = "none";
      relatoriosDiv.style.display = "block";

      relatoriosBtn.style.display = "none";
      imagemParaSumir3.style.display = "none";
    });
     */
  });
function gerarCartao () {
    fetch('http://localhost:8081/gerar-cartao')
        .then(response => response.json())
        .then(data => {
            const resp = parseInt(data.informacao); // Converte para um número inteiro
            console.log('Informação recebida:', resp);

            // Verifica se resp é um número válido
            if (!isNaN(resp)) {
                swal("Cartão Gerado!", "Não se esqueça de anotar seu código! \n O Código do seu cartão é: " + resp, "success");
            } else {
                swal("Erro", "O servidor não retornou um valor válido.", "error");
            }
        })
        .catch(error => {
            console.error('Erro ao obter a informação:', error);
            swal("Erro", "Ocorreu um erro ao obter a informação do servidor.", "error");
        });
}

function comprarProdutos() {
    const produtosSelecionados = [];
    const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    const Card = document.getElementById("cartaoNumero");
    const valCard = Card.value;

    checkboxes.forEach((checkbox) => {
        produtosSelecionados.push(checkbox.value);
    });

    fetch('/comprar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ produtos: produtosSelecionados, cartao: valCard }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.success === true) {
                swal("Compra realizada com sucesso!", "Seus itens foram adicionados ao seu cartão!", "success");
            } else {
                swal("Erro", "Erro na compra. Tente novamente.", "error");
            }
        })
        .catch((error) => {
            console.error('Erro na solicitação:', error);
        });
}

btnCartao.addEventListener("click", function () {
    gerarCartao();
});

btnComprar.addEventListener("click", function () {
    comprarProdutos();
});

