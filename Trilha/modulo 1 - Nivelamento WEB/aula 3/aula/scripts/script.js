const container = document.getElementById("container");

// 1 - appendChild - adiciona no final
document.getElementById("btnAppend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Paragrafo adicionado com appendChild";
    container.appendChild(p);
});

// 2 - prepend - no inicio
document.getElementById("btnPrepend").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Paragrafo adicionado no inicio (prepend)";
    const primeiro = container.prepend(p);
});

// 3 - insertBefore - antes do primeiro
document.getElementById("btnInsertBefore").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Paragrafo inserido antes do primeiro (insertBefore)";
    const primeiro = container.firstElementChild;
    container.insertBefore(p, primeiro);
});

// 4 - replaceWith - substitui o primeiro paragrafo
document.getElementById("btnReplace").addEventListener("click", () => {
    const novo = document.createElement("p");
    novo.textContent = "Primeiro paragrafo substituido!";
    const primeiro = container.firstElementChild;
    primeiro.replaceWith(novo);
});

// 5 - add card
document.getElementById("btnCard").addEventListener("click", () => {
    const card = document.createElement("div");
    card.className = "card";

    const titulo = document.createElement("h3");
    titulo.textContent = "Card Dinamico";

    const btnRemover = document.createElement("button");
    btnRemover.textContent = "Remover";
    btnRemover.addEventListener("click", () => {
        container.removeChild(card);
    });

    card.appendChild(titulo);
    card.appendChild(btnRemover);
    container.prepend(card);
});

// 6 - manipule text with textContext
document.getElementById("btnTextContent").addEventListener("click", () => {
    const p = document.createElement("p");
    p.textContent = "Texto add com textContext";
    container.appendChild(p);
});

// 7 - manipule html with innerHTML
document.getElementById("btnInnerHTML").addEventListener("click", () => {
    const p = document.createElement("p");
    p.innerHTML = "<strong>Text add com innerHTML</strong>";
    container.appendChild(p);
});
