population = list(map(int, input().split(", ")))
wealth = int(input())

for i in range(len(population)):
    max_number = max(population)
    idx_max_number = population.index(max_number)

    if population[i] < wealth:
        needed = wealth - population[i]

        if max_number > needed:
            population[i] += needed
            population[idx_max_number] -= needed

if all(j >= wealth for j in population):
    print(population)

else:
    print("No equal distribution possible")
