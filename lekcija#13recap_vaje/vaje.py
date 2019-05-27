# my_dict={"name":Gugi, "height":5, "neki":druzga}
# ,y_list={1,2}
# print(list(my_dict.__iter__()))
# for x in my dict:
#     # print(key,value)
# print("Key":, x)
# print("Value":, my_dict[x])



class Player:
    def __init__(self, name, date, score):
        self.name = name
        self.date = date
        self.score = score


name=input("Your name:")
date=datetime.datetime.now().isoformat()

score=0
player=Player(name, date, score)

player.score=4
with open("vaje#1.txt", "w") as res_file
    json.dump(results, res_file




car_dict={
    "model":"A4",
    "brand":"Audi",
    "color":"black",
    "km": 0
}


class Car:
    def __init__(self, model, band, color, km):
        self.model=model
        sel.band=band
        self.color=color
        self.km=km



 # ce zelis decode and encode web page with python:

from urllib.request import urlopen
wiki="here you have the link of the web page"
page=urlopen(wiki)
print(page.read().decode())
