
function solve() {
    const baseURL = 'http://localhost:3030/jsonstore/tasks/'

    let loadHistoryButton = document.getElementById('load-history')
    loadHistoryButton.addEventListener('click', loadHistoryEvent)

    let listElement = document.getElementById('list')

    let addWeatherButton = document.getElementById('add-weather')
    addWeatherButton.addEventListener('click', addWeatherEvent)

    let editWeatherButton = document.getElementById('edit-weather')

    let locationInput = document.getElementById('location')
    let temperatureInput = document.getElementById('temperature')
    let dateInput = document.getElementById('date')

    async function loadHistoryEvent(event) {
        let historyResponse = await fetch(baseURL)
        let history = await historyResponse.json()

        listElement.innerHTML = ''

        for (let town of Object.values(history)) {
            let div = document.createElement('div')
            div.className = 'container'
            
            // First
            let h2 = document.createElement('h2')
            let location = town.location
            h2.textContent = location

            let h3Date = document.createElement('h3')
            let date = town.date
            h3Date.textContent = date

            let h3Temperature = document.createElement('h3')
            let temperature = town.temperature
            h3Temperature.textContent = temperature
            h3Temperature.id = 'celsius'

            // Second
            let buttonsDiv = document.createElement('div')
            buttonsDiv.id = 'buttons-container'

            let changeButton = document.createElement('button')
            changeButton.className = 'change-btn'
            changeButton.textContent = 'Change'
            changeButton.addEventListener('click', changeWeatherEvent)

            let deleteButton = document.createElement('button')
            deleteButton.className = 'delete-btn'
            deleteButton.textContent = 'Delete'
            deleteButton.addEventListener('click', deleteWeatherEvent)

            buttonsDiv.appendChild(changeButton)
            buttonsDiv.appendChild(deleteButton)

            // Final
            div.appendChild(h2)
            div.appendChild(h3Date)
            div.appendChild(h3Temperature)
            div.appendChild(buttonsDiv)

            listElement.appendChild(div)
            
            async function changeWeatherEvent(event) {
                div.remove()

                locationInput.value = location
                temperatureInput.value = temperature
                dateInput.value = date

                editWeatherButton.disabled = false
                editWeatherButton.addEventListener('click', editWeatherEvent)
                addWeatherButton.disabled = true

                async function editWeatherEvent(event) {
                    let currItem = {
                        location: locationInput.value,
                        temperature: temperatureInput.value,
                        date: dateInput.value,
                        '_id': town._id
                    }

                    await fetch(baseURL + town._id, {
                        method: 'PUT',
                        body: JSON.stringify(currItem)
                    })

                    loadHistoryEvent()

                    editWeatherButton.disabled = true
                    addWeatherButton.disabled = false

                    locationInput.value = ''
                    temperatureInput.value = ''
                    dateInput.value = ''
                }
            }

            async function deleteWeatherEvent(event) {
                await fetch(baseURL + town._id, {
                    method: 'DELETE'
                })

                loadHistoryEvent()
            }
        }
    }

    async function addWeatherEvent(event) {
        if (!locationInput.value || !temperatureInput.value || !dateInput.value) {
            return
        }

        let [location, temperature, date] = [locationInput.value, temperatureInput.value, dateInput.value]

        let newWeather = {
            location,
            temperature,
            date
        }

        await fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(newWeather)
        })

        loadHistoryEvent()

        locationInput.value = ''
        temperatureInput.value = ''
        dateInput.value = ''
    }
}

solve()