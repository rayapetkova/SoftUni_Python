function sumTable() {
    let table = document.querySelector('table')
    let lastColumns = Array.from(document.querySelectorAll('td:nth-child(even):not(#sum)'))
    let sumColumnElement = document.getElementById('sum')

    let totalSum = 0
    for (let element of lastColumns) {
        totalSum += Number(element.textContent)
    }

    sumColumnElement.textContent = totalSum
}