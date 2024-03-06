function editElement(element, current, replacement) {
    while (element.textContent.includes(current)) {
        element.textContent = element.textContent.replace(current, replacement)
    }   
}