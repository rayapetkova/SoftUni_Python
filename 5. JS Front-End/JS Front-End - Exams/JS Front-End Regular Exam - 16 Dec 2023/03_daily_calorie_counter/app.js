
function solve() {
    const baseURL = 'http://localhost:3030/jsonstore/tasks/'

    let loadMealsButton = document.getElementById('load-meals')
    loadMealsButton.addEventListener('click', loadMealsEvent)

    let mealsElement = document.getElementById('list')

    let editMealButton = document.getElementById('edit-meal')

    let addMealButton = document.getElementById('add-meal')
    addMealButton.addEventListener('click', addNewMealEvent)

    let foodInput = document.getElementById('food')
    let timeInput = document.getElementById('time')
    let caloriesInput = document.getElementById('calories')

    async function loadMealsEvent(event) {
        let mealsResponse = await fetch(baseURL)
        let meals = await mealsResponse.json()

        mealsElement.innerHTML = ''

        for (let meal of Object.values(meals)) {
            let div = document.createElement('div')
            div.className = 'meal'

            let h2 = document.createElement('h2')
            h2.textContent = meal.food

            let h3First = document.createElement('h3')
            h3First.textContent = meal.time

            let h3Second = document.createElement('h3')
            h3Second.textContent = meal.calories

            // Second
            let divButtons = document.createElement('div')
            divButtons.id = 'meal-buttons'

            let changeButton = document.createElement('change')
            changeButton.className = 'change-meal'
            changeButton.textContent = 'Change'
            changeButton.addEventListener('click', editMealEvent)
            
            let deleteButton = document.createElement('button')
            deleteButton.className = 'delete-meal'
            deleteButton.textContent = 'Delete'
            deleteButton.addEventListener('click', deleteMealEvent)

            divButtons.appendChild(changeButton)
            divButtons.appendChild(deleteButton)

            div.appendChild(h2)
            div.appendChild(h3First)
            div.appendChild(h3Second)
            div.appendChild(divButtons)

            mealsElement.appendChild(div)
            editMealButton.disabled = true

            async function editMealEvent(event) {
                div.remove()

                foodInput.value = meal.food
                timeInput.value = meal.time
                calories.value = meal.calories

                editMealButton.disabled = false
                addMealButton.disabled = true

                editMealButton.addEventListener('click', editMealButtonEvent)

                async function editMealButtonEvent(event) {
                    let editedMeal = {
                        food: foodInput.value,
                        time: timeInput.value,
                        calories: caloriesInput.value,
                        '_id': meal._id
                    }

                    await fetch(baseURL + meal._id, {
                        method: 'PUT',
                        body: JSON.stringify(editedMeal)
                    })

                    loadMealsEvent()
                    editMealButton.disabled = true
                    addMealButton.disabled = false
                }
            }

            async function deleteMealEvent(event) {
                await fetch(baseURL + meal._id, {
                    method: 'DELETE'
                })

                loadMealsEvent()
            }
        }
    }

    async function addNewMealEvent(event) {
        let [food, time, calories] = [foodInput.value, timeInput.value, caloriesInput.value]

        let newMealObj = {
            food,
            time,
            calories
        }

        await fetch(baseURL, {
            method: 'POST', 
            body: JSON.stringify(newMealObj)
        })

        foodInput.value = ''
        timeInput.value = ''
        caloriesInput.value = ''
        loadMealsEvent()
    }
}

solve()