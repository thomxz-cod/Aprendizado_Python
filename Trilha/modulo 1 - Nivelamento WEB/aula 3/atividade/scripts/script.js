const container = document.getElementById("cardsContainer");

document.getElementById("criarCard").addEventListener("click", () => {
    const card = document.createElement("div");
    card.className = "card";

    const titulo = document.createElement("h3");
    titulo.textContent = document.getElementById("tituloCard").value;

    const btnRemover = document.createElement("button");
    btnRemover.textContent = "Remover";
    btnRemover.addEventListener("click", () => {
        container.removeChild(card);
    });

    card.appendChild(titulo);
    card.appendChild(btnRemover);
    container.prepend(card);
});