function astroAdventureSolve(commands) {
    let num = Number(commands.shift())
    let astronauts = {}

    for (let i = 0; i < num; i++) {
        let [astronautName, oxygenLevel, energyReserves] = commands[i].split(' ')
        astronauts[astronautName] = [Number(oxygenLevel), Number(energyReserves)]
    }

    for (let command of commands) {
        if (command === 'End') {
            for (let [key, value] of Object.entries(astronauts)) {
                console.log(`Astronaut: ${key}, Oxygen: ${value[0]}, Energy: ${value[1]}`)
            }

            break
        }

        let commandArr = command.split(' - ')

        if (commandArr.includes('Explore')) {
            let [aName, energy] = [commandArr[1], Number(commandArr[2])]
            
            if (astronauts[aName][1] >= energy) {
                astronauts[aName][1] -= energy
                console.log(`${aName} has successfully explored a new area and now has ${astronauts[aName][1]} energy!`)
            } else {
                console.log(`${aName} does not have enough energy to explore!`)
            }
        } else if (commandArr.includes('Refuel')) {
            let [aName, amount] = [commandArr[1], Number(commandArr[2])]
            let currentEnergy = astronauts[aName][1]
            let amountRecovered = amount
            
            astronauts[aName][1] += amount
            if (astronauts[aName][1] > 200) {
                astronauts[aName][1] = 200
                amountRecovered = 200 - currentEnergy
            }

            console.log(`${aName} refueled their energy by ${amountRecovered}!`)
        } else if (commandArr.includes('Breathe')) {
            let [aName, amount] = [commandArr[1], Number(commandArr[2])]
            let currentOxygen = astronauts[aName][0]
            let amountRecovered = amount

            astronauts[aName][0] += amount
            if (astronauts[aName][0] > 100) {
                astronauts[aName][0] = 100
                amountRecovered = 100 - currentOxygen
            }

            console.log(`${aName} took a breath and recovered ${amountRecovered} oxygen!`)
        }
    }
}

astroAdventureSolve([    '4',
'Alice 60 100',
'Bob 40 80',
'Charlie 70 150',
'Dave 80 180',
'Explore - Bob - 60',
'Refuel - Alice - 30',
'Breathe - Charlie - 50',
'Refuel - Dave - 40',
'Explore - Bob - 40',
'Breathe - Charlie - 30',
'Explore - Alice - 40',
'End']

)