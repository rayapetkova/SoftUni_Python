function calculateDifference(numbers) {
    evenSum = 0
    oddSum = 0
    
    for (let i=0; i<numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenSum += numbers[i]
        } else {
            oddSum += numbers[i]
        }
    }
    
    console.log(evenSum - oddSum)
}