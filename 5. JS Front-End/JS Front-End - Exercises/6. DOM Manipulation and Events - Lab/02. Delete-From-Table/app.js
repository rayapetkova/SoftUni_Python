function deleteByEmail() {
    let searchEmail = Array.from(document.getElementsByName('email'))[0].value
    let tableRows = document.querySelectorAll('table tbody tr')
    let deleted = false

    for (let row of tableRows) {
        let currentEmail = row.children[1].textContent
        let result = document.getElementById('result')

        if (currentEmail === searchEmail) {
            row.remove()

            result.textContent = 'Deleted'
        } else {
            result.textContent = 'Not found.'
        }
    }
}