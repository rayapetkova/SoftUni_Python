from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAM_NAMES = {
        'Red Bull': RedBullTeam,
        'Mercedes': MercedesTeam
    }

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in F1SeasonApp.VALID_TEAM_NAMES:
            raise ValueError(f"Invalid team name!")

        curr_team = F1SeasonApp.VALID_TEAM_NAMES[team_name](budget)

        if team_name == "Red Bull":
            self.red_bull_team = curr_team
        else:
            self.mercedes_team = curr_team

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception(f"Not all teams have registered for the season.")

        red_bull = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        better = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return f"Red Bull: {red_bull}. Mercedes: {mercedes}. {better} is ahead at the {race_name} race."


# Test case:

# f1_season = F1SeasonApp()
# print(f1_season.register_team_for_season("Red Bull", 2000000))
# print(f1_season.register_team_for_season("Mercedes", 2500000))
# print(f1_season.new_race_results("Nurburgring", 1, 7))
# print(f1_season.new_race_results("Silverstone", 10, 1))
