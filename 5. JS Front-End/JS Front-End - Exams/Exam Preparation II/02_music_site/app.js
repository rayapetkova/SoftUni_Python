window.addEventListener('load', solve);

function solve() {
    let addButton = document.getElementById('add-btn')
    addButton.addEventListener('click', addNewSong)

    let allHitsContainerElement = document.querySelector('#all-hits .all-hits-container')

    let savedHitsContainerElement = document.querySelector('#saved-hits .saved-container')

    function addNewSong(event) {
        event.preventDefault()

        let genreElement = document.getElementById('genre')
        let genre = genreElement.value

        let nameSongElement = document.getElementById('name')
        let nameSong = nameSongElement.value

        let authorElement = document.getElementById('author')
        let authorStr = authorElement.value

        let dateOfCreationElement = document.getElementById('date')
        let dateOfCreation = dateOfCreationElement.value

        if (!genreElement.value || !nameSongElement.value || !authorElement.value || ! dateOfCreationElement.value) {
            return
        }

        let div = document.createElement('div')
        div.className = 'hits-info'

        let imgElement = document.createElement('img')
        imgElement.src = './static/img/img.png'

        let h2Genre = document.createElement('h2')
        h2Genre.textContent = `Genre: ${genreElement.value}`

        let h2Name = document.createElement('h2')
        h2Name.textContent = `Name: ${nameSongElement.value}`

        let h2Author = document.createElement('h2')
        h2Author.textContent = `Author: ${authorElement.value}`

        let h3Date = document.createElement('h3')
        h3Date.textContent = `Date: ${dateOfCreationElement.value}`

        let saveButton = document.createElement('button')
        saveButton.className = 'save-btn'
        saveButton.textContent = 'Save song'
        saveButton.addEventListener('click', saveSongEvent)

        let likeButton = document.createElement('button')
        likeButton.className = 'like-btn'
        likeButton.textContent = 'Like song'
        likeButton.addEventListener('click', likeSongEvent)

        let deleteButton = document.createElement('button')
        deleteButton.className = 'delete-btn'
        deleteButton.textContent = 'Delete'
        deleteButton.addEventListener('click', deleteSongEvent)

        div.appendChild(imgElement)
        div.appendChild(h2Genre)
        div.appendChild(h2Name)
        div.appendChild(h2Author)
        div.appendChild(h3Date)
        div.appendChild(saveButton)
        div.appendChild(likeButton)
        div.appendChild(deleteButton)

        allHitsContainerElement.appendChild(div)

        genreElement.value = ''
        nameSongElement.value = ''
        authorElement.value = ''
        dateOfCreationElement.value = ''

        function likeSongEvent(event) {
            let totalLikesP = document.querySelector('#total-likes p')
            let likesCount = Number(totalLikesP.textContent[totalLikesP.textContent.length - 1]) + 1
            totalLikesP.textContent = `Total Likes: ${likesCount}`

            event.currentTarget.disabled = true
        }

        function saveSongEvent(event) {
            div.remove()

            let newDiv = document.createElement('div')
            newDiv.className = 'hits-info'

            let imgElement1 = document.createElement('img')
            imgElement1.src = './static/img/img.png'

            let h2Genre1 = document.createElement('h2')
            h2Genre1.textContent = `Genre: ${genre}`

            let h2Name1 = document.createElement('h2')
            h2Name1.textContent = `Name: ${nameSong}`

            let h2Author1 = document.createElement('h2')
            h2Author1.textContent = `Author: ${authorStr}`

            let h3Date1 = document.createElement('h3')
            h3Date1.textContent = `Date: ${dateOfCreation}`

            let deleteButton1 = document.createElement('button')
            deleteButton1.className = 'delete-btn'
            deleteButton1.textContent = 'Delete'
            deleteButton1.addEventListener('click', removeSavedSongEvent)

            newDiv.appendChild(imgElement1)
            newDiv.appendChild(h2Genre1)
            newDiv.appendChild(h2Name1)
            newDiv.appendChild(h2Author1)
            newDiv.appendChild(h3Date1)
            newDiv.appendChild(deleteButton1)

            savedHitsContainerElement.appendChild(newDiv)

            function removeSavedSongEvent(event) {
                newDiv.remove()
            }
        }

        function deleteSongEvent(event) {
            div.remove()
        }
    }
}