// const botao = document.getElementById("botao");
// const perfil = document.getElementById("perfil");

// const inputUsuario = document.getElementById("usuario");

// botao.addEventListener("click", () => {
//     const nome = inputUsuario.value
//     console.log("Botão clicado")
//     fetch(`https://api.github.com/users/${nome}`)

//     alert(nome)
// })

document.addEventListener("DOMContentLoaded", function () {
    const botao = document.getElementById("buscar");
    
    botao.addEventListener("click", () => {      
        let input_nome = document.getElementById("usuario");
        let imagem = document.getElementById("imagemPerfil");
        let titulo = document.getElementById("titulo");
        let bio = document.getElementById("bio");

        let nome = input_nome.value;
        
        fetch(`https://api.github.com/users/${nome}`)
        .then(response => response.json())
        .then(data => {
            imagem.src = data.avatar_url
            titulo.innerText = data.name
            bio.innerText = data.bio
        })

    })
});