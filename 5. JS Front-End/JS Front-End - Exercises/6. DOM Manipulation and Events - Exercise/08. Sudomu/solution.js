function solve() {
    function sumNumbers(a, b, c) {
        return a + b + c
    }

    let rows = Array.from(document.querySelectorAll('tbody tr'))

    let tableElement = document.querySelector('table')
    let checkParagraphElement = document.querySelector('#check p')

    let quickCheckButton = document.querySelector('tfoot tr td button')
    quickCheckButton.addEventListener('click', checkSudomuEvent)

    let clearButton = Array.from(document.querySelectorAll('tfoot tr td button'))[1]
    clearButton.addEventListener('click', clearButtonEvent)

    function checkSudomuEvent(event) {
        let correctSum = true
        let columns = [[], [], []]

        for (let row of rows) {
            let threeTableDatasInputs = Array.from(row.querySelectorAll('td input'))
            first = Number(threeTableDatasInputs[0].value)
            second = Number(threeTableDatasInputs[1].value)
            third = Number(threeTableDatasInputs[2].value)

            columns[0].push(first)
            columns[1].push(second)
            columns[2].push(third)

            let sumOfThreeNumbers = sumNumbers(first, second, third)
            
            if (sumOfThreeNumbers !== 6) {
                correctSum = false
                break
            }
        }

        for (let column of columns) {
            console.log(column)
            let sumOfThreeNumbers = sumNumbers(column[0], column[1], column[2])
            
            if (sumOfThreeNumbers !== 6) {
                correctSum = false
                break
            }
        }

        if (correctSum) {
            tableElement.style.border = "2px solid green"
            checkParagraphElement.textContent = "You solve it! Congratulations!"
            checkParagraphElement.style.color = "green"
        } else {
            tableElement.style.border = "2px solid red"
            checkParagraphElement.textContent = "NOP! You are not done yet..."
            checkParagraphElement.style.color = "red"
        }
    }

    function clearButtonEvent(event) {
        for (let row of rows) {
            let currentRowInputs = Array.from(row.querySelectorAll('td input'))
            
            for (let currInput of currentRowInputs) {
                currInput.value = ''
            }
        }
        
        tableElement.style.border = ''
        checkParagraphElement.textContent = ''
    }
}
