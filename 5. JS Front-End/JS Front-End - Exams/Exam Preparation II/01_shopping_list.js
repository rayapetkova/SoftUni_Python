function shoppingListManagement(commands) {
    let groceries = commands.shift().split('!')
    
    for (let command of commands) {
        let commandArr = command.split(' ')

        if (commandArr.includes('Urgent')) {
            let item = commandArr[1]

            if (!groceries.includes(item)) {
                groceries.unshift(item)
            }
        } else if (commandArr.includes('Unnecessary')) {
            let item = commandArr[1]

            if (groceries.includes(item)) {
                groceries = groceries.filter((element) => element != item)
            }
        } else if (commandArr.includes('Correct')) {
            let oldItemIndex = groceries.indexOf(commandArr[1])
            let newItem = commandArr[2]

            if (oldItemIndex >= 0) {
                groceries[oldItemIndex] = newItem
            }
        } else if (commandArr.includes('Rearrange')) {
            let indexItem = groceries.indexOf(commandArr[1])

            if (groceries.includes(commandArr[1])) {
                groceries.splice(indexItem, 1)
                groceries.push(commandArr[1])
            }
        }
    }

    console.log(groceries.join(', '))
}
