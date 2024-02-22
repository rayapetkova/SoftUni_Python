function checkPasswordValidation(password) {
    errors = []
    digitsCount = 0

    if (!(password.length >= 6 && password.length <= 10)) {
        errors.push('Password must be between 6 and 10 characters')
    }

    if (!(/^[a-zA-z0-9]+$/.test(password))) {
        errors.push('Password must consist only of letters and digits')
    }

    for (let symbol of password) {
        if (!isNaN(symbol)) {
            digitsCount += 1
        }
    }

    if (digitsCount < 2) {
        errors.push('Password must have at least 2 digits')
    }

    if (errors.length) {
        return errors.join('\n')
    } else {
        return 'Password is valid'
    }
    
}







// Test code
// console.log(checkPasswordValidation('MyPass123'))