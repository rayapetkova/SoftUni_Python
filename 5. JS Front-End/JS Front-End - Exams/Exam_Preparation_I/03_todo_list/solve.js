// TODO
function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/tasks/'

    let loadTasksButton = document.getElementById('load-button')
    loadTasksButton.addEventListener('click', loadAllTasksEvent)

    let addButton = document.getElementById('add-button')
    addButton.addEventListener('click', addNewTaskEvent)

    let ulTodoList = document.getElementById('todo-list')

    async function loadTasks() {
        ulTodoList.innerHTML = ''

        let tasksResponse = await fetch(baseURL)
        let tasks = await tasksResponse.json()

        for (let task of Object.values(tasks)) {
            let li = document.createElement('li')
            
            let span = document.createElement('span')
            span.textContent = task.name

            let removeButton = document.createElement('button')
            removeButton.textContent = 'Remove'
            removeButton.addEventListener('click', removeTaskEvent)

            let editButton = document.createElement('button')
            editButton.textContent = 'Edit'
            editButton.addEventListener('click', editTaskEvent)

            li.appendChild(span)
            li.appendChild(removeButton)
            li.appendChild(editButton)

            ulTodoList.appendChild(li)

            function removeTaskEvent(event) {
                event.preventDefault()

                fetch(baseURL + task['_id'], {
                    method: 'DELETE'
                })

                loadTasks()
            }

            function editTaskEvent(event) {
                event.preventDefault()

                span.remove()
                let inputField = document.createElement('input')
                inputField.value = task.name
                li.insertBefore(inputField, removeButton)

                editButton.remove()
                let submitButton = document.createElement('button')
                submitButton.textContent = 'Submit'
                li.appendChild(submitButton)
                submitButton.addEventListener('click', submitEdittedTask)

                function submitEdittedTask(event) {
                    event.preventDefault()

                    let changedTask = {
                        'name': inputField.value
                    }

                    fetch(baseURL + task['_id'], {
                        method: 'PATCH',
                        body: JSON.stringify(changedTask)
                    })

                    loadTasks()
                }
            }
        }
    }

    async function loadAllTasksEvent(event) {
        event.preventDefault()

        loadTasks()
    }

    async function addNewTaskEvent(event) {
        event.preventDefault()
        let itemTitle = document.getElementById('title')

        let itemObj = {
            'name': itemTitle.value
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(itemObj)
        })
        
        itemTitle.value = ''
        loadTasks()
    }
}

attachEvents();
