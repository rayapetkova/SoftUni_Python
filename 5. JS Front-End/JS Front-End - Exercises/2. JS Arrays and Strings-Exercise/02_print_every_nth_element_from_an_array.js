function everyNthNumber(currArray, number) {

    finalResult = []

    for (let index = 0; index < currArray.length; index++) {
        if (index % number === 0){
            finalResult.push(currArray[index])
        }
    }

    return finalResult
}
