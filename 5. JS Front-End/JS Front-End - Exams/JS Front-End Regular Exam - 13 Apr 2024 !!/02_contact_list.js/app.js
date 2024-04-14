window.addEventListener("load", solve);

function solve() {
    let addButton = document.getElementById('add-btn')
    addButton.addEventListener('click', addNewContact)

    let nameInput = document.getElementById('name')
    let phoneInput = document.getElementById('phone')
    let categoryInput = document.getElementById('category')

    let ulCheckList = document.getElementById('check-list')
    let ulContactList = document.getElementById('contact-list')

    function addNewContact(event) {
        event.preventDefault()

        if (!nameInput.value || !phoneInput.value || !categoryInput.value) {
            return
        }

        let li = document.createElement('li')

        // First
        let article = document.createElement('article')

        let p1 = document.createElement('p')
        let name = nameInput.value
        p1.textContent = `name:${name}`

        let p2 = document.createElement('p')
        let phone = phoneInput.value
        p2.textContent = `phone:${phone}`

        let p3 = document.createElement('p')
        let category = categoryInput.value
        p3.textContent = `category:${category}`

        article.appendChild(p1)
        article.appendChild(p2)
        article.appendChild(p3)

        // Second
        let buttonsDiv = document.createElement('div')
        buttonsDiv.className = 'buttons'

        let editButton = document.createElement('button')
        editButton.className = 'edit-btn'
        editButton.addEventListener('click', editContactEvent)
        
        let saveButton = document.createElement('button')
        saveButton.className = 'save-btn'
        saveButton.addEventListener('click', saveContactEvent)

        buttonsDiv.appendChild(editButton)
        buttonsDiv.appendChild(saveButton)

        // Final
        li.appendChild(article)
        li.appendChild(buttonsDiv)

        ulCheckList.appendChild(li)

        nameInput.value = ''
        phoneInput.value = ''
        categoryInput.value = ''

        function editContactEvent(event) {
            li.remove()

            nameInput.value = name
            phoneInput.value = phone
            categoryInput.value = category
        }

        function saveContactEvent(event) {
            li.remove()

            let li1 = document.createElement('li')

            // First
            let article = document.createElement('article')

            let p1 = document.createElement('p')
            p1.textContent = `name:${name}`

            let p2 = document.createElement('p')
            p2.textContent = `phone:${phone}`

            let p3 = document.createElement('p')
            p3.textContent = `category:${category}`

            article.appendChild(p1)
            article.appendChild(p2)
            article.appendChild(p3)

            // Second
            let deleteButton = document.createElement('button')
            deleteButton.className = 'del-btn'
            deleteButton.addEventListener('click', deleteContactEvent)

            li1.appendChild(article)
            li1.appendChild(deleteButton)

            ulContactList.appendChild(li1)

            function deleteContactEvent(event) {
                li1.remove()
            }
        }
    }
}
  