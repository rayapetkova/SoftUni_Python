function numberTransform(number, ...commands) {

    commandsAction = {
        chop: (num) => num / 2,
        dice: (num) => Math.sqrt(num),
        spice: (num) => num + 1,
        bake: (num) => num * 3,
        fillet: (num) => num - 0.2*num
    }

    for (let command of commands) {
        number = commandsAction[command](number)
        console.log(number)
    }
}





// Test code
// numberTransform('32', 'chop', 'chop', 'chop', 'chop', 'chop')
// numberTransform('9', 'dice', 'spice', 'chop', 'bake', 'fillet')