//função javaScrip que chama a view mostrarServicos
//essa função utiliza o ajax por meio do fetch para 
//mostrar mais serviços sem que o usuário seja redireciondo
//para outra página
document.addEventListener("DOMContentLoaded", function(){
    const botao = document.getElementById("mostrarMais");
    if(botao){
        botao.addEventListener("click", function(){
            fetch("/clinicaEstetica/mostrarServicos")
            .then(response => response.text())
            .then(html => {
                document.getElementById("servicosIniciais").insertAdjacentHTML("beforeend", html);
                botao.remove();
            })
            .catch(error => console.error("Erro ao carregar servicos:", error));
            
        });
    }
});