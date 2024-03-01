function parkingLot(cars) {
    let parkingLotCars = []

    for (let i = 0; i < cars.length; i++) {
        let [command, carNumber] = cars[i].split(', ')

        if (command === 'IN' && !parkingLotCars.includes(carNumber)) {
            parkingLotCars.push(carNumber)
        } else if (command === 'OUT' && parkingLotCars.includes(carNumber)) {
            let indexCar = parkingLotCars.indexOf(carNumber)
            parkingLotCars.splice(indexCar, 1)
        }

    }

    parkingLotCars.sort()
    if (parkingLotCars.length === 0) {
        console.log('Parking Lot is Empty')
    } else {
        console.log(parkingLotCars.join('\n'))
    }
}



parkingLot(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
)