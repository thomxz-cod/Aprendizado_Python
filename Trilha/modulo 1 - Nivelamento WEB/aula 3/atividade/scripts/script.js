let preço = 20;
let quantidade = 3.;

let valorTotal = preço * quantidade;

console.log(`Valor total da compra: ${valorTotal}`)
console.log(`Dobro do valor: ${valorTotal * 2}`)
console.log(`Resto da divisão por 2: ${valorTotal % 2}`)

let cupomValido = true;
let freteGratis = false;

if (cupomValido == true && freteGratis == true) {
    console.log("Você possui todos os beneficio!")
} else if (cupomValido == true || freteGratis == true) {
    let beneficio = "";

    if (cupomValido == true){
        beneficio = "Cupom Valido";
    } else if (freteGratis == true) {
        beneficio = "Frete Gratis";
    }

    console.log(`Você possui o beneficio: ${beneficio}!`)
} else {
    console.log("Você não possui nenhum beneficio!")
}