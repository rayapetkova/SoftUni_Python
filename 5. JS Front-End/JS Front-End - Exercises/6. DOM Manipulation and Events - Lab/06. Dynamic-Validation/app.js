function validate() {
    let inputField = document.getElementById('email')
    inputField.addEventListener('change', onChangeEvent)

    let regexPattern = /[a-z]+@[a-z]+\.[a-z]+/g

    function onChangeEvent(e) {
        let currentValue = e.currentTarget.value
        if (!currentValue.match(regexPattern)) {
            e.currentTarget.className = 'error'
        } else {
            e.currentTarget.classList.remove('error')
        }
    }
}