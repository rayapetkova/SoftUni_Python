function convertWords(text) {
    let textMatch = text.match(/\w+/g)

    finalResult = []
    
    for (let word of textMatch) {
        finalResult.push(word.toUpperCase())
    }

    console.log(finalResult.join(", "))
}
