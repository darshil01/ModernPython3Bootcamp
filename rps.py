import random 

play_dict = {
    "paper": "",
    "rock": "",
    "scissors": "",
}

print("...rock...")
print("...paper...")
print("...scissors...")

p1_input = input("Player 1 enter your choice - ")
c_list = ["rock", "paper", "scissors"]

c_pick = random.choice(c_list)
print("Computer picks {}".format(c_pick))

def choose_winner():
    if play_dict['rock'] and play_dict['paper']:
        print(play_dict['paper'] + " wins")
    if play_dict['rock'] and play_dict['scissors']:
        print(play_dict['rock'] + " wins")
    if play_dict['paper'] and play_dict['scissors']:
        print(play_dict['scissors'] + " wins")

if p1_input == c_pick:
    print("Tie")
else:
    play_dict[p1_input] = "Player 1"
    play_dict[c_pick] = "Computer"
    choose_winner()




# if p1_input == "rock" and c_pick == "paper":
#     print("Computer wins")
# elif p1_input == "rock" and c_pick == "scissors":
#     print("P1 wins")
# elif p1_input == "paper" and c_pick == "rock":
#     print("P1 wins")
# elif p1_input == "paper" and c_pick == "scissors":
#     print("Computer wins")
# elif p1_input == "scissors" and c_pick == "paper":
#     print("P1 wins")
# elif p1_input == "scissors" and c_pick == "rock":
#     print("Computer wins")
# elif p1_input == c_pick:
#     print("Tie")
# else:
#     print("someone can't type")

