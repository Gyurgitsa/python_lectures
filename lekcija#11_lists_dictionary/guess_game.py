import random
import json
import datetime

current_time=datetime.datetime.time(datetime.datetime.now())
print(current_time)

from lists import cars

secret = random.randint(1, 30)
attempts = 0
wrong_guesses= 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

name=input("What is your name?")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now().isoformat()), "name":name, "secret_number":str(secret), "wrong_guesses": str(wrong_guesses)})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list, indent=2))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
        wrong_guesses += 1
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
        wrong_guesses += 1


def sort_by_wrong_guesses(dict_keys):
    return int(dict_keys.get("wrong_guesses"))
score_list.sort(key=sort_by_wrong_guesses)

for score_dict in score_list[0:3]:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date") + " , your name is "+ str(score_dict["name"]) + ", your secret number "+ score_dict.get("secret_number") + ", wrong guesses "+ score_dict.get("wrong_guesses"))