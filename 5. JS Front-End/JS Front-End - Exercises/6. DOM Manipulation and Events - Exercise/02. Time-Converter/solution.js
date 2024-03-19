function attachEventsListeners() {
    // Buttons
    let daysButton = document.getElementById('daysBtn')
    let hoursButton = document.getElementById('hoursBtn')
    let minutesButton = document.getElementById('minutesBtn')
    let secondsButton = document.getElementById('secondsBtn')

    // Inputs
    let daysInput = document.getElementById('days')
    let hoursInput = document.getElementById('hours')
    let minutesInput = document.getElementById('minutes')
    let secondsInput = document.getElementById('seconds')

    // Listeners
    daysButton.addEventListener('click', daysConverter)
    hoursButton.addEventListener('click', hoursConverter)
    minutesButton.addEventListener('click', minutesConverter)
    secondsButton.addEventListener('click', secondsConverter)

    function daysConverter(e) {
        let days = Number(daysInput.value)
        hoursInput.value = days * 24
        minutesInput.value = days * 1440
        secondsInput.value = days * 86400
    }

    function hoursConverter(e) {
        let hours = Number(hoursInput.value)
        daysInput.value = hours / 24
        minutesInput.value = hours * 60
        secondsInput.value = hours * 3600
    }

    function minutesConverter(e) {
        let minutes = Number(minutesInput.value)
        hoursInput.value = minutes / 60
        daysInput.value = hoursInput.value / 24
        secondsInput.value = minutes * 60
    }

    function secondsConverter(e) {
        let seconds = Number(secondsInput.value)
        minutesInput.value = seconds / 60
        hoursInput.value = minutesInput.value / 60
        daysInput.value = hoursInput.value / 24
    }
}