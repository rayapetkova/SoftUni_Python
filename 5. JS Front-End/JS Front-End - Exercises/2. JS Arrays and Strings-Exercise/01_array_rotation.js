function rotateArray(currArray, num_rotations) {
    
    for (let i = 0; i < num_rotations; i++) {
        currArray.push(currArray.shift())
    }

    console.log(currArray.join(' '))
}






// Test code
// rotateArray([51, 47, 32, 61, 21], 2)
