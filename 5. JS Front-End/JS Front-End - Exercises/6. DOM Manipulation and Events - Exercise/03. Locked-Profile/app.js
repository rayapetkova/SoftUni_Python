function lockedProfile() {
    let radioButtons = Array.from(document.querySelectorAll('.profile input[type="radio"]'))
    
    for (let button of radioButtons) {
        let showMoreButton = button.parentNode.querySelector('button')
        showMoreButton.addEventListener('click', showMoreButtonEvent)
    }

    function showMoreButtonEvent(e) {
        let hiddentFields = e.currentTarget.parentNode.querySelector('div')
        let unlockRadioButton = e.currentTarget.parentNode.querySelectorAll('input[type="radio"]')[1]

        if (e.currentTarget.textContent === 'Show more') {
            if (unlockRadioButton.checked) {
                hiddentFields.style.display = 'block'
                e.currentTarget.textContent = 'Hide it'
            } 
        } else {
            if (unlockRadioButton.checked) {
                hiddentFields.style.display = 'none'
                e.currentTarget.textContent = 'Show more'
            }
        }
    }
}