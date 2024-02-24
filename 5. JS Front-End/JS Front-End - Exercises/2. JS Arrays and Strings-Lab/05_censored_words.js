function censoreWord(text, word) {

    occurencies = text.split(word).length - 1

    for (let i = 0; i < occurencies; i++) {
        text = text.replace(word, '*'.repeat(word.length))
    }

    console.log(text)
}
