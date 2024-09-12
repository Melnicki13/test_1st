
# Task 1
# Write a Python program to create a list containing the following
# numbers: 10, 20, 30, 40, 50.
#  Sub-task1: Print the list.


#sub-task1:

def task1():
    pass
numbers = [10, 20, 30, 40, 50]
print(numbers)



# Task 2.
# Given the list
#       numbers = [10, 20, 30, 40, 50],
#
#       write a Python program to:
#       sub-task2: Print the first element of the list.
#       Sub-task 3: faceti o functie empty, care sa nu provoace erori la rulare :)
#       sub-task4: Print the third element of the list.
#       sub-task5: Change the second element of the list to 25 and print the updated list.
#       sub-task6: Insert the number 15 at the second position in the list

def task2():
    pass
numbers = [10, 20, 30, 40, 50]

# sub-task2
print(numbers[0])

#Sub-task 3
#faceti o functie empty, care sa nu provoace erori la rulare :)

def how_to_pass():
    pass

# sub-task4
print(numbers[2])

# sub-task5
numbers[1] = 25
print(numbers)

# sub-task6
numbers.insert(1, 15)
print(numbers)

#Task 3.
# Given the list
# matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
#
# write a Python program to:
# sub-task7: Print the second element of the second list.
# sub-task8: Print all the elements from the first, third and last list.




def task3():
    pass

#Sub Task 7

matrix = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]


print(matrix[1][1])

# sub-task8

print(matrix[0])
print(matrix[2])
print(matrix[-1])

#Task 4

# Task 4.
# Write a Python program to create a dictionary with the following key-value pairs
#       sub-task9: Print the dictionary
# Given the following dictionary
#       person = {"name": "Alice", "age": 25, "city": "New York"},
#
#       write a Python program to:
#       sub-task9: Print the value associated with the key "name".
#       sub-task10: Print the value associated with the key "age".
#       sub-task11: Print the value of the "city" key using the get() method.

def task4():
    pass

person = {"name": "Alice", "age": 25, "city": "New York"}


print(person)

# sub-task9
print(person["name"])

# sub-task10
print(person["age"])

# sub-task11
print(person.get("city"))


# Task 5.
# Write a Python program that takes a list of fruits:
#       fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]

#       sub-task12: Create a dictionary that counts the number of occurrences of each fruit, resulting in:
#           {"apple": 3, "banana": 2, "cherry": 1}

def task5():
    pass

fruits = ["apple", "banana", "cherry", "apple", "banana", "apple"]
fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

print(fruit_count)

if __name__ == "__main__":
    print("You scared me i thought it would be harder ! ")

