function create(words) {
   let contendDiv = document.getElementById('content')

   for (let word of words) {
      let div = document.createElement('div')
      let p = document.createElement('p')
      p.textContent = word
      p.style.display = 'none'
      div.appendChild(p)
      div.addEventListener('click', clickedDivEvent)

      contendDiv.appendChild(div)
   }

   function clickedDivEvent(e) {
      let currentP = e.currentTarget.getElementsByTagName('p')[0]
      currentP.style.display = 'block'
   }
}