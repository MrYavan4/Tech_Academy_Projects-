# Python version 2.7.12
#
#
# Author: Tanvir Khondakar
#
#
# Drill for Tech_Academy



# Question 1: Assign an interger to a variable

variable1 = 10

# Question 2: Assign a string to a variable

varibale2 = 'This is a string'

# Question 3: Assign a float to a variable

variable3 = 3.14

# Question 4: Use the print function and .format() notation to print out the variable you assigned

print ('I will print {}.').format(varibale2)

# Question 5: Use each of the operators +, -, /, +=, =, %

print(5 + 2)

print(5 - 2)

print (5/2)

y = 1
y +=1 #increment y by one using +=
print(y)

z = 5 # = assigns a value to z

print(z % y)


# Question 6: Use of logical operators and, or, not

item1 = True
item2 = False

if item1 == True and item2 == False:
    print("One is True, the other is False")

if item1 == True or item2 == True:
    print("One of these are true")

username = ""
while not username:
    username = raw_input("Username: ")
     

# Question 7 Use of conditional statements: if, elif, else

if y == 5:
    print("y is 5")
elif y == 2:
    print("y is 2")
else:
    print("The number is not known")

# Question 8: Use a while loop

v = 1
while v < 5:
    print('Hello')
    v += 1

# Question 9: Use a for loop

for v in range(0,5):
    print ('This is a for Loop')

# Question 10: Create a list and iterate through the list using a for loop to print each item out on a new line

myList = [
    "item1",
    "item2",
    "item3",
    "item4",
    "item5"
]

for item in myList:
    print("This is: %s") % item

# Question 11: Create a tuple and iterate through it using a for loop to print each item out on a new line

tup1 = (1,2,3,4)

for number in tup1:
    print("The count is %d") % number

# Question 12: Define a function that returns a string variable

def print_something(str):
    print str

# Question 13: Call the function you defined above and print the results to the shell

print_something("Hello my name is Tanvir")
