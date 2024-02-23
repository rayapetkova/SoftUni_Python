function printMatrix(number) {
    for (let i = 0; i < number; i++) {
        row_nums = Array(number).fill(number)
        console.log(row_nums.join(' '))
    }
}






// Test code
// printMatrix(3)