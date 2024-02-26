function registerHeroes(peopleArr) {
    let heroes = []

    for (let person of peopleArr) {
        let personArr = person.split(' / ')
        
        heroes.push({
            'Hero': personArr[0],
            'level': Number(personArr[1]),
            'Items': personArr[2]
        })
    }

    heroes.sort((a, b) => {
        return a.level - b.level
    })

    for (let hero of heroes) {
        console.log([`Hero: ${hero['Hero']}`, `level => ${hero['level']}`, `items => ${hero['Items']}`].join('\n'))
    }
}
