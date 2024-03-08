function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchValue = document.getElementById('searchField')
      let allElements = Array.from(document.querySelectorAll('td'))
      let allRows = Array.from(document.querySelectorAll('tr'))

      for (let row of allRows) {
         row.classList.remove('select')
      }

      for (let element of allElements) {
         if (element.textContent.includes(searchValue.value)) {
            element.parentElement.className = 'select'
         }
      }

      searchValue.value = ''
   }
}