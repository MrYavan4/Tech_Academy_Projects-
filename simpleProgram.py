print('Let\'s see how long you have lived in days, minutes and seconds')
name = raw_input("name: ")
print("Now enter your age")
age = int(raw_input("age: "))

#define days, minutes and seconds

days = age * 365
minutes = age * 523948
seconds = age * 31556926

#Print the final result
print("{} has been alive for {} days, {} minutes and {} seconds! Wow!").format(name,days,minutes,seconds)


