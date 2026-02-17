const prompt = require("prompt-sync")();

let login = prompt();
let message = (login == "Employee") ? "Hello" : (login == "Director") ?"Greetings" : (login == '') ? 'No login' : "";

console.log(message)