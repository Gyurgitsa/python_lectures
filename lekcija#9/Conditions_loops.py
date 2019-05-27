
     #FOR  LOOP


# secret = 22
#
# for x in range(5):
#         guess = int(input("Vnesi stevilo:"))
#
#         if guess == secret:
#             print("Bravo!")
#             break
#
#         else:
#             print("UPS! Narobe.")

#zadeva pol se razvija naslednjo:

# import random
    # #
    # # secret = random. randint(1, 30)
    # # while True:
    # #     guess = int(input("Guess the secret number (between 1 and 30): "))
    # #     if guess == secret:
    # #          print("You guessed it - congratulations! It's number" + str(secret))
    # #          break
    # #     elif guess > secret:
    # #         print("Too big")
    # #     elif guess < secret:
    # #         print("Too small")



# EXERCISE 9.1: Unit converter
# Create a program that converts units. More specifically, kilometers into miles.
#Plan:
# The program greets user and describes what's the purpose of the program.
# The program asks user to enter number of kilometers.
# User enters the amount of kilometers.
# The program converts these kilometers into miles and prints them.
# The program asks user if s/he'd want to do another conversion.
# If yes, repeat the above process (except the greeting).
# If not, the program says goodbye and stops.


# print=("Here you can convert km into miles")
#
# while True:
#     print("Enter a number you want to convert form kilometers into miles")
#
# km=input("Kilometers:")
# km=float(input("Vpisi kilometri"))
#
# miles=km*0.621371
# print("miles", km *1,6)
#
# again= input("Ponovi(da/ne?)")
# if again == "no":
#     print("Buy,buy!")
#     break


# Homework 9.2: FizzBuzz:
#  User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal).
# In case the number is divisible with 3, it prints "fizz" instead of the number.
# If the number is divisible with 5, it prints "buzz".
# If it's divisible with both 3 and 5, it prints "fizzbuzz".

print("Wellcome to the fuzzbuzz game!")

end=input("Enter a number between 1 and 100")
end=input(end)

for num in range(1, end):
    # a % b	Modulo: Remainder when a is divided by b
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
