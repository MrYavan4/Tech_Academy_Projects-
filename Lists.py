# Making Lists

'''
    Can make lists by:

    name_of_list = [list_item_1, list_item_2]

'''

# Create the list of epic programmers

epic_programmer_list = ["Tim Berners-Lee",
                        "Guido van Rossum",
                        "Linus Torvalds",
                        "Larry Page",
                        "Sergey Brin",]

#Print to console

print "An epic Programmer: " + epic_programmer_list[0]
print "An epic Programmer: " + epic_programmer_list[1]
print "An epic Programmer: " + epic_programmer_list[2]
print "An epic Programmer: " + epic_programmer_list[3]
print "An epic Programmer: " + epic_programmer_list[4]


#Changing Items on a List

'''
Type:
epic_programmer_list[4] = "Me"
'''

#Adding Items on a List

'''
Type:
epic_programmer_list.append("Me")
'''

#Using Loops with Lists: (This way you don't have to type each line over and over again)

epic_programmer_list
for programmer in epic_programmer_list:
    # Print the programmers' name to the console
    print "An epic programmer: " + programmer







#Creating list of numbers

number_list = [1,2,3,4,5]

# Loop each number in the number_list
for x in number_list:
    # Print each number to the power of 2
    print x**2

#Creating list of numbers

number_list = [1,2,3,4,5]

empty_number_list = []

# Loop each number in the number_list
for x in number_list:
    # Append each number to the power of 2 and add it to the empty list
    empty_number_list.append(x**2)

print empty_number_list





    
