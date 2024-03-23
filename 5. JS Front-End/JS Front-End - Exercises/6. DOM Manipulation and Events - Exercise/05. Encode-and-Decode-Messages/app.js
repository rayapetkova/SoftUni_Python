function encodeAndDecodeMessages() {
    let firstTextArea = document.querySelector('textarea')
    let encodeButton = document.querySelector('button')
    encodeButton.addEventListener('click', encodeMessageEvent)

    let secondTextArea = Array.from(document.querySelectorAll('textarea'))[1]
    let decodeButton = Array.from(document.querySelectorAll('button'))[1]
    decodeButton.addEventListener('click', decodeMessageEvent)

    function encodeMessageEvent(event) {
        let firstMessage = firstTextArea.value
        let encodedMessage = ''

        for (let symbol of firstMessage) {
            let asciiCodeSymbol = symbol.charCodeAt(0)
            let newSymbol = String.fromCharCode(asciiCodeSymbol + 1)
            encodedMessage += newSymbol
        }

        firstTextArea.value = ''
        secondTextArea.value = encodedMessage
    }

    function decodeMessageEvent(event) {
        let secondMessage = secondTextArea.value
        let decodedMessage = ''

        for (let symbol of secondMessage) {
            let asciiCodeSymbol = symbol.charCodeAt(0)
            let newSymbol = String.fromCharCode(asciiCodeSymbol - 1)
            decodedMessage += newSymbol
        }

        secondTextArea.value = decodedMessage
    }
    
}