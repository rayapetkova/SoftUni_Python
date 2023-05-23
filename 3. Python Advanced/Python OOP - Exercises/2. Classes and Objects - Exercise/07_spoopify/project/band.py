from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for some_album in self.albums:
            if some_album.name == album_name:

                if not some_album.published:
                    self.albums.remove(some_album)
                    return f"Album {some_album.name} has been removed."

                return f"Album has been published. It cannot be removed."

        return f"Album {album_name} is not found."

    def details(self):
        final = []

        final.append(f"Band {self.name}")

        for some_album in self.albums:
            final.append(f"{some_album.details()}")

        return '\n'.join(final)


# Test code:

# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
