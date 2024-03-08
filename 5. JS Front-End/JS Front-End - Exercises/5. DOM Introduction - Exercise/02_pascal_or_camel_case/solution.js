function solve() {
  let text = document.getElementById('text').value
  let currentCase = document.getElementById('naming-convention').value

  let finalStr = ''
  let words = text.split(' ')

  if (!['Camel Case', 'Pascal Case'].includes(currentCase)) {
    finalStr = 'Error!'
  } else {
    for (let word of words) {
      word = word.toLowerCase()
      word = word[0].toUpperCase() + word.slice(1)
      finalStr += word
    }

    if (currentCase === 'Camel Case') {
      finalStr = finalStr[0].toLowerCase() + finalStr.slice(1)
    }
  }

  let spanResultElement = document.getElementById('result')
  spanResultElement.textContent = finalStr
}