const botao = document.getElementById("botao");
const imagem = document.getElementById("imagem");

botao.addEventListener("click", () => {
    console.log("Botão clicado")
    fetch('https://api.thecatapi.com/v1/images/search')

    .then(function(response){
        console.log(`response HTTP Recebida:
Status Code: ${response.status}
Headers: ${response.headers}`)
        return response.json()
    })

    .then(function(data) {
        console.log(`Dados extraidos (Json - Object JS): ${data}`)

        const url = data[0].url;
        console.log(`URL do gato: ${url}`)

        imagem.src = url;
        imagem.style.display = "block";

        console.log("Imagem carregada com sucesso!")
    })
})