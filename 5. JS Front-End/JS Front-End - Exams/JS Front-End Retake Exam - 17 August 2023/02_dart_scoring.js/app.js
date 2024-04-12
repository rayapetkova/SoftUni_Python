window.addEventListener("load", solve);

function solve() {
    let addButton = document.getElementById('add-btn')
    addButton.addEventListener('click', addPlayerEvent)

    let playerInput = document.getElementById('player')
    let scoreInput = document.getElementById('score')
    let roundInput = document.getElementById('round')

    let ulSureList = document.getElementById('sure-list')
    let ulScoreboardList = document.getElementById('scoreboard-list')

    let clearButton = document.querySelector('.dart .clear')
    clearButton.addEventListener('click', clearScoreBoardEvent)

    function addPlayerEvent(event) {
        let li = document.createElement('li')
        li.className = 'dart-item'

        // First
        let article = document.createElement('article')
        
        let p1 = document.createElement('p')
        let player = playerInput.value
        p1.textContent = player

        let p2 = document.createElement('p')
        let score = scoreInput.value
        p2.textContent = `Score: ${score}`

        let p3 = document.createElement('p')
        let round = roundInput.value
        p3.textContent = `Round: ${round}`

        article.appendChild(p1)
        article.appendChild(p2)
        article.appendChild(p3)

        // Second
        let editButton = document.createElement('button')
        editButton.className = 'btn edit'
        editButton.textContent = 'edit'
        editButton.addEventListener('click', editPlayerEvent)

        let okButton = document.createElement('button')
        okButton.className = 'btn ok'
        okButton.textContent = 'ok'
        okButton.addEventListener('click', okButtonEvent)

        // Final
        li.appendChild(article)
        li.appendChild(editButton)
        li.appendChild(okButton)

        ulSureList.appendChild(li)

        addButton.disabled = true
        playerInput.value = ''
        scoreInput.value = ''
        roundInput.value = ''

        function editPlayerEvent(event) {
            li.remove()

            playerInput.value = player
            scoreInput.value = score
            roundInput.value = round

            addButton.disabled = false
        }

        function okButtonEvent(event) {
            li.remove()

            let li1 = document.createElement('li')
            li1.className = 'dart-item'

            // First
            let article = document.createElement('article')
            
            let p1 = document.createElement('p')
            p1.textContent = player

            let p2 = document.createElement('p')
            p2.textContent = `Score: ${score}`

            let p3 = document.createElement('p')
            p3.textContent = `Round: ${round}`

            article.appendChild(p1)
            article.appendChild(p2)
            article.appendChild(p3)

            // Final
            li1.appendChild(article)

            ulScoreboardList.appendChild(li1)

            addButton.disabled = false
        }
    }

    function clearScoreBoardEvent(event) {
        ulScoreboardList.innerHTML = ''
    }
}