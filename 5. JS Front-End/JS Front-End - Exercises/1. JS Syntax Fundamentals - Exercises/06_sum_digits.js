function sumDigits(num) {
    let str_num = num.toString()
    let total_sum = 0

    for (digit of str_num) {
        total_sum += Number(digit)
    }

    console.log(total_sum)
}
