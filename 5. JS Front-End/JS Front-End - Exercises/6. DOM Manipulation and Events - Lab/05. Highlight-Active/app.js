function focused() {
    let allInputs = Array.from(document.querySelectorAll('div input'))

    for (let inputBox of allInputs) {
        inputBox.addEventListener('focus', onFocus)
        inputBox.addEventListener('blur', outOfFocus)
    }
    
    function onFocus(e) {
        e.currentTarget.parentNode.className = 'focused'
    }

    function outOfFocus(e) {
        e.currentTarget.parentNode.classList.remove('focused')
    }
}