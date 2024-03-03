function splitString(text) {
    let pattern = /([A-Z]{1}[^A-Z]*)/g
    let matches = text.match(pattern)
    console.log(matches.join(', '))
}


splitString('SplitMeIfYouCanHaHaYouCantOrYouCan')