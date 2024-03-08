function extract(content) {
    let text = document.querySelector(`#${content}`).textContent
    let matches = text.match(/\((.+?)\)/g)

    let extractedMatches = []
    
    for (let match of matches) {
        match = match.replace('(', '')
        match = match.replace(')', '')

        extractedMatches.push(match)
    }
    
    return extractedMatches.join('; ')
}