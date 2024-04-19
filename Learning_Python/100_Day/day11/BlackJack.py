############### Blackjack House #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

def choose_card():
    card = random.choice(cards)
    return card

user_cards_list = []
computer_cards_list = []

user_total = 0
computer_total = 0

for i in range(2):
    user_cards_list.append(choose_card())
    user_total += user_cards_list[i]
    computer_cards_list.append(choose_card())
    computer_total += computer_cards_list[i]
    
print(f"Your card are {user_cards_list}, current score: {user_total} ")
print(f"Computer first cards are [{computer_cards_list[0]}]")

get_another_card = True

while get_another_card:
    user_move = input("Are you want to get another card? yes or no? : ")
    
    if user_move == "yes":
        user_next_card = random.choice(cards)
        user_cards_list.append(user_next_card)
        user_total += user_next_card
        print(f"Your card are {user_cards_list}")
        
        if user_total > 21:
            get_another_card = False
    else:
        get_another_card = False

# append the second card of the computer cards
computer_cards_list.append(computer_first_card)
computer_total = computer_first_card + computer_second_card

print(f"Computer cards are {computer_cards_list}")

if user_total > 21:
    print("You loss you stupid bastard")
elif user_total > computer_total and user_total <= 21:
    print("You win")
elif user_total == computer_total:
    print("Draw")
else:
    print("You lose")