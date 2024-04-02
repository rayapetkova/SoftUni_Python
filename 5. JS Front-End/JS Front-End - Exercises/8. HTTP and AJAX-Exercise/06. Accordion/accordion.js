function solution() {
    const baseURL = 'http://localhost:3030/jsonstore/advanced/articles/list'
    const detailsURL = 'http://localhost:3030/jsonstore/advanced/articles/details/'

    let mainSection = document.getElementById('main')
    mainSection.innerHTML = ''

    async function loadArticles() {
        let articlesResponse = await fetch(baseURL)
        let articles = await articlesResponse.json()

        for (let articleObj of articles) {
            let accordionElement = document.createElement('div')
            accordionElement.className = 'accordion'

            accordionElement.innerHTML = `
                <div class="head">
                    <span>${articleObj.title}</span>
                    <button class="button" id="${articleObj['_id']}">More</button>
                </div>
                <div class="extra">
                    <p>Scalable Vector Graphics .....</p>
                </div>
            `

            mainSection.appendChild(accordionElement)
            let accordionButton = accordionElement.querySelector('button')
            accordionButton.addEventListener('click', accordionButtonEvent)
            
            async function accordionButtonEvent() {
                let detailsResponse = await fetch(detailsURL + articleObj['_id'])
                let detailsArticle = await detailsResponse.json()
                
                let extraContentElement = accordionElement.querySelector('.extra p')
                extraContentElement.textContent = detailsArticle.content

                if (accordionButton.textContent === 'More') {
                    extraContentElement.parentElement.style.display = 'block'
                    accordionButton.textContent = 'Less'
                } else if (accordionButton.textContent === 'Less') {
                    extraContentElement.parentElement.style.display = 'none'
                    accordionButton.textContent = 'More'
                }
                

            }
        }
    }

    loadArticles()
}

solution()