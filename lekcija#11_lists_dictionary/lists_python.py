#
# # LISTS
#
# names=["mike", "john", "rob"]
# print(names[1])
#
# numbers=[1,2,3,4,5]
# print(numbers[4])
#
# # an empthy list
# abc=[]
# print(abc)
#
#
# # list operations in python
#
# numbers=[1,1,1,1,1,1,1]
# numbers[3]=5
# print(numbers)
#
# numbers=[1,1,1,1,1]
# newnumber=[2,2,2,2,2]
# print(numbers+newnumber)
# print(numbers*3)
#
#
# fruits=["apples", "mango", "peach"]
# print("mango" in fruits)
# print("orange" in fruits)
#
#
#
# # list functions in python
#
#
# #  append=add new item to your list
# fruits=["Apple", "Mango", "Banana", "Orange"]
# fruits.append("Peach")
# fruits.append("Tommatoe")
# print(fruits)
#
#
# len= to calculate the length of the list
fruits=["Apple", "Mango", "Banana", "Orange"]
print(len(fruits))

# # insert function =to insert item at a particular position
# fruits=["Apple", "Mango", "Banana", "Orange"]
# fruits.insert(3,"avocado")
# print(fruits)
#
#
# # index value= it returns the index value / position of particular item in the list.
# fruits=["Apple", "Mango", "Banana", "Orange"]
# print(fruits.index("Banana"))



# # EXERCISE: Coding challenge part 2
#
# # Create a list of your favorite food items, the list should have minimum 5 elements.
# # List out the 3rd element in the list.
# # Add additional item to the current list and display the list.
# # Insert an element named tacos at the 3rd index position of the list and print out the list elements.
#
# food=["Chicken", "Broccoli", "Jogurt", "Banana", "Avocado"]
#
# print(food[2])
#
# food.append("Milk")
# print(food)
#
# food.insert(3,"tacos")
# print(food)
#
#
# # EXERCISE:
# # Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.
# # Task no 2: Create a function which displays out the square values of numbers from 1 to 9.
#
# for x in range(5):
#     print("i'am a programer")
#
#
#
# def display_square():
#     for x in range(1,10):
#         print(x*x)
# display_square()
#
#
