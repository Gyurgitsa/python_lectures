# my_list = [1, 34, 12, 17, 87]
# my_list.sort()
# print(my_list)
#
# my_str_list=["1", "01", "2", "10", "11", "20"]
# my_str_list.sort()
# print(my_str_list)
#
# cars=["toyota", "bmw", "nissan"]
# models=["prius", "juke", "m3"]
#
# for car in cars:
#     print(car)
# print(cars[1])
#
# # len function
# for i in range(len(cars)):
#     print(cars[1])
# i=0
# print("####")
# while i < len(cars):
#     print(cars[i])
#     i += 1



# EXAMPLE 2:

courses=["History", "Math", "Physics", "Computers"]

print(len(courses))
print(courses[-1])
print(courses[0:2])
      #or
print(courses[:2])
print(courses[2:])


# courses.append("Art")
# print(courses)


courses.insert(0,"Art")
print(courses)


courses2=["Education", "Science"]
courses.extend(courses2)
print(courses)


courses.remove("Math")
print(courses)


courses.sort()
print(courses)

nums=[1,5,3,7,9,2]
nums.sort()
print(nums)



# Python program to sum all the items in a list


sum = 0
list = [22, 33, 44, 55]

for x in list:
    sum = sum + x

print("sumata ke e: ", sum)


# Python program to multiplies all the items in a list

beseda = 1
lista = [11, 34, 53, 2, 1]

for y in lista:
    beseda = beseda * y
print("the sum is: ", beseda)




