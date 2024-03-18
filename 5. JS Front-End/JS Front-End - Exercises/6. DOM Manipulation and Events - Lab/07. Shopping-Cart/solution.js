function solve() {
   let allProductsButtons = Array.from(document.querySelectorAll('.product .product-add .add-product'))
   let cartProducts = new Set()
   let totalMoney = 0
   let textareaResult = document.querySelector('textarea')

   let checkoutButton = document.querySelector('.checkout')
   checkoutButton.addEventListener('click', checkoutButtonClicked)

   for (let productButton of allProductsButtons) {
      productButton.addEventListener('click', clickButtonEvent)
   }

   function clickButtonEvent(e) {
      let elementWithClassProduct = e.currentTarget.parentNode.parentNode
      let productName = elementWithClassProduct.querySelector('.product-title').textContent
      let productPrice = elementWithClassProduct.querySelector('.product-line-price').textContent

      cartProducts.add(productName)
      totalMoney += Number(productPrice)

      let productDesc = `Added ${productName} for ${productPrice} to the cart.\n`
      textareaResult.textContent += productDesc
   }

   function checkoutButtonClicked() {
      textareaResult.textContent += `You bought ${Array.from(cartProducts).join(', ')} for ${totalMoney.toFixed(2)}.`
      
      let allButtons = Array.from(document.querySelectorAll('button'))
      for (let button of allButtons) {
         button.disabled = true
      }
   }
   
}