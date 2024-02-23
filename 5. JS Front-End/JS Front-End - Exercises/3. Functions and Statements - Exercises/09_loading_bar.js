function printLoadingBar(number) {
    let loadingBar = Array(10).fill('.')
    loadingBar.fill('%', 0, number / 10)

    if (number === 100) {
        console.log('100% Complete!')
        console.log(`[${loadingBar.join('')}]`)
    } else {
        console.log(`${number}% [${loadingBar.join('')}]`)
        console.log('Still loading...')
    }
}
