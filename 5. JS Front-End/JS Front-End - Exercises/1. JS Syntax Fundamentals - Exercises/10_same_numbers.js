function checkSameNumbers(number) {
    let strNumber = number.toString()
    let digitsList = strNumber.split('')

    currSymbol = 0
    equal = true
    
    for (let i = 1; i < digitsList.length; i++) {
        let digit = digitsList[i];
        if (digit !== digitsList[currSymbol]) {
            equal = false
            currSymbol += 1
        }
    }

    console.log(equal)

    totalSum = 0
    for (let digit of digitsList) {
        totalSum += Number(digit)
    }

    console.log(totalSum)
}







// Test code:
// checkSameNumbers(2222222)
// checkSameNumbers(1234)