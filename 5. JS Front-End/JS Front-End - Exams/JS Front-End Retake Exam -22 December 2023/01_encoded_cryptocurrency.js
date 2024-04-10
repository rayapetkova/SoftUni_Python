function decodeMessage(commands) {
    let message = commands.shift()

    for (let command of commands) {
        if (command === 'Buy') {
            console.log(`The cryptocurrency is: ${message}`)
        }

        if (command === 'TakeEven') {
            let newMessage = ''

            for (let i = 0; i < message.length; i++) {
                if (i % 2 === 0) {
                    newMessage += message[i]
                }
            }

            message = newMessage
            console.log(message)
        }

        let commandArr = command.split('?')
        if (commandArr.includes('ChangeAll')) {
            let [substring, replacement] = [commandArr[1], commandArr[2]]
            message = message.split(substring).join(replacement)
            console.log(message)
        } else if (commandArr.includes('Reverse')) {
            let substring = commandArr[1]

            if (message.includes(substring)) {
                let reversedSubstring = substring.split('').reverse().join('')
                message = message.replace(substring, '')
                message += reversedSubstring
                console.log(message)
            } else {
                console.log('error')
            }
        }
    }
}
