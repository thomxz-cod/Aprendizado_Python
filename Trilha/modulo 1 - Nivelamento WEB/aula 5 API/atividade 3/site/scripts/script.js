// https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true

const imgs = {
    "frio" : "https://i.pinimg.com/1200x/6c/29/98/6c2998bd3d41c11cb3e066937b584c81.jpg",
    "normal" : "https://i.pinimg.com/1200x/06/23/50/062350c88473334c815561a92658db79.jpg",
    "quente" : "https://i.pinimg.com/736x/8f/65/63/8f6563a9d339ed641b026cb444d1fe3d.jpg"
}


document.addEventListener("DOMContentLoaded", function () {
    const botao = document.getElementById("buscar");

    let imgTemperatura = document.getElementById("imgTemperatura")
    let nomeCidade = document.getElementById("nomeCidade")
    let temperaturaAtual = document.getElementById("temperaturaAtual")
    
    botao.addEventListener("click", () => {
        const select = document.getElementById("cidade");
        let cordenada = select.value;
        let[lat, lon] = cordenada.split(",")
        fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`)

        .then(response => response.json())
        .then(data => {
            let temp = data.current_weather.temperature
            temperaturaAtual.innerHTML = `<i>Temperatura Atual: </i>${temp}`

            if (temp <= 25) {
                imgTemperatura.src = imgs["frio"]
            } else if (temp <= 30) {
                imgTemperatura.src = imgs["normal"]
            } else {
                imgTemperatura.src = imgs["quente"]
            }
        })
    })
});