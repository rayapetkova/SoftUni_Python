function phoneBook(people) {
    peopleInfo = {}

    for (person of people) {
        let personArr = person.split(' ')
        peopleInfo[personArr[0]] = personArr[1]
    }

    for (key of Object.keys(peopleInfo)) {
        console.log(`${key} -> ${peopleInfo[key]}`)
    }
}
