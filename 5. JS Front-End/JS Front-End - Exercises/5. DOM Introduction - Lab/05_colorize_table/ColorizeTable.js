function colorize() {
    let rowElements = Array.from(document.querySelectorAll('tr:nth-child(even)'))

    for (let element of rowElements) {
        element.style.backgroundColor = 'Teal'
    }
}