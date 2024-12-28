############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of CARDS:
# CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The CARDS in the list have equal probability of being drawn.
# CARDS are not removed from the deck as they are drawn.

import random
import os
from art import logo
import cProfile

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(CARDS)



def calculate_score(CARDS):
    """Take a list of CARDS and return the score calculated from the CARDS"""
    score = sum(CARDS)
    if score == 21 and len(CARDS) == 2:
        return 21
    
    if 11 in CARDS and score > 21:
        score -= 10
    return score


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not is_game_over:
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)  # Update score
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # TODO
    #cProfile.run('play_game()')
    os.system('cls')
    play_game()
