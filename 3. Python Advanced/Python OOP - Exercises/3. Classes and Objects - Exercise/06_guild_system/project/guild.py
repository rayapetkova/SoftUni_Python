from project.player import Player

class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for some_player in self.players:
            if some_player.name == player_name:
                self.players.remove(some_player)
                some_player.guild = "Unaffiliated"

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        final = []

        final.append(f"Guild: {self.name}")

        for p in self.players:
            final.append(f"{p.player_info()}")

        return "\n".join(final)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
