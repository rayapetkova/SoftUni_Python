
function solve() {
    const baseURL = 'http://localhost:3030/jsonstore/games/'

    let loadGamesButton = document.getElementById('load-games')
    loadGamesButton.addEventListener('click', loadGamesEvent)

    let gamesListElement = document.getElementById('games-list')

    let addGameButton = document.getElementById('add-game')
    addGameButton.addEventListener('click', addNewGameEvent)
    let editGameButton = document.getElementById('edit-game')

    let nameInput = document.getElementById('g-name')
    let typeInput = document.getElementById('type')
    let playersInput = document.getElementById('players')

    async function loadGamesEvent(event) {
        let gamesResponse = await fetch(baseURL)
        let games = await gamesResponse.json()

        gamesListElement.innerHTML = ''

        for (let game of Object.values(games)) {
            let div = document.createElement('div')
            div.className = 'board-game'

            // First
            let div1 = document.createElement('div')
            div1.className = 'content'

            let p1 = document.createElement('p')
            let name = game.name
            p1.textContent = name

            let p2 = document.createElement('p')
            let players = game.players
            p2.textContent = players

            let p3 = document.createElement('p')
            let type = game.type
            p3.textContent = type

            div1.appendChild(p1)
            div1.appendChild(p2)
            div1.appendChild(p3)

            // Second
            let div2 = document.createElement('div')
            div2.className = 'buttons-container'
            
            let changeButton = document.createElement('button')
            changeButton.className = 'change-btn'
            changeButton.textContent = 'Change'
            changeButton.addEventListener('click', changeGameEvent)

            let deleteButton = document.createElement('button')
            deleteButton.className = 'delete-btn'
            deleteButton.textContent = 'Delete'
            deleteButton.addEventListener('click', deleteGameEvent)

            div2.appendChild(changeButton)
            div2.appendChild(deleteButton)

            // Final
            div.appendChild(div1)
            div.appendChild(div2)

            gamesListElement.appendChild(div)
            
            async function changeGameEvent(event) {
                div.remove()

                nameInput.value = name
                typeInput.value = type
                playersInput.value = players

                editGameButton.disabled = false
                editGameButton.addEventListener('click', editGameEvent)
                addGameButton.disabled = true
                
                async function editGameEvent(event) {
                    let editedGame = {
                        name: nameInput.value,
                        type: typeInput.value,
                        players: playersInput.value,
                        '_id': game._id
                    }

                    await fetch(baseURL + game._id, {
                        method: 'PUT',
                        body: JSON.stringify(editedGame)
                    })

                    editGameButton.disabled = true
                    addGameButton.disabled = false

                    loadGamesEvent()

                    nameInput.value = ''
                    typeInput.value = ''
                    playersInput.value = ''
                }
            }

            async function deleteGameEvent(event) {
                await fetch(baseURL + game._id, {
                    method: 'DELETE'
                })

                loadGamesEvent()
            }
        }
    }

    async function addNewGameEvent(event) {
        let newGame = {
            'name': nameInput.value,
            'type': typeInput.value,
            'players': playersInput.value
        }

        await fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(newGame)
        })

        loadGamesEvent()

        nameInput.value = ''
        typeInput.value = ''
        playersInput.value = ''
    }
}

solve()