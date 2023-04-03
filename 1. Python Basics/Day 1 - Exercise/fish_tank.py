lenght = int(input())
width = int(input())
height = int(input())
percentage = float(input())

aquarium_volume = lenght * width * height
aquarium_volume_in_L = aquarium_volume / 1000
accessories_space = (percentage / 100) * aquarium_volume_in_L
result = aquarium_volume_in_L - accessories_space

print(result)
