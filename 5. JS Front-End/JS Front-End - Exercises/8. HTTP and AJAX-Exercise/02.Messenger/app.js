function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/messenger'
    
    let sendButton = document.getElementById('submit')
    sendButton.addEventListener('click', sendMessageEvent)

    let refreshButton = document.getElementById('refresh')
    refreshButton.addEventListener('click', refreshEvent)

    let textareaResult = document.querySelector('textarea')

    function sendMessageEvent(event) {
        let author = document.getElementsByName('author')[0].value
        let content = document.getElementsByName('content')[0].value

        let message = {
            author,
            content
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(message)
        })
    }

    async function refreshEvent(event) {
        textareaResult.textContent = ''

        let messagesResponse = await fetch(baseURL)
        let messages = await messagesResponse.json()

        let messagesArr = []
        for (let messageElement of Object.entries(messages)) {
            let messageObj = messageElement[1]
            messagesArr.push(`${messageObj.author}: ${messageObj.content}`)
        }

        textareaResult.textContent = messagesArr.join('\n')
    }
}

attachEvents();