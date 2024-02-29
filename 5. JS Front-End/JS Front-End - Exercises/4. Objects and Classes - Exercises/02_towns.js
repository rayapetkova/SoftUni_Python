function convertToObjects(locations) {
    let allLocationsArr = []

    for (location of locations) {
        let locationArr = location.split(' | ')
        allLocationsArr.push({
            town: locationArr[0],
            latitude: Number(locationArr[1]).toFixed(2),
            longitude: Number(locationArr[2]).toFixed(2)
        })
    }

    for (let locationObj of allLocationsArr) {
        console.log(locationObj)
    }
    
}
