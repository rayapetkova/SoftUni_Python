function attachGradientEvents() {
    let gradientElement = document.getElementById('gradient')
    gradientElement.addEventListener('mousemove', mouseMoveEvent)
    gradientElement.addEventListener('mouseout', mouseOutEvent)

    function mouseMoveEvent(e) {
        let power = e.offsetX / (e.target.clientWidth - 1)
        power = Math.trunc(power * 100)
        document.getElementById('result').textContent = `${power}%`
    }

    function mouseOutEvent(e) {
        document.getElementById('result') = ''
    }
}