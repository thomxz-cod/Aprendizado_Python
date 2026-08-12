const nome_player = "Thomaz Erick";
let idade = 18;
let status = true; 
let game_fav = {nome: nome_player, game_fav: "Call of Duty"};
let pontuacoes = [89, 43, 98]

console.log("Dados do player")
console.log(nome_player, typeof nome_player)
console.log(idade, typeof idade)
console.log(status, typeof status)
console.log(game_fav, typeof game_fav)
console.log(pontuacoes, typeof pontuacoes)

console.log("\nAlterado:\n")

idade = 19;
status = false;

console.log(idade, typeof idade);
console.log(status, typeof status);

console.log("\nMedia: ");

let soma = 0;
for (let pontuacao of pontuacoes) {
    soma += pontuacao;
}

let media = (soma / pontuacoes.length);

console.log(media.toFixed(2));