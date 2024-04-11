function cafeteriaManagement(commands) {
    let numBaristas = Number(commands.shift())
    let team = {}

    for (let i = 0; i < numBaristas; i++) {
        let person = commands.shift().split(' ')
        let [personName, shift, coffeeTypes] = person
        team[personName] = [shift, coffeeTypes.split(',')]
    }

    for (let command of commands) {
        if (command === 'Closed') {
            for (let key of Object.keys(team)) {
                console.log(`Barista: ${key}, Shift: ${team[key][0]}, Drinks: ${team[key][1].join(', ')}`)
            }
        }

        let commandArr = command.split(' / ')

        if (commandArr.includes('Prepare')) {
            commandArr.shift()
            let [name, shift, coffeeType] = commandArr

            if (team[name][0] === shift && team[name][1].includes(coffeeType)) {
                console.log(`${name} has prepared a ${coffeeType} for you!`)
            } else {
                console.log(`${name} is not available to prepare a ${coffeeType}.`)
            }
        } else if (commandArr.includes('Change Shift')) {
            commandArr.shift()
            let [name, newShift] = commandArr
            team[name][0] = newShift
            console.log(`${name} has updated his shift to: ${newShift}`)
        } else if (commandArr.includes('Learn')) {
            commandArr.shift()
            let [name, newCoffeeType] = commandArr
            
            if (team[name][1].includes(newCoffeeType)) {
                console.log(`${name} knows how to make ${newCoffeeType}.`)
            } else {
                team[name][1].push(newCoffeeType)
                console.log(`${name} has learned a new coffee type: ${newCoffeeType}.`)
            }
        }
    }
}

cafeteriaManagement([
    '3',
      'Alice day Espresso,Cappuccino',
      'Bob night Latte,Mocha',
      'Carol day Americano,Mocha',
      'Prepare / Alice / day / Espresso',
      'Change Shift / Bob / night',
      'Learn / Carol / Latte',
      'Learn / Bob / Latte',
      'Prepare / Bob / night / Latte',
      'Closed'
    ])
    