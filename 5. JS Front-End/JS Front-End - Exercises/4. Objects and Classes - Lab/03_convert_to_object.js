function convertToObject(jsonFormat) {
    let person = JSON.parse(jsonFormat)

    for (let key of Object.keys(person)) {
        console.log(`${key}: ${person[key]}`)
    }
}
