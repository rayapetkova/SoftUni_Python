function getInfo() {
    const baseURL = 'http://localhost:3030/jsonstore/bus/businfo/'

    let stopID = document.getElementById('stopId')
    let stopNameElement = document.getElementById('stopName')
    let ulElement = document.getElementById('buses')

    fetch(baseURL + stopID.value)
        .then(response => response.json())
        .then(data => {
            stopNameElement.textContent = data.name
            ulElement.innerHTML = ''

            for (let key of Object.keys(data.buses)) {
                let liElement = document.createElement('li')
                liElement.textContent = `Bus ${key} arrives in ${data.buses[key]} minutes`
                ulElement.appendChild(liElement)
            }
        })
        .catch(() => {
            stopNameElement.textContent = 'Error'
        })
}