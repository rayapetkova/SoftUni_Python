function totalPrice(product, quantity) {

    let product_prices = {
        coffee: 1.50,
        water: 1.00,
        coke: 1.40,
        snacks: 2.00
    }

    return (product_prices[product] * quantity).toFixed(2)
}







// Test code:
// console.log(totalPrice('coffee', 2))