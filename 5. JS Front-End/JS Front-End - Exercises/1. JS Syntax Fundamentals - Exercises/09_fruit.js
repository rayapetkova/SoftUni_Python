function calculateMoneyForFruit(typeFruit, grams, pricePerKg) {
    let quantityInKg = grams / 1000
    console.log(`I need $${(pricePerKg * quantityInKg).toFixed(2)} to buy ${quantityInKg.toFixed(2)} kilograms ${typeFruit}.`)
}






// calculateMoneyForFruit('orange', 2500, 1.80)