function carWashManagement(commands) {
    let cleanPercentage = 0

    let possibleCommands = {
        soap: (value) => value + 10,
        water: (value) => value + ((20/100) * value),
        'vacuum cleaner': (value) => value + ((25/100) * value),
        mud: (value) => value - ((10/100) * value)
    }

    for (let command of commands) {
        cleanPercentage = possibleCommands[command](cleanPercentage)
    }

    console.log(`The car is ${cleanPercentage.toFixed(2)}% clean.`)
}
