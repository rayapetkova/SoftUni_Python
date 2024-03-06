function extractText() {
    let content = Array.from(document.querySelectorAll('ul li'))
    let finalTextarea = document.getElementById('result')

    let contentArr = []
    for (element of content) {
        contentArr.push(element.textContent)
    }

    finalTextarea.value = contentArr.join('\n')
}