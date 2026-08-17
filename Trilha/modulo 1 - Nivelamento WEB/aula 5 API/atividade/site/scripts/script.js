const botao = document.getElementById("botao");
const perfil = document.getElementById("perfil");

const inputUsuario = document.getElementById("usuario");

botao.addEventListener("click", () => {
    const nome = inputUsuario.value
    console.log("Botão clicado")
    fetch(`https://api.github.com/users/${nome}`)

    alert(nome)
})