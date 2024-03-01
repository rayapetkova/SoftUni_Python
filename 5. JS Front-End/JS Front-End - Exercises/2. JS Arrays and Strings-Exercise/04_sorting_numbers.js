function sortNumbers(numbersArray) {
    let sortedArr = numbersArray.sort((a, b) => a - b)
    let finalResult = []

    while (sortedArr.length > 0) {
        let firstNum= sortedArr.shift()
        let lastNum = sortedArr.pop()

        finalResult.push(firstNum, lastNum)
    }
   
    return finalResult
}




console.log(sortNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))