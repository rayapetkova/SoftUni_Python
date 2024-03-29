function attachEvents() {
    let baseURL = 'http://localhost:3030/jsonstore/forecaster/'
    let wantedLocation = document.getElementById('location')
    let submitButton = document.getElementById('submit')
    submitButton.addEventListener('click', getWeatherEvent)

    let forecastDiv = document.getElementById('forecast')
    let currentWeatherConditions = document.getElementById('current')
    let upcomingWeatherConditions = document.getElementById('upcoming')

    let weatherSymbols = {
        'Sunny': '&#x2600',
        'Partly sunny': '&#x26C5',
        'Overcast': '&#x2601',
        'Rain': '&#x2614',
        'Degrees': '&#176'
    }

    function getWeatherEvent() {
        forecastDiv.style.display = 'block'

        fetch(baseURL + 'locations')
        .then(response => response.json())
        .then(data => {

            for (let location of data) {
                if (location.name === wantedLocation.value) {
                    let currentLocationCode = location.code

                    fetch(baseURL + 'today/' + currentLocationCode)
                        .then(response => response.json())
                        .then(data => {
                            let divElement = document.createElement('div')
                            divElement.className = 'forecasts'
                            divElement.innerHTML = `
                            <span class="condition symbol">${weatherSymbols[data.forecast.condition]}</span>
                            <span class="condition">
                                <span class="forecast-data">${data.name}</span>
                                <span class="forecast-data">${data.forecast.low}${weatherSymbols['Degrees']}/${data.forecast.high}${weatherSymbols['Degrees']}</span>
                                <span class="forecast-data">${data.forecast.condition}</span>
                            </span>
                            `

                            currentWeatherConditions.appendChild(divElement)
                        })
                    
                    fetch(baseURL + 'upcoming/' + currentLocationCode)
                        .then(response => response.json())
                        .then(data => {
                            let divElement = document.createElement('div')
                            divElement.className = 'forecast-info'
                            for (let dayForecast of data.forecast) {
                                let newSpan = document.createElement('span')
                                newSpan.className = 'upcoming'
                                newSpan.innerHTML = `
                                <span class="symbol">${weatherSymbols[dayForecast.condition]}</span>
                                <span class="forecast-data">${dayForecast.low}${weatherSymbols['Degrees']}/${dayForecast.high}${weatherSymbols['Degrees']}</span>
                                <span class="forecast-data">${dayForecast.condition}</span>
                                `
                                divElement.appendChild(newSpan)
                            }

                            upcomingWeatherConditions.appendChild(divElement)
                        })
                }
            }
        })

        
    }

    
}

attachEvents();