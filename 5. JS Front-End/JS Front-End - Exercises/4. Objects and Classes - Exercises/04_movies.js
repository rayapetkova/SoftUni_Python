function moviesManagement(commandsMoviesArr) {
    let movies = []

    for (let commandMovie of commandsMoviesArr) {
        let splitCommandMovie = commandMovie.split(' ')

        if (commandMovie.includes('addMovie')) {
            let movieName = splitCommandMovie.slice(1).join(' ')
            movies.push({
                'name': movieName
            })
        } else if (commandMovie.includes('directedBy')) {
            let [movieName, director] = commandMovie.split(' directedBy ')
            for (let movie of movies) {
                if (movie['name'] === movieName) {
                    movie['director'] = director
                }
            }
        } else if (commandMovie.includes('onDate')) {
            let [movieName, date] = commandMovie.split(' onDate ')
            for (let movie of movies) {
                if (movie['name'] === movieName) {
                    movie['date'] = date
                }
            }
        }
    }

    for (let movieObj of movies) {
        if (movieObj['name'] && movieObj['director'] && movieObj['date']) {
            console.log(JSON.stringify(movieObj))
        }
    }
}
