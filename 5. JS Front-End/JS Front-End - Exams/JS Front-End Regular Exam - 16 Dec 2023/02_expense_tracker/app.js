window.addEventListener("load", solve);

function solve() {
    let addButton = document.getElementById('add-btn')
    addButton.addEventListener('click', addNewExpenseEvent)

    let expenseTypeElement = document.getElementById('expense')
    let amountElement = document.getElementById('amount')
    let dateElement = document.getElementById('date')

    let ulPreviewList = document.getElementById('preview-list')
    let ulExpensesList = document.getElementById('expenses-list')

    let deleteButton = document.querySelector('#expenses button')
    deleteButton.addEventListener('click', deleteExpensesEvent)

    function addNewExpenseEvent(event) {
        let [expenseType, amount, date] = [expenseTypeElement.value, amountElement.value, dateElement.value]

        let li = document.createElement('li')
        li.className = 'expense-item'

        // First
        let article = document.createElement('article')

        let p1 = document.createElement('p')
        p1.textContent = `Type: ${expenseType}`

        let p2 = document.createElement('p')
        p2.textContent = `Amount: ${amount}$`

        let p3 = document.createElement('p')
        p3.textContent = `Date: ${date}`

        article.appendChild(p1)
        article.appendChild(p2)
        article.appendChild(p3)

        // Second
        let buttonsDiv = document.createElement('div')
        buttonsDiv.className = 'buttons'

        let editButton = document.createElement('button')
        editButton.className = 'btn edit'
        editButton.textContent = 'edit'
        editButton.addEventListener('click', editExpenseEvent)

        let okButton = document.createElement('button')
        okButton.className = 'btn ok'
        okButton.textContent = 'ok'
        okButton.addEventListener('click', okButtonEvent)

        buttonsDiv.appendChild(editButton)
        buttonsDiv.appendChild(okButton)

        // Final
        li.appendChild(article)
        li.appendChild(buttonsDiv)

        ulPreviewList.appendChild(li)

        expenseTypeElement.value = ''
        amountElement.value = ''
        dateElement.value = ''

        addButton.disabled = true

        function editExpenseEvent(event) {
            li.remove()

            expenseTypeElement.value = expenseType
            amountElement.value = amount
            dateElement.value = date

            addButton.disabled = false
        }

        function okButtonEvent(event) {
            li.remove()

            let newLi = document.createElement('li')
            li.className = 'expense-item'

            // First
            let article = document.createElement('article')

            let p1 = document.createElement('p')
            p1.textContent = `Type: ${expenseType}`

            let p2 = document.createElement('p')
            p2.textContent = `Amount: ${amount}`

            let p3 = document.createElement('p')
            p3.textContent = `Date: ${date}`

            article.appendChild(p1)
            article.appendChild(p2)
            article.appendChild(p3)

            // Final
            newLi.appendChild(article)

            let deleteButton = document.createElement('button')
            deleteButton.className = 'btn delete'
            deleteButton.textContent = 'Delete'

            ulExpensesList.appendChild(newLi)

            addButton.disabled = false
        }
    }

    function deleteExpensesEvent(event) {
        location.reload()
    }
}