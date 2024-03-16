function addItem() {
    let li = document.createElement('li')
    let a = document.createElement('a')
    a.textContent = '[Delete]'
    a.href = '#'
    a.addEventListener('click', deleteButtonClick)

    let boxContent = document.getElementById('newItemText').value
    li.textContent = boxContent
    li.appendChild(a)

    let ul = document.getElementById('items')
    ul.appendChild(li)

    function deleteButtonClick(e) {
        e.currentTarget.parentNode.remove()
    }
}