function evenAndOddsums(number) {
    strNumber = number.toString()

    oddSum = 0
    evenSum = 0

    for (let digit of strNumber) {
        let numDigit = Number(digit)

        if (numDigit % 2 !== 0) {
            oddSum += numDigit
        } else {
            evenSum += numDigit
        }
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}







// Test code
// console.log(evenAndOddsums(1000435))