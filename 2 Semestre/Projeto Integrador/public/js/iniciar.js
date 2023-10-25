// Criação de Constantes
const cartaoDiv = document.querySelector(".cartao");
const comprarDiv = document.querySelector(".comprar");
const relatoriosDiv = document.querySelector(".relatorios");

const cartaoBtn = document.getElementById("cartao-btn");
const comprarBtn = document.getElementById("comprar-btn");
const relatoriosBtn = document.getElementById("relatorios-btn");

const imagemParaSumir1 = document.getElementById("hidden1");
const imagemParaSumir2 = document.getElementById("hidden2");
const imagemParaSumir3 = document.getElementById("hidden3");

const imagemParaAparecer1 = document.getElementById("show1");
const imagemParaAparecer2 = document.getElementById("show2");
const imagemParaAparecer3 = document.getElementById("show3");

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
    });
  
    relatoriosBtn.addEventListener("click", function() {
      cartaoDiv.style.display = "none";
      comprarDiv.style.display = "none";
      relatoriosDiv.style.display = "block";

      relatoriosBtn.style.display = "none";
      imagemParaSumir3.style.display = "none";
    });
  });






  