function pointsValidation(points) {
    [x1, y1, x2, y2] = points

    function checkValidDistance(x1, y1, x2, y2) {
        if (Number.isInteger(Math.sqrt((x2 - x1)**2 + (y2 - y1)**2))) {
            return 'valid'
        }

        return 'invalid'  
    }

    let firstValidation = checkValidDistance(x1, y1, 0, 0)
    console.log(`{${x1}, ${y1}} to {0, 0} is ${firstValidation}`)

    let secondValidation = checkValidDistance(x2, y2, 0, 0)
    console.log(`{${x2}, ${y2}} to {0, 0} is ${secondValidation}`)

    let thirdValidation = checkValidDistance(x1, y1, x2, y2)
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${thirdValidation}`)
}