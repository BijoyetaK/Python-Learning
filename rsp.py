import random
choice = "y"
#if they put y continue otherwise stop

while choice =="y":
    print("Lets play R, S, P Game")

    options = ["r", "s", "p"]

    computer_choice = random.choice(options)

    user_choice = input("Please enter p,s,r: ")

    #if user_choice != 'r' or user_choice != 's' or user_choice != 'p':

    if user_choice not in options:
        print("wrong entry")
    else:
        #draw
        if (user_choice == computer_choice):
            print("draw")
        #user win
        elif (user_choice =="r" and computer_choice =="s") or (user_choice=="s" and computer_choice=="p") or (user_choice=="p" and computer_choice=="r"):
            print("User wins")
        #computer wins
        elif (user_choice =="r" and computer_choice =="p") or (user_choice =="s" and computer_choice =="r") or (user_choice=="p" and computer_choice=="s"):
            print("Computer Wins")
        else:
            print("Error")            

    choice = input("Enter y to continue , anything else to stop: ")
