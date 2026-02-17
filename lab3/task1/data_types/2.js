//task1.Sum numbers
const prompt = require("prompt-sync")();

let a = parseInt(prompt("The first number?"))
let b = parseInt(prompt("The second number?"))
console.log(a + b);

//task2.
console.log( (6.35 * 10).toFixed(20) ); 

//task3.
function readNumber() {
    let num;
    do {
        num = prompt("Enter a number please?")
    } while (!isFinite(num));
    if(num == null || num === '') return null;
    return +num;
}
console.log(`Read: ${readNumber()}`);

//task4.
let i = 0
while(i != 10) {
    i += 0.2
}

//task5.
function random(min, max) {
    return min + Math.random() * (max - min);
}
console.log(random(1, 5));
console.log(random(1, 5));
console.log(random(1, 5));

//task.6
function randomInteger(min, max) {
    let rand = min - 0.5 + Math.random() * (max - min + 1);
}

console.log(randomInteger(1, 3))

