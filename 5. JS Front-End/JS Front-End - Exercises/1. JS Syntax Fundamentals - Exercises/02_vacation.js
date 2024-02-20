function vacationPrice(people, group, day) {

    let group_types = {
        Students: {
            Friday: 8.45,
            Saturday: 9.80,
            Sunday: 10.46
        },
        Business: {
            Friday: 10.90,
            Saturday: 15.60,
            Sunday: 16
        },
        Regular: {
            Friday: 15,
            Saturday: 20,
            Sunday: 22.50
        }
    }

    let total_price_discount = 0

    if (people >= 30 && group==="Students") {
        let total_price = group_types[group][day] * people
        total_price_discount = total_price - ((15/100) * total_price)
    }
    else if (people >= 100 && group==="Business") {
        total_price_discount = group_types[group][day] * (people - 10)
    }
    else if (people >= 10 && people <= 20 && group==="Regular") {
        let total_price = group_types[group][day] * people
        total_price_discount = total_price - ((5/100) * total_price)
    }
    else {
        total_price_discount = group_types[group][day] * people
    }

    console.log(`Total price: ${total_price_discount.toFixed(2)}`)

}






// vacationPrice(40, "Regular", "Saturday")