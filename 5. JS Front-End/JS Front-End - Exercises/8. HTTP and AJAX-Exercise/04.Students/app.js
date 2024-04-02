function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/collections/students'

    let tableBodyElement = document.querySelector('tbody')
    let submitButton = document.getElementById('submit')
    submitButton.addEventListener('click', addNewStudentEvent)

    async function extractStudents() {
        tableBodyElement.innerHTML = ''

        let studentsResponse = await fetch(baseURL)
        let students = await studentsResponse.json()

        for (let key of Object.keys(students)) {
            let studentInfo = students[key]

            let tr = document.createElement('tr')

            let tdFirstName = document.createElement('td')
            tdFirstName.textContent = studentInfo.firstName

            let tdLastName = document.createElement('td')
            tdLastName.textContent = studentInfo.lastName

            let tdFacultyNumber = document.createElement('td')
            tdFacultyNumber.textContent = studentInfo.facultyNumber

            let tdGrade = document.createElement('td')
            tdGrade.textContent = studentInfo.grade

            tr.appendChild(tdFirstName)
            tr.appendChild(tdLastName)
            tr.appendChild(tdFacultyNumber)
            tr.appendChild(tdGrade)

            tableBodyElement.appendChild(tr)
        }
    }
    
    extractStudents()

    async function addNewStudentEvent() {
        let firstName = document.getElementsByName('firstName')[0]
        let lastName = document.getElementsByName('lastName')[0]
        let facultyNumber = document.getElementsByName('facultyNumber')[0]
        let grade = document.getElementsByName('grade')[0]

        let student = {
            firstName: firstName.value,
            lastName: lastName.value,
            facultyNumber: facultyNumber.value,
            grade: grade.value
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(student)
        })

        extractStudents()

        firstName.value = ''
        lastName.value = ''
        facultyNumber.value = ''
        grade.value = ''
    }
}

attachEvents();