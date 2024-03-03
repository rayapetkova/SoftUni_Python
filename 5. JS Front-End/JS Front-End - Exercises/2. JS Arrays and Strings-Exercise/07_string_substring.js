function checkSubstring(word, text) {
    allWords = text.split(' ')

    for (let word1 of allWords) {
        let pattern = new RegExp(`^${word.toLowerCase()}$`, 'g')
        if (word1.toLowerCase().match(pattern)) {
            console.log(word)
            return
        }
    }
    
    console.log(`${word} not found!`)
}
