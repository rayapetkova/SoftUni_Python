function printEmployeesWithPersonalNumbers(names) {
    let people = {}

    for (namePerson of names) {
        people[namePerson] = namePerson.length
    }

    for (person of Object.keys(people)) {
        console.log(`Name: ${person} -- Personal Number: ${people[person]}`)
    }
}
