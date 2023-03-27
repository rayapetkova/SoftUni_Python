stops = input()

while True:
    line = input()
    if line == "Travel":
        break
    command = line.split(":")
    if "Add Stop" in command:
        idx = int(command[1])
        new_string = command[2]
        if 0 <= idx < len(stops):
            stops = stops[:idx] + new_string + stops[idx:]
        print(stops)
    elif "Remove Stop" in command:
        start = int(command[1])
        end = int(command[2])
        if 0 <= start < len(stops) and end < len(stops):
            stops = stops[:start] + stops[end + 1:]
        print(stops)
    elif "Switch" in command:
        old_string = command[1]
        new_string = command[2]
        stops = stops.replace(old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")