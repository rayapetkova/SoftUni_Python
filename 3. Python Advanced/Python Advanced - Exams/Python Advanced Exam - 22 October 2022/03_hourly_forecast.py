def forecast(*args):
    dictionary, final, end_weather = {}, [], []
    for location, weather in args:
        dictionary[weather] = dictionary.get(weather, []) + [location]
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0], reverse=True)
    for key, value in sorted_dictionary:
        sorted_locations = sorted(value)
        if key == "Rainy":
            for c_location in sorted_locations:
                end_weather.append(f"{c_location} - {key}")
            continue
        for c_location in sorted_locations:
            final.append(f"{c_location} - {key}")
    final.extend(end_weather)
    return '\n'.join(final)


# Test inputs:

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))


# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))


# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
