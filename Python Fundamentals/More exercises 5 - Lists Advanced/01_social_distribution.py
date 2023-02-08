population = list(map(int, input().split(", ")))
wealth = int(input())

for i in population:
    max_number = max(population)
    idx_max_number = population.index(max_number)
    if i < wealth:
        idx_i = population.index(i)
        if max_number > wealth - i:
            population[idx_i] += wealth - i
            population[idx_max_number] -= wealth - i

if all(j >= wealth for j in population):
    print(population)
else:
    print("No equal distribution possible")
