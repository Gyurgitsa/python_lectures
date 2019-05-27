

class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        weight=self.weight_kg* 2.20462262

        return weight_kg



class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        # child class:
        super().__init__(first_name, last_name, height_cm, weight_kg)

        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

ronaldo = FootballPlayer(first_name="Cristiano", last_name="Ronaldo", height_cm=184, weight_kg=79, goals=586, yellow_cards=95, red_cards=11)

messi = FootballPlayer(first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)


print(ronaldo.first_name)
print(ronaldo.goals)
print(messi.first_name)
print(messi.goals)

