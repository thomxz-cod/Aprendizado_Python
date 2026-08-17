document.addEventListener("DOMContentLoaded", function () {

  const caixas = {
    "caixa1" : document.getElementById("caixa1"),
    "caixa2" : document.getElementById("caixa2"),
    "caixa3" : document.getElementById("caixa3")
  }
  
  const cores = [
    // Azuis
    "linear-gradient(135deg, #3b82f6, #1d4ed8)",
    "linear-gradient(135deg, #06b6d4, #0891b2)",
    "linear-gradient(135deg, #6366f1, #4338ca)",
    
    // Vermelhos e Rosas
    "linear-gradient(135deg, #ef4444, #b91c1c)",
    "linear-gradient(135deg, #ec4899, #be185d)",
    "linear-gradient(135deg, #f43f5e, #be123c)",

    // Verdes
    "linear-gradient(135deg, #10b981, #047857)",
    "linear-gradient(135deg, #84cc16, #4d7c0f)",
    "linear-gradient(135deg, #14b8a6, #0f766e)",

    // Amarelos e Laranjas
    "linear-gradient(135deg, #f59e0b, #b45309)",
    "linear-gradient(135deg, #f97316, #c2410c)",
    "linear-gradient(135deg, #eab308, #a16207)",

    // Roxos e Violetas
    "linear-gradient(135deg, #a855f7, #6b21a8)",
    "linear-gradient(135deg, #8b5cf6, #6d28d9)",
    "linear-gradient(135deg, #d946ef, #a21caf)",

    // Escuros e Neutros
    "linear-gradient(135deg, #64748b, #334155)",
    "linear-gradient(135deg, #475569, #0f172a)",
    "linear-gradient(135deg, #71717a, #27272a)"
  ];


  caixas["caixa1"].addEventListener("click", () => {
    let numeroAleatorio = Math.floor(Math.random() * cores.length);
    caixas["caixa1"].style.background = cores[numeroAleatorio]
    console.log("Caixa clicada: Caixa ", this);
  })

  caixas["caixa2"].addEventListener("click", () => {
    let numeroAleatorio = Math.floor(Math.random() * cores.length);
    caixas["caixa2"].style.background = cores[numeroAleatorio]
    console.log("Caixa clicada: Caixa ", this);
  })

  caixas["caixa3"].addEventListener("click", () => {
    let numeroAleatorio = Math.floor(Math.random() * cores.length);
    caixas["caixa3"].style.background = cores[numeroAleatorio]
    console.log("Caixa clicada: Caixa ", this);
  })

})