function pianistSolution(wholeArr) {
    let piecesObj = {}
    let n = Number(wholeArr.shift())
    let pieces = wholeArr

    for (let i = 0; i < Number(n); i++) {
        let currentPieceArr = pieces[i].split('|')

        let piece = currentPieceArr[0]
        let composer = currentPieceArr[1]
        let key = currentPieceArr[2]
        piecesObj[piece] = [composer, key]
    }

    for (let command of pieces) {
        if (command === "Stop") {
            break
        }

        let commandArr = command.split('|')
        if (commandArr.includes('Add')) {
            commandArr.shift()
            let [piece, composer, key] = commandArr

            if (Object.keys(piecesObj).includes(piece)) {
                console.log(`${piece} is already in the collection!`)
            } else {
                piecesObj[piece] = [composer, key]
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
            }
        } else if (commandArr.includes('Remove')) {
            let piece = commandArr[1]

            if (!Object.keys(piecesObj).includes(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`)
            } else {
                delete piecesObj[piece]
                console.log(`Successfully removed ${piece}!`)
            }
        } else if (commandArr.includes('ChangeKey')) {
            commandArr.shift()
            let [piece, newKey] = commandArr

            if (!Object.keys(piecesObj).includes(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`)
            } else {
                piecesObj[piece] = [piecesObj[piece][0], newKey]
                console.log(`Changed the key of ${piece} to ${newKey}!`)
            }
        }
    }

    for (let [piece, info] of Object.entries(piecesObj)) {
        console.log(`${piece} -> Composer: ${info[0]}, Key: ${info[1]}`)
    }
    
}

pianistSolution([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',

    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'  
  ]
  )