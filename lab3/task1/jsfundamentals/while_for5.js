let i = 0;
while(i < 3){
    console.log(`number ${i++}`)
}

const prompt = require("prompt-sync")();

let q = parseInt(prompt());
for(let i = 0; i <= 10; i++){
    console.log(`${q} * ${i} = ${q * i}`)

}