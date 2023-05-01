def add_songs(*args):
    dictionary, final = {}, []
    for song_name, lyrics in args:
        dictionary[song_name] = dictionary.get(song_name, []) + lyrics
    for key, value in dictionary.items():
        final.append(f"- {key}")
        if value:
            for some in value:
                final.append(some)
    return '\n'.join(final)


# Test input:

# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))
