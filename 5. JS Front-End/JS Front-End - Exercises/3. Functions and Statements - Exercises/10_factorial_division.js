function calculateDivision(firstNum, secondNum) {
    firstResult = 1
    secondResult = 1

    for (let i = 1; i < firstNum + 1; i++) {
        firstResult *= i
    }

    for (let j = 1; j < secondNum + 1; j++) {
        secondResult *= j
    }

    console.log((firstResult / secondResult).toFixed(2))
}







// Test code
// calculateDivision(5, 2)
// calculateDivision(6, 2)