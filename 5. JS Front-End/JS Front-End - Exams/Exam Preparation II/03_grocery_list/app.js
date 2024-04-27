async function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/grocery/'

    let loadProductsButton = document.getElementById('load-product')
    loadProductsButton.addEventListener('click', loadProductsEvent)

    let addProductButton = document.getElementById('add-product')
    addProductButton.addEventListener('click', addNewProductEvent)

    let tableElement = document.querySelector('table')
    let tbody = document.getElementById('tbody')

    let productNameElement = document.getElementById('product')
    let productCountElement = document.getElementById('count')
    let productPriceElement = document.getElementById('price')

    let updateProductButton = document.getElementById('update-product')

    async function loadProducts() {
        let productsResponse = await fetch(baseURL)
        let products = await productsResponse.json()

        tbody.innerHTML = ''

        for (let product of Object.values(products)) {
            let tr = document.createElement('tr')

            let firstTd = document.createElement('td')
            firstTd.className = 'name'
            firstTd.textContent = product.product

            let secondTd = document.createElement('td')
            secondTd.className = 'count-product'
            secondTd.textContent = product.count

            let thirdTd = document.createElement('td')
            thirdTd.className = 'product-price'
            thirdTd.textContent = product.price

            let tdButtons = document.createElement('td')
            tdButtons.className = 'btn'

            let updateBtn = document.createElement('button')
            updateBtn.className = 'update'
            updateBtn.textContent = 'Update'

            let deleteBtn = document.createElement('button')
            deleteBtn.className = 'delete'
            deleteBtn.textContent = 'Delete'

            tdButtons.appendChild(updateBtn)
            tdButtons.appendChild(deleteBtn)

            tr.appendChild(firstTd)
            tr.appendChild(secondTd)
            tr.appendChild(thirdTd)
            tr.appendChild(tdButtons)

            tbody.appendChild(tr)

            let updateButton = tr.querySelector('.btn .update')
            updateButton.addEventListener('click', updateProductEvent)

            let deleteButton = tr.querySelector('.btn .delete')
            deleteButton.addEventListener('click', deleteProductEvent)

            async function deleteProductEvent(event) {
                await fetch(baseURL + product['_id'], {
                    method: "DELETE"
                })
                loadProducts()
            }

            async function updateProductEvent(event) {
                productNameElement.value = product.product
                productCountElement.value = product.count
                productPriceElement.value = product.price

                updateProductButton.disabled = false
                updateProductButton.addEventListener('click', updateProduct)

                async function updateProduct(event) {
                    event.preventDefault()
                    
                    let currProductObj = {
                        'product': productNameElement.value,
                        'count': productCountElement.value,
                        'price': productPriceElement.value
                    }

                    await fetch(baseURL + product['_id'], {
                        method: 'PATCH',
                        body: JSON.stringify(currProductObj)
                    })

                    loadProducts()
                }
            }
        }

        tableElement.appendChild(tbody)
    }

    function loadProductsEvent(event) {
        event.preventDefault()

        loadProducts()
    }

    function addNewProductEvent(event) {
        event.preventDefault()
        
        let product = productNameElement.value
        let count = productCountElement.value
        let price = productPriceElement.value

        let productObj = {
            product, 
            count,
            price
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(productObj)
        })

        loadProducts()

        productNameElement.value = ''
        productCountElement.value = ''
        productPriceElement.value = ''
    }
}

attachEvents()
