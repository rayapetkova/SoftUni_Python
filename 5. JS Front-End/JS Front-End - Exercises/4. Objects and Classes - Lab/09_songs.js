function songManagement(songsArr) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList
            this.name = name
            this.time = time
        }
    }

    let songs = []
    let numSongs = songsArr.shift()
    let typeSong = songsArr.pop()

    for (let song of songsArr) {
        let [typeListSong, nameSong, timeSong] = song.split('_')
        let newSong = new Song(typeListSong, nameSong, timeSong)
        songs.push(newSong)
    }

    if (typeSong === "all") {
        songs.forEach(
            (s) => console.log(s.name)
            )
    } else {
        let filteredSongs = songs.filter((s) => s.typeList === typeSong)
        filteredSongs.forEach(
            (s) => console.log(s.name)
            )
    }
}




songManagement([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']
    )