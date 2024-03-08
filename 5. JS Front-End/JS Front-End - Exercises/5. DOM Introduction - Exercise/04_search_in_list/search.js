function search() {
   let searchBoxValue = document.getElementById('searchText').value
   let listElements = Array.from(document.querySelectorAll('#towns li'))

   let allMatches = 0
   for (let liElement of listElements) {
      if (liElement.textContent.includes(searchBoxValue)) {
         allMatches += 1
         liElement.style.fontWeight = 'bold'
         liElement.style.textDecoration = 'underline'
      }
   }

   let resultDiv = document.getElementById('result')
   resultDiv.textContent = `${allMatches} matches found`
}
