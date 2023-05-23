class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return f"Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        final = []

        final.append(f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}")

        for key, value in self.skills.items():
            final.append(f"==={key} - {value}\n")

        return '\n'.join(final)
