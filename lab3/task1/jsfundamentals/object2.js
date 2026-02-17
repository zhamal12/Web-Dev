let schedule = {};

function isEmpty(schedule) {
    for(let key in schedule) {
        return false;
    }
    return true;
}

console.log(isEmpty(schedule))

schedule["8:30"] = "go to school";

console.log(isEmpty(schedule))