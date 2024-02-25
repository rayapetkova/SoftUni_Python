function storeStocking(currentStock, orderedStock) {
    let products = {}

    for (let i = 0; i < currentStock.length; i++) {
        if (i % 2 !== 0) {
            products[currentStock[i - 1]] = Number(currentStock[i])
        }
    }

    for (let j = 0; j < orderedStock.length; j++) {
        if (j % 2 !== 0) {
            if (Object.keys(products).includes(orderedStock[j - 1])) {
                products[orderedStock[j - 1]] += Number(orderedStock[j])
            } else {
                products[orderedStock[j - 1]] = Number(orderedStock[j])
            }
        }
    }

    for (let key of Object.keys(products)) {
        console.log(`${key} -> ${products[key]}`)
    }
}




storeStocking([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
    )