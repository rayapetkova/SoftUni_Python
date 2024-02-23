function checkPerfectNumber(number) {
    numbersArray = []
    numbersSum = 0

    for (let i = 0; i < number; i++) {
        if (number % i === 0) {
            numbersArray.push(i)
        }
    }

    for (let num of numbersArray) {
        numbersSum += num
    }

    if (numbersSum === number) {
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.")
    }
}






// Test code
// checkPerfectNumber(6)
// checkPerfectNumber(1236498)