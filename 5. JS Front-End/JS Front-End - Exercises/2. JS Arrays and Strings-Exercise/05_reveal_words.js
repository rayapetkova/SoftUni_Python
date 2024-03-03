function revealWords(wordsStr, text) {
    wordsArr = wordsStr.split(', ')

    for (let word of wordsArr) {
        text = text.replace('*'.repeat(word.length), word)
    }

    console.log(text)
}
