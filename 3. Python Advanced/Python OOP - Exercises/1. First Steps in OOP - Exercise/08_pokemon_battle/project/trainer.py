from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str):
        for c_pokemon in self.pokemons:
            if c_pokemon.name == pokemon_name:
                self.pokemons.remove(c_pokemon)
                return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"

    def trainer_data(self):
        final = [f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"]

        for pokemon in self.pokemons:
            final.append(f"- {pokemon.pokemon_details()}")

        return '\n'.join(final)


# Test code:

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
