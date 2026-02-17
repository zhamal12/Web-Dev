const prompt = require("prompt-sync")();


let a = parseInt(prompt("A: "))
let b = parseInt(prompt("B: "))


let result = (a + b < 4) ? 'Bellow' : 'Over';
console.log(result)