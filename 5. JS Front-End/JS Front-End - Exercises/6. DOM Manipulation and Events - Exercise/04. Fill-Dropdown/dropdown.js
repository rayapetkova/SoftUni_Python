function addItem() {
    let selectDropdown = document.getElementById('menu')
    
    let itemText = document.getElementById('newItemText')
    let itemValue = document.getElementById('newItemValue')

    let option = document.createElement('option')
    option.textContent = itemText.value
    option.value = itemValue.value

    selectDropdown.appendChild(option)

    itemText.value = ''
    itemValue.value = ''
}