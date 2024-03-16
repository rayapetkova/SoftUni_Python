function numberModification(number) {

    function findSum(numsArr) {
        return numsArr.reduce(
            (acc, currentNum) => {
                return acc + Number(currentNum)
            }, 0
        )
    }

    let numbersArr = number.toString().split('')
    let averageValue = findSum(numbersArr) / numbersArr.length

    while (averageValue <= 5) {
        numbersArr.push(9)
        averageValue = findSum(numbersArr) / numbersArr.length
    }

    console.log(numbersArr.join(''))
}