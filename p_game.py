# Python 2.7.12
#
#   Author Tanvir Khonakar
#
#
#   Purpose: Practice Phyton by creating a simple python game



def start(nice=0, mean=0,name=""):
    #get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get user's name.
        if it is not a new name, thank the player for
        playing again and continue game.
    """

    if name != "": #meaning if we do not already have this user's name, they are a new player and we need to get their name
        print("\nThank you for playing again {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game you will be greeted by serveral different people. \nYou can be nice or mean.")
                    print("At the end of the game your fate will be influenced by your actions")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m:").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and abruptly storms off... ")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score 


def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, Nice) and ({}, Mean) points.".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the value stored within the 3 variables
    if nice > 3: #if condition is valid, call win function passing in the variables as it can use them
        win(nice,mean,name)
    if mean > 3: #if condition is valid, call lose function passing in the varibales as it can use them
        lose(nice,mean,name)
    else:        #eles, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice Job {}! You Win! \nEveryone loves you and you now live in a palace".format(name))
    again(nice,mean,name) #call again function and pass in our variable

def lose(nice,mean,name):
    print("\nToo bad {}! You are hated by everyone and live in a van by the river alone!".format(name))
    again(nice,mean,name) # call again function and pass in our variables

def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n:").lower()
        if choice == "y":
            stop == False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you later!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for YES or 'n' for NO...")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #I do not reset the name variable as the same user has decided to play again
    start(nice,mean,name)

if __name__ == "__main__":
    start()
    
