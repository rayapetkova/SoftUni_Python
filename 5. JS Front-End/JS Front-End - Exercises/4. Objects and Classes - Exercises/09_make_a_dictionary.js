function makeDictionary(terms) {
    let objectTerms = {}

    for (let term of terms) {
        termObject = JSON.parse(term)
        objectTerms[Object.keys(termObject)[0]] = Object.values(termObject)[0]
    }

    for ([key, value] of Object.entries(objectTerms).sort()) {
        console.log(`Term: ${key} => Definition: ${value}`)
    }
}
