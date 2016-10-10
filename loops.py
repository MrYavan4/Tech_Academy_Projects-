# Loops! * IF you ever get stuck in a loop press Ctrl - C *

# While Loop
# Start the counter at 0

counter = 0

# While counter is less than or equal to 5, run the loop

while counter < 5:
    # Show the value of the Counter
    print counter
    
    # Shortcut to increase counter by 1 (instead of typing counter = counter + 1)
    counter += 1


'''
    The problem with while loops is that you can get stuck in an infinite loop if you forget to set
    a proper counter. Using the "for" loop takes care of that as you are using a range.

'''

# For Loop
# Run loop in range  0 - 5

for counter in range(0,5):
    # Show the value of counter
    print counter
