// task1
function ucFirst(str) {
    if(!str) return str;
    return str[0].toUpperCase() + str.slice(1);
}
console.log(ucFirst("john"));

//task2
function checkSpam(str) {
    let lowerStr = str.toLowerCase();
    return lowerStr.includes('viagra') || lowerStr.includes('xxx');

}
console.log(checkSpam('buy ViAgRa now'));
console.log(checkSpam('free qwqww'));
console.log(checkSpam('innocent rabbit'));

//task 3
function truncate(str, maxlength) {
    return (str.length > maxlength) ?
    str.slice(0, maxlength - 1) + '' : str;
}

//task4.
function extractCurrencyVakue(str) {
    return +str.slice(1);
}