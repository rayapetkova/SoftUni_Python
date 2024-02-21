function typeOfPerson(age) {
    let typePerson = "out of bounds"

    if (age >= 0 && age <= 2) {
        typePerson = "baby"
    }
    else if (age >= 3 && age <= 13) {
        typePerson = "child"
    }
    else if (age >= 14 && age <= 19) {
        typePerson = "teenager"
    }
    else if (age >= 20 && age <= 65) {
        typePerson = "adult"
    }
    else if (age >= 66) {
        typePerson = "elder"
    }

    console.log(typePerson)
}




// Test code:
// typeOfPerson(20)
// typeOfPerson(-1)