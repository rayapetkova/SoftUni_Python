function calculate(firstNum, operator, secondNum) {
    let operators = {
        '+': (num1, num2) => num1 + num2,
        '-': (num1, num2) => num1 - num2,
        '/': (num1, num2) => num1 / num2,
        '*': (num1, num2) => num1 * num2
    }

    console.log(operators[operator](firstNum, secondNum).toFixed(2))
}
