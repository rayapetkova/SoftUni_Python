function addItem() {
    let li = document.createElement('li')
    let boxContent = document.getElementById('newItemText').value
    li.textContent = boxContent

    let ul = document.getElementById('items')
    ul.appendChild(li)
}