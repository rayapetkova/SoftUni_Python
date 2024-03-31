function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/phonebook'

    let loadButton = document.getElementById('btnLoad')
    loadButton.addEventListener('click', loadPhonesEvent)

    let ulPhonebookElement = document.getElementById('phonebook')

    let createButton = document.getElementById('btnCreate')
    createButton.addEventListener('click', createNewPhoneEvent)

    async function loadPhonesEvent(event) {
        ulPhonebookElement.innerHTML = ''
        let phonesResponse = await fetch(baseURL)
        let phones = await phonesResponse.json()

        for (let phoneInfo of Object.entries(phones)) {
            let key = phoneInfo[0]
            let phoneObj = phoneInfo[1]

            let li = document.createElement('li')
            let deleteButton = document.createElement('button')
            deleteButton.textContent = 'Delete'
            deleteButton.addEventListener('click', deletePhoneEvent)

            li.textContent = `${phoneObj.person}: ${phoneObj.phone}`
            li.appendChild(deleteButton)
            ulPhonebookElement.appendChild(li)

            async function deletePhoneEvent(event) {
                fetch(baseURL + `/${phoneObj._id}`, {
                    method: 'DELETE'
                })

                li.remove()
            }
        }
    }

    async function createNewPhoneEvent(event) {
        let person = document.getElementById('person')
        let phone = document.getElementById('phone')

        let newPhone = {
            person: person.value,
            phone: phone.value
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(newPhone)
        })

        person.value = ''
        phone.value = ''
        loadPhonesEvent()
    }
}

attachEvents();