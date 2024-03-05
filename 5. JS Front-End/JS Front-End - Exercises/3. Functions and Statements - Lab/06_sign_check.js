function typeOfNumberResult(num1, num2, num3) {
    let multiply = (a, b) => a * b

    if (multiply(multiply(num1, num2), num3) < 0) {
        return 'Negative'
    } else {
        return 'Positive'
    }
}