class Party:
    def __init__(self):
        self.people = []

    def going(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


party = Party()

while True:
    line = input()
    if line == "End":
        print(party.going())
        break
    party.people.append(line)
