function typeOfPerson(age) {
    let type_person = "out of bounds"

    if (age >= 0 && age <= 2) {
        type_person = "baby"
    }
    else if (age >= 3 && age <= 13) {
        type_person = "child"
    }
    else if (age >= 14 && age <= 19) {
        type_person = "teenager"
    }
    else if (age >= 20 && age <= 65) {
        type_person = "adult"
    }
    else if (age >= 66) {
        type_person = "elder"
    }

    console.log(type_person)
}




// Test code:
// typeOfPerson(20)
// typeOfPerson(-1)