from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page " \
                       f"{r + 1} slot {len(self.photos[r])}"

        return f"No more free slots"

    def display(self):
        final = []

        for r in range(len(self.photos)):
            c_photos = [[] for i in range(len(self.photos[r]))]

            if not c_photos:
                final.append("-----------")
                final.append("")
            else:
                final.append("-----------")
                final.append(' '.join(str(l) for l in c_photos))

        final.append("-----------")
        return '\n'.join(final)


# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())
