function solve(commands) {
    let num = Number(commands.shift())
    let characters = {}

    for (let i = 0; i < num; i++) {
        let hero = commands[i].split(' ')
        let [heroName, HP, bullets] = [hero[0], Number(hero[1]), Number(hero[2])]

        characters[heroName] = [HP, bullets]
    }


    for (let command of commands) {
        if (command === 'Ride Off Into Sunset') {
            for (let [key, value] of Object.entries(characters)) {
                if (value[0] > 0) {
                    console.log(key)
                    console.log(` HP: ${value[0]}`)
                    console.log(` Bullets: ${value[1]}`)
                }
            }

            break
        }

        let commandArr = command.split(' - ')

        if (commandArr.includes('FireShot')) {
            let [charName, target] = [commandArr[1], commandArr[2]]

            if (characters[charName][1] > 0) {
                characters[charName][1] -= 1
                console.log(`${charName} has successfully hit ${target} and now has ${characters[charName][1]} bullets!`)
            } else {
                console.log(`${charName} doesn't have enough bullets to shoot at ${target}!`)
            }
        } else if (commandArr.includes('TakeHit')) {
            let [charName, damage, attacker] = [commandArr[1], Number(commandArr[2]), commandArr[3]]

            characters[charName][0] -= damage
            if (characters[charName][0] > 0)  {
                console.log(`${charName} took a hit for ${damage} HP from ${attacker} and now has ${characters[charName][0]} HP!`)
            } else {
                delete charName[charName]
                console.log(`${charName} was gunned down by ${attacker}!`)
            }
        } else if (commandArr.includes('Reload')) {
            let charName = commandArr[1]
            let currentBullets = characters[charName][1]

            if (characters[charName][1] < 6) {
                characters[charName][1] = 6
                console.log(`${charName} reloaded ${6 - currentBullets} bullets!`)
            } else {
                console.log(`${charName}'s pistol is fully loaded!`)
            }
        } else if (commandArr.includes('PatchUp')) {
            let [charName, amount] = [commandArr[1], Number(commandArr[2])]
            
            let currentHP = characters[charName][0]

            if (characters[charName][0] === 100) {
                console.log(`${charName} is in full health!`)
                continue
            }

            let recoveredBy = amount
            characters[charName][0] += amount
            if (characters[charName][0] >= 100) {
                characters[charName][0] = 100
                recoveredBy = 100 - currentHP
            }

            console.log(`${charName} patched up and recovered ${recoveredBy} HP!`)
        }
    }
}

solve(["2", 'Gus 100 0', 'Walt 100 6', 'TakeHit - Gus - 80 - Bandit', 'PatchUp - Gus - 20', 'Ride Off Into Sunset'])
