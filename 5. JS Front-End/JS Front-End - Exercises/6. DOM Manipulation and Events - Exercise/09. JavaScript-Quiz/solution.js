function solve() {
    let allSectionsElements = Array.from(document.querySelectorAll('section'))
    let allCorrectAnswers = ['onclick', 'JSON.stringify()', 'A programming API for HTML and XML documents']
    let currentQuestion = 0
    let guessedQuestions = 0

    for (let section of allSectionsElements) {
        let twoAnswers = Array.from(section.querySelectorAll('p'))
        let firstP = twoAnswers[0]
        let secondP = twoAnswers[1]
        firstP.addEventListener('click', checkForCorrectAnswer)
        secondP.addEventListener('click', checkForCorrectAnswer)
    }

    function checkForCorrectAnswer(event) {
        allSectionsElements[currentQuestion].style.display = 'none'

        if (currentQuestion < 2) {
            allSectionsElements[currentQuestion + 1].style.display = 'block'
        }

        if (allCorrectAnswers.includes(event.currentTarget.textContent)) {
            currentQuestion += 1
            guessedQuestions += 1
        } else {
            currentQuestion += 1
        }

        if (currentQuestion === 3) {
            showResults()
        }
    }

    function showResults() {
        let ulResults = document.getElementById('results')
        let h1Result = ulResults.querySelector('h1')

        if (guessedQuestions === 3) {
            h1Result.textContent = 'You are recognized as top JavaScript fan!'
        } else {
            h1Result.textContent = `You have ${guessedQuestions} right answers`
        }
        ulResults.style.display = 'block'
    }
    
}