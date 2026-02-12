# The objecive of this program is shuffle a deck of cards and deal 5 cards to the user.
# If the user gets a pair, triple, straight, or all of the same suit, they will get a personalised congratulatory statement.

# Author: Loic Bagnoud

import requests
import json
from collections import Counter


input("Press ENTER to shuffle the deck...")

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
requests_deck = requests.get(url)
shuffled_deck = requests_deck.json()

deck_id = shuffled_deck["deck_id"]

input("Press ENTER to deal 5 cards...")

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
requests_cards = requests.get(draw_url)
cards_drawn = requests_cards.json()

values = []
suits = []

for card in cards_drawn["cards"]:
    print(card["value"], "of", card["suit"])
    values.append(card["value"])
    suits.append(card["suit"])

value_counts = Counter(values)

def check_straight(hand):
    card_values = {
        "ACE": 1,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13
    }

    straight_values = []

    for card in hand:
        straight_values.append(card_values[card["value"]])

    straight_values.sort()

    
    for i in range(len(straight_values) - 1):
        if straight_values[i + 1] != straight_values[i] + 1:
            break
    else:
        return True

    
    if set(straight_values) == {1, 2, 3, 4, 5}:
        return True

    return False

if 3 in value_counts.values():
    print("Three of a kind! Nice draw!")
elif 2 in value_counts.values():
    print("You got a pair!")
elif len(set(suits)) == 1:
    print("A Flush! Someone's feeling lucky!")
elif check_straight(cards_drawn["cards"]):
    print("Straight! Lets go!")
else:
    print("Sorry... No luck this time...")


# https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python/
# https://docs.python.org/3/library/collections.html#collections.Counter