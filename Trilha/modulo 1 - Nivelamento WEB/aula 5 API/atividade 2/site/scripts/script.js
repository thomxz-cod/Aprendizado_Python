document.addEventListener("DOMContentLoaded", function () {
    const botao = document.getElementById("buscar");
    
    botao.addEventListener("click", () => {      
        const inputCEP = document.getElementById("cep")
        let CEP = inputCEP.value;

        if (CEP.length !== 8) {
            alert("CEP inválido! O CEP deve conter 8 números.");
            return;
        }

        if (CEP) {
            let logradouro = document.getElementById("logradouro")
            let bairro = document.getElementById("bairro")
            let cidade = document.getElementById("cidade")
            let uf = document.getElementById("uf")

            fetch(`https://viacep.com.br/ws/${CEP}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (data.erro == "true") {
                        alert("Erro ao procurar CEP!")
                    } else {
                        logradouro.innerHTML = `<b>Logradouro:</b> ${data.logradouro}`
                        bairro.innerHTML = `<b>Bairro:</b> ${data.bairro}`
                        cidade.innerHTML = `<b>Cidade:</b> ${data.cidade}`
                        uf.innerHTML = `<b>UF:</b> ${data.uf}`
                    }

                })
        } else {
            alert("CEP invalido")
        }
    })
});