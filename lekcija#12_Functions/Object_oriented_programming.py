

class BasketballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        # model-nacin z katerin bomo opisali temi igraci
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


    def weight_to_lbs(self):
        weight_lbs = self.weight_kg * 2.20462262

        return weight_lbs

Lebron = BasketballPlayer(first_name="Lebron", last_name="James", height_cm=203, weight_kg=113, points=27.2, rebounds=7.4, assists=7.2)
Durant = BasketballPlayer (first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1, assists=4)

print(Lebron.last_name)
print(Durant.weight_kg)

players=[Lebron, Durant]

for player in players:
    print(player.last_name + ", " + player.first_name)

print(Lebron.weight_to_lbs())
print(Durant.weight_to_lbs())