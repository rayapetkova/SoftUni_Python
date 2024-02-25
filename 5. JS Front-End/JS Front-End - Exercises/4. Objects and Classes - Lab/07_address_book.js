function printAddressBook(peopleArr) {
    people = {}

    for (personStr of peopleArr) {
        personArr = personStr.split(':')
        people[personArr[0]] = personArr[1]
    }

    for (let [name, address] of Object.entries(people).sort()) {
        console.log(`${name} -> ${address}`)
    }
}
