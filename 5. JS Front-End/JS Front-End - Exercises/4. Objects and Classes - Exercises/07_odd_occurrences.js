function findOddOccurrences(strWords) {
    let words = strWords.split(' ')
    let wordsObj = {}

    words.forEach(word => {
        let wordLower = word.toLowerCase()

        if (Object.keys(wordsObj).includes(wordLower)) {
            wordsObj[wordLower] += 1
        } else {
            wordsObj[wordLower] = 1
        }
    });

    let finalResult = []
    for (let key of Object.keys(wordsObj)) {
        if (wordsObj[key] % 2 !== 0) {
            finalResult.push(key)
        }
    }

    console.log(finalResult.join(' '))
}