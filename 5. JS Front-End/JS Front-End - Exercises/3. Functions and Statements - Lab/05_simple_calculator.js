function calculate(num1, num2, operator) {

    let operators = {
        multiply: (firstNum, secondNum) => firstNum * secondNum,
        divide: (firstNum, secondNum) => firstNum / secondNum,
        add: (firstNum, secondNum) => firstNum + secondNum,
        subtract: (firstNum, secondNum) => firstNum - secondNum,
    }

    return operators[operator](num1, num2)

}





// Test code:
// console.log(calculate(1, 2, 'add'))