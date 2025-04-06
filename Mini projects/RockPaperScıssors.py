import random 

user_wins = 0 
computers_wins = 0

options = ["rock", "scissors", "paper"]

while True:
    if user_wins == 5:
        print("YEEEEY YOU WON THE GAME!!!")
        break
    elif computers_wins == 5:
        print("Sorry dude you lost BUT I WİN PUAHAHAHA")
        break

    user_input = input("Type Rock, scissors, paper or Q to quit.").lower()
    if user_input =="q":
        break

    if user_input not in ["rock", "scissors", "paper"]:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins += 1
    elif user_input == computer_pick:
        print("you and the computer tied down")
        user_wins += 1
        computers_wins += 1
    else:
        print("you lose")
        computers_wins += 1

print("you won", user_wins, "times.")
print("the computer won", computers_wins, "times.")
print("Good bye.")