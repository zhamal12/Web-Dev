const prompt = require("prompt-sync")();

let browser = prompt();

if(browser == 'Edge') {
    console.log("You've got the Edge!");
} else if (browser == 'Chrome'
    || browser == 'Firebox'
    || browser == 'Safari'
    || browser == 'Opera') {
        console.log("Okay we support these browesers");
    } else {
        console.log('We hope that this page looks ok!');
    }
