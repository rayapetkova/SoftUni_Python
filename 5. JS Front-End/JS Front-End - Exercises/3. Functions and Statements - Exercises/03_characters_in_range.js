function charsBetween(first_symbol, second_symbol) {
    numFirst = first_symbol.charCodeAt()
    numSecond = second_symbol.charCodeAt()

    lowerNum = 0
    biggerNum = 0

    if (numFirst > numSecond) {
        lowerNum = numSecond
        biggerNum = numFirst
    } else {
        lowerNum = numFirst
        biggerNum = numSecond
    }

    finalResult = []
    for (let i = lowerNum + 1; i < biggerNum; i++) {
        finalResult.push(String.fromCharCode(i))
    }

    return finalResult.join(" ")
}





// Test code
// console.log(charsBetween('a', 'd'))
// console.log(charsBetween('#', ':'))
// console.log(charsBetween('C', '#'))