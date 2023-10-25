import swal from 'https://cdn.jsdelivr.net/npm/sweetalert@2.1.2/+esm'

const gerarCartao = document.getElementById("show2");

// Mostrar o cartão
gerarCartao.addEventListener("click", function () {
    swal("Cartão Gerado!", "O Código do seu cartão é: "+(10), "success");
});
