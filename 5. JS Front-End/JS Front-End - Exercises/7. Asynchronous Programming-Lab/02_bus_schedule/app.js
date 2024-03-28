function solve() {
    const baseURL = 'http://localhost:3030/jsonstore/bus/schedule/'

    let infoBox = document.querySelector('.info')
    let departButton = document.getElementById('depart')
    let arriveButton = document.getElementById('arrive')

    let stopId = 'depot'
    let nextStop = ''

    function depart() {
        fetch(baseURL + stopId)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                infoBox.textContent = `Next stop ${data.name}`
                nextStop = data.name
                stopId = data.next
                departButton.disabled = true
                arriveButton.disabled = false
            })
            .catch((error) => {
                infoBox.textContent = "Error"
                departButton.disabled = true
                arriveButton.disabled = true
            })
    }

    async function arrive() {
        infoBox.textContent = `Arriving at ${nextStop}`
        departButton.disabled = false
        arriveButton.disabled = true
    }

    return {
        depart,
        arrive
    };
}

let result = solve();