box = {"height": 120, "width": 45, "length": 30}
print(box["height"])
print(box.get("weight" , 10))

for key, value in box.items():
    print(key, value)
