window.addEventListener("load", solve);

function solve() {
    let publishButton = document.getElementById('form-btn')
    publishButton.addEventListener('click', publishInfoEvent)

    let ulPriview = document.getElementById('preview-list')

    let firstNameElement = document.getElementById('first-name')
    let lastNameElement = document.getElementById('last-name')
    let ageElement = document.getElementById('age')
    let storyTitleElement = document.getElementById('story-title')
    let genreSelectElement = document.getElementById('genre')
    let storyElement = document.getElementById('story')

    let mainElement = document.getElementById('main')

    function publishInfoEvent(event) {

        if (firstNameElement.value !== '' && lastNameElement.value !== '' && ageElement.value !== '' && storyTitleElement.value !== '' && genreSelectElement.value !== '' && storyElement.value !== '') {
            let li = document.createElement('li')
            li.className = 'story-info'

            let article = document.createElement('article')

            let h4 = document.createElement('h4')
            let firstName = firstNameElement.value
            let lastName = lastNameElement.value
            h4.textContent = `Name: ${firstName} ${lastName}`

            let pAge = document.createElement('p')
            let age = ageElement.value
            pAge.textContent = `Age: ${age}`

            let pTitle = document.createElement('p')
            let storyTitle = storyTitleElement.value
            pTitle.textContent = `Title: ${storyTitle}`

            let pGenre = document.createElement('p')
            let genre = genreSelectElement.value
            pGenre.textContent = `Genre: ${genre}`

            let pStory = document.createElement('p')
            let story = storyElement.value
            pStory.textContent = story

            article.appendChild(h4)
            article.appendChild(pAge)
            article.appendChild(pTitle)
            article.appendChild(pGenre)
            article.appendChild(pStory)

            let saveButton = document.createElement('button')
            saveButton.className = 'save-btn'
            saveButton.textContent = 'Save Story'
            saveButton.addEventListener('click', saveInfoEvent)

            let editButton = document.createElement('button')
            editButton.className = 'edit-btn'
            editButton.textContent = 'Edit Story'
            editButton.addEventListener('click', editInfoEvent)

            let deleteButton = document.createElement('button')
            deleteButton.className = 'delete-btn'
            deleteButton.textContent = 'Delete Story'
            deleteButton.addEventListener('click', deleteStoryEvent)

            li.appendChild(article)
            li.appendChild(saveButton)
            li.appendChild(editButton)
            li.appendChild(deleteButton)

            ulPriview.appendChild(li)

            firstNameElement.value = ''
            lastNameElement.value = ''
            ageElement.value = ''
            storyTitleElement.value = ''
            genreSelectElement.value = ''
            storyElement.value = ''

            publishButton.disabled = true

            function editInfoEvent(event) {
                firstNameElement.value = firstName
                lastNameElement.value = lastName
                ageElement.value = age
                storyTitleElement.value = storyTitle
                genreSelectElement.value = genre
                storyElement.value = story

                saveButton.disabled = true
                editButton.disabled = true
                deleteButton.disabled = true

                publishButton.disabled = false
                li.remove()
            }

            function saveInfoEvent(event) {
                mainElement.innerHTML = ''
                let h1 = document.createElement('h1')
                h1.textContent = 'Your scary story is saved!'

                mainElement.appendChild(h1)
            }

            function deleteStoryEvent(event) {
                publishButton.disabled = false
                li.remove()
            }
        }
 
    }
}
