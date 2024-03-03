function findMatches(text) {
    let matches = text.match(/#[A-Za-z]+/g)

    for (let match of matches) {
        match = match.replace('#', '')
        console.log(match)
    }
}
