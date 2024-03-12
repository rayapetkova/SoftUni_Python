function generateReport() {
    let checkBoxes = Array.from(document.querySelectorAll('thead input'))

    let checkedCheckBoxes = []
    let checkedCheckBoxesObj = {}
    for (let index = 0; index < checkBoxes.length; index++) {
        let checkBoxElement = checkBoxes[index]
        let columnName = checkBoxElement.name

        if (checkBoxElement.checked) {
            checkedCheckBoxes.push([index, columnName])
            checkedCheckBoxesObj[columnName] = []
        }
    }

    let tableRows = Array.from(document.querySelectorAll('table tbody tr'))
    for (let checkBoxArr of checkedCheckBoxes) {
        let [indexColumn, nameColumn] = checkBoxArr
        
        for (let row of tableRows) {
            checkedCheckBoxesObj[nameColumn].push(row.children[indexColumn].textContent)
        }
    }

    console.log(checkedCheckBoxesObj)
    let finalResult = []
    if (Object.keys(checkedCheckBoxesObj).length) {
        let firstObjElement = Object.keys(checkedCheckBoxesObj)[0]
        for (let index = 0; index < checkedCheckBoxesObj[firstObjElement].length; index++) {
            let currentObject = {}
            for (let [column, elementsArr] of Object.entries(checkedCheckBoxesObj)) {
                currentObject[column] = elementsArr[index]
            }

            if (Object.keys(currentObject).length) {
                finalResult.push(currentObject)
            }
        
    }

    let outputTextArea = document.getElementById('output')
    outputTextArea.textContent = JSON.stringify(finalResult)
    }

}