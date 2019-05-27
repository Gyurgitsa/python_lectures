print("hello gugi") #"hello world" is a STRING

print("more string")

print(3) #you can also print a number

print("more string")
print(3)               #multiple lines


a = 1  #a=variable , 1=value meaning the variable "a" now contains the value "1"
           # you can see "a" as a name tag
print(a)  #note here that there is no quote on the variable=VARIABLES DO NOT CONTAIN QUOTES


b = 2
print(b)

print(a)
print(b)

c="hello gugi"
print(c)


#COMPLICATED EXERCIS

print(b)
b = 1       #we changed the value of "b"
print(b)


print(a)      # now "f" referes to the value that "a" has it
print(c)

f=a
print(f)

a=5       # we can change the value of "a"=5 / the value of "f" will remain "1"
print(a)
print(f)


#EXERCISE: SWAPPING TWO VARIABLES

v1="first string"
v2="second string"

v1="second string"
v2="first string"

#what seems as a resonabe solution is:

v1=v2
v2=v1

#this is not the true solution because v1 will refers to the value"second string" and v2 will also refer to the value"second string, because v2=v1

# the solution is:

temp1=v1
temp2=v2

v1=temp2
v2=temp1

#or

temp=v1  #value="first string
v1=v2    #referes to "second string
v2=temp  #will refers to fistr value

#lets test it:

v1="first string"
v2="second string"

temp=v1
v1=v2
v2=temp
print(v1)
print(v2)





x=2
print(x+3)

y=3
print(x+y)

string_a = "Hello"
string_b = "World!"

print(string_a + string_b)
print(string_a + " " + string_b)

name="youtube"
print(name + " rocks")
print(name[0])
print(name[6])
print(name[-1])
print(name[-3])
print(name[0:2])
print(name[0:5])
print(name[:3])
print(name[2:])
print("my "+name[3:])





#HOMEWORK 7.1 the mood checker

mood = input("What is your mood today? ")

if mood == "happy":
    print("It is great to see you happy!")

elif mood == "nervous":
    print("Take a deep breath 3 times")

elif mood == "sad":
    print("Cheer up, mate!")

elif mood == "excited":
    print("Excited about what?")

elif mood == "relaxed":
    print("Good way to go")

else:
    print("I don't recognize this mood.")


#HOMEWORK 7.2 guess the secret number

secret = 5

guess = int(input("Guess the number (from 1 to 10): "))

if guess == secret:
    print("Correct answer!")

else:
    print("Sorry, incorrect number")



#HOMEWORK 7.3 calculator


x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

operation = input("Choose math operation (+, -, *, /:  ")

if operation == "+":
    print(x+y)

elif operation == "-":
    print(x-y)

elif operation == "*":
    print(x*y)

elif operation == "/":
    print(x/y)

else:
    print("Incorrect answer")















