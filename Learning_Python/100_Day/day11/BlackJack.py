############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

user_first_card = random.choice(cards)
user_second_card = random.choice(cards)
computer_first_card = random.choice(cards)
computer_second_card = random.choice(cards)

user_cards_list = []
user_cards_list.append(user_first_card)
user_cards_list.append(user_second_card)
user_total = user_first_card + user_second_card

computer_cards_list = []
computer_cards_list.append(computer_first_card)

print(f"Your card are {user_cards_list} ")
print(f"Computer cards are {computer_cards_list}")

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