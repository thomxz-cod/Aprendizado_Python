document.addEventListener("DOMContentLoaded", function () {
  const duploClique = document.getElementById("duploClique");
  duploClique.addEventListener("dblclick", () => {
    alert("Você deu um duplo click nesse parágrafo");
    console.log("this se refere a:", this); // exibe o elemento clicado
  });

  // demonstração arrow function x função regular
  duploClique.addEventListener("click", () => {
    console.log("Arrow funtion this: ", this);
  });


  const btnRemoverItem2 = document.getElementById("btnRemoverItem2");
  const lista = document.getElementById("lista");

  btnRemoverItem2.addEventListener("click", () => {
    const item2 = document.getElementById("item2");
    if (item2) {
        item2.remove();
    } else {
        alert("Item ja foi apagado!")
    }
  });

  const item3 = document.getElementById("item3");
  if (item3) {
    lista.removeChild(item3);
  }

  const tarefas = document.getElementById("tarefas")
  const btnAdicionarTarefa = document.getElementById("btnAdicionarTarefa")
  let contador = (document.getElementsByClassName("tarefa")).length

  btnAdicionarTarefa.addEventListener("click", () => {
    const li = document.createElement("li");
    li.className = "tarefa";
    contador++;
    li.textContent = "Tarefa " + contador;
    tarefas.appendChild(li);
  });

  tarefas.addEventListener("click", () => {
    if (event.target.tagName === "LI") {
        event.target.remove();
        console.log("Tarefa removida: ", event.target.textContent)
    }
  })

});
