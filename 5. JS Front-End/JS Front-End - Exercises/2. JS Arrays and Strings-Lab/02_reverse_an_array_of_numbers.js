function printNumbers(num, numbers) {
    newArray = numbers.slice(0, num).reverse()
    console.log(newArray.join(' '))
}