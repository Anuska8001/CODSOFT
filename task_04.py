import random

user_win = 0
comp_win = 0

options = ["rock", "paper", "scissor"]
# list


while True:
    user_input = input("CHOOSE : Rock/Paper/Scissor or Q for quit... ").lower()
    
    if user_input == "q":
        break

    if user_input not in options:     
        continue

    random_number = random.randint(0,2)
    # rock : 0, paper : 1, scissor : 2

    comp_pick = options[random_number]
    print("Computer picked", comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissor":
        print("You Won...!")
        user_win += 1
        continue

    elif user_input == "scissor" and comp_pick == "paper":
        print("You Won...!")
        user_win += 1
        continue

    elif user_input == "paper" and comp_pick == "rock":
        print("You Won...!")
        user_win += 1
        continue

    else:
        print("You Lost...!")
        comp_win += 1

print("You won", user_win, "times.")
print("The computer won", comp_win, "times.")

print("Goodbye!")
