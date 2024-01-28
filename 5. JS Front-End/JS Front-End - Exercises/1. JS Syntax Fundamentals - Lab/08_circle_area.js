function findCircleArea (input_arg) {
    let result = 0;
    let typeInput = typeof(input_arg);

    if (typeInput === 'number') {
        result = Math.pow(input_arg, 2) * Math.PI;
        result = result.toFixed(2)
    }
    else {
        result = `We can not calculate the circle area, because we receive a ${typeof(input_arg)}.`;
    }

    console.log(result)
}





// Test code:
// findCircleArea(5)
// findCircleArea('name')
