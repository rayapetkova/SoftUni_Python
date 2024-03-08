function solve() {

  function createElementAndAppendToOutput() {
    p = document.createElement('p')
    p.textContent = threeSentencesArr.join('.') + '.'
    outputDiv.appendChild(p)
  }

  let text = document.getElementById('input').value
  let sentences = text.split('.').filter((el) => el.length !== 0)

  let outputDiv = document.getElementById('output')
  let threeSentencesArr = []
  for (let sentence of sentences) {
    if (threeSentencesArr.length === 3) {
      createElementAndAppendToOutput()
      threeSentencesArr = []
    }
    threeSentencesArr.push(sentence)
  }

  createElementAndAppendToOutput()
}