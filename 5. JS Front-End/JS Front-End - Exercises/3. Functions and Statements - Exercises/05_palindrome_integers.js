function checkPalindromeNumbers(numbers) {
    finalResult = []

    for (let num of numbers) {
        strNum = num.toString()

        if (strNum === strNum.split('').reverse().join('')) {
            finalResult.push(true)
        } else {
            finalResult.push(false)
        }
    }

    return finalResult.join('\n')
}






// Test code
// console.log(checkPalindromeNumbers([123, 323, 421, 121]))