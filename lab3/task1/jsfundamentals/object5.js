function makeUser() {
    return {
        name: "John",
        ref: this
    };
}

let users = makeUser();

console.log(user.ref.name);

function makeUser() {
    return {
        name: "John",
        ref() {
            return this;
        }
    };
}

let user = makeUser();
console.log(user.ref().name); 


let calculator = {
    read() {
        let a = +prompt("a?", '');
        let b = +prompt("b?", '')
    },
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    }
};
calculator.read();
console.log(calculator.sum())
console.log(calculator.mul())
