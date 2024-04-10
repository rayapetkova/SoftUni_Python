function solve() {
    const baseURL = 'http://localhost:3030/jsonstore/gifts/'

    let loadPresentsButton = document.getElementById('load-presents')
    loadPresentsButton.addEventListener('click', loadPresentsEvent)

    let giftListElement = document.getElementById('gift-list')
    let editPresentButton = document.getElementById('edit-present')

    let addGiftButton = document.getElementById('add-present')
    addGiftButton.addEventListener('click', addNewPresent)

    let presentInput = document.getElementById('gift')
    let forInput = document.getElementById('for')
    let priceInput = document.getElementById('price')

    async function loadAllPresents() {
        let presentsResponse = await fetch(baseURL)
        let presents = await presentsResponse.json()

        giftListElement.innerHTML = ''
        for (let present of Object.values(presents)) {
            let mainDiv = document.createElement('div')
            mainDiv.className = 'gift-sock'

            // first
            let contentDiv = document.createElement('div')
            contentDiv.className = 'content'

            let p1 = document.createElement('p')
            p1.textContent = present.gift

            let p2 = document.createElement('p')
            p2.textContent = present.for

            let p3 = document.createElement('p')
            p3.textContent = present.price

            contentDiv.appendChild(p1)
            contentDiv.appendChild(p2)
            contentDiv.appendChild(p3)

            // second
            let buttonsDiv = document.createElement('div')
            buttonsDiv.className = 'buttons-container'

            let changeButton = document.createElement('button')
            changeButton.className = 'change-btn'
            changeButton.textContent = 'Change'
            changeButton.addEventListener('click', changePresent)

            let deleteButton = document.createElement('button')
            deleteButton.className = 'delete-btn'
            deleteButton.textContent = 'Delete'
            deleteButton.addEventListener('click', deleteGiftEvent)

            buttonsDiv.appendChild(changeButton)
            buttonsDiv.appendChild(deleteButton)

            // final
            mainDiv.appendChild(contentDiv)
            mainDiv.appendChild(buttonsDiv)

            giftListElement.appendChild(mainDiv)

            function changePresent(event) {
                presentInput.value = present.gift
                forInput.value = present.for
                priceInput.value = present.price

                editPresentButton.disabled = false
                editPresentButton.addEventListener('click', editPresentEvent)
                addGiftButton.disabled = true
                
                async function editPresentEvent(event) {
                    event.preventDefault()
                    
                    let editedPresentObj = {
                        'gift': presentInput.value,
                        'for': forInput.value,
                        'price': priceInput.value,
                        '_id': present._id
                    }

                    await fetch(baseURL + present._id, {
                        method: 'PUT',
                        body: JSON.stringify(editedPresentObj)
                    })

                    loadAllPresents()
                    editPresentButton.disabled = true
                    addGiftButton.disabled = false
                }
            }

            async function deleteGiftEvent(event) {
                await fetch(baseURL + present._id, {
                    method: 'DELETE'
                })

                loadAllPresents()
            }
        }
    }

    function loadPresentsEvent(event) {
        loadAllPresents()
        editPresentButton.disabled = true
    }

    async function addNewPresent(event) {
        event.preventDefault()

        
        let present = presentInput.value
        let forPerson = forInput.value
        let price = priceInput.value

        let presentObj = {
            'gift': present,
            'for': forPerson,
            'price': price
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(presentObj)
        })

        presentInput.value = ''
        forInput.value = ''
        priceInput.value = ''

        loadAllPresents()
    }
}

solve()