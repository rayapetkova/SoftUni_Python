function findWords(wordsArr) {
    let searchWords = wordsArr[0].split(' ')
    let searchWordsObj = {}

    for (let word1 of searchWords) {
        searchWordsObj[word1] = 0
        for (let word2 of wordsArr.slice(1)) {
            if (word1 === word2) {
                searchWordsObj[word1] += 1
            }
        }
    }

    for (let [key, value] of Object.entries(searchWordsObj).sort((a, b) => b[1] - a[1])) {
        console.log(`${key} - ${value}`)
    }
}
