function numsAndSum(num1, num2) {
    let result = []
    let sum_nums = 0

    for (let i = num1; i <= num2; i++) {
        result.push(i)
    }

    for (let x of result) {
        sum_nums += x
    }

    console.log(result.join(' '))
    console.log(`Sum: ${sum_nums}`)
}

