function checkPassword(infoArr) {
    let username = infoArr.shift()
    let reversedUsername = username.split('').reverse().join('')
    let logged = false
    
    for (let index = 0; index < infoArr.length; index++) {
        if (infoArr[index] === reversedUsername) {
            logged = true
            console.log(`User ${username} logged in.`)
        }
        
        if (index === 3 && !logged) {
            console.log(`User ${username} blocked!`)
            return
        }

        if (infoArr[index] !== reversedUsername) {
            console.log(`Incorrect password. Try again.`)
        }
    }
}