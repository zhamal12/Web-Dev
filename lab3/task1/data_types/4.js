//task1.
let fruits = ["apple", "banana", "orange"];

let shoppingCart = fruits;
shoppingCart.push("watermelon")
console.log(shoppingCart)

//task2.
let styles = ["jazz", "blues"];
styles.push("vocal");
styles[Math.floor((styles.length - 1) / 2)] = "classics";
console.log(styles.shift());
styles.unshift("rap", "reggae");
console.log(styles)

//task3.
let arr = ['a', 'b']
arr.push(function() {
    console.log(this)
})
arr[2]();

//task4.sum
function sumInput() {
    let numbers = [];
    while(true) {
        let value = prompt("A number please?", 0);
        if(value === "" || value === null || !isFinite(value)) break;
        numbers.push(+value);
    }
    let sum = 0;
    for (let number of numbers) {
        sum += number;
    }
    return sum;
}
console.log(sumInput());

//task5
function getMaxSubSum(arr) {
    let maxSum = 0;
    let partialSum = 0;
    for (let item of arr) {
      partialSum += item; 
      maxSum = Math.max(maxSum, partialSum); 
      if (partialSum < 0) partialSum = 0; 
    }
    return maxSum;
  }
  alert( getMaxSubSum([-1, 2, 3, -9]) ); 
  alert( getMaxSubSum([-1, 2, 3, -9, 11]) ); 
  alert( getMaxSubSum([-2, -1, 1, 2]) ); 
  alert( getMaxSubSum([100, -9, 2, -3, 5]) ); 
  alert( getMaxSubSum([1, 2, 3]) ); 
  alert( getMaxSubSum([-1, -2, -3]) ); 