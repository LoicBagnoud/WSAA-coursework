# The objecive of this program is to shuffle a deck of cards and deal 5 cards to the user.
# If the user gets a pair, triple, straight, or all of the same suit, they will get a personalised congratulatory statement.

# Author: Loic Bagnoud

# We import our packages
import requests
import json
from collections import Counter

# I decided to add prompts to make it more interactive
input("Press ENTER to shuffle the deck...")

# This first part gets our deck and shuffles it. After getting back in Json, we get the Deck ID
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
requests_deck = requests.get(url)
shuffled_deck = requests_deck.json()

deck_id = shuffled_deck["deck_id"]

# Repeat the same as above but now we're gonna get 5 cards from the Deck ID we got from before.
input("Press ENTER to deal 5 cards...")

draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
requests_cards = requests.get(draw_url)
cards_drawn = requests_cards.json()

# We're gonna create two lists. One for values of cards and one for suits. 
values = []
suits = []

# Inside those 5 cards, print each one and store the values and suits in their appropriate lists.
for card in cards_drawn["cards"]:
    print(card["value"], "of", card["suit"])
    values.append(card["value"])
    suits.append(card["suit"])

# Thanks to the Counter module, we can count how many times each value appears in the values list.
value_counts = Counter(values)

# This function is necessary to see if the hand is a straight because it involves a sequence.
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

# We store the values here 
    straight_values = []

# This was adapted from a code I saw online for poker hands. Reference below.
# 
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

# Then we check if specific values are inside our values.
# If a value appears 3 times, we get a three of a kind.
if 3 in value_counts.values():
    print("Three of a kind! Nice draw!")

# If two times, we get a pair    
elif 2 in value_counts.values():
    print("You got a pair!")

# Since we appended the suits into their specific list, this checks if there is only one unique set. If so, we get a flush
elif len(set(suits)) == 1:
    print("A Flush! Someone's feeling lucky!")

# This one tests for the function above.
elif check_straight(cards_drawn["cards"]):
    print("Straight! Lets go!")

# If all fails, we display a sad message.
else:
    print("Sorry... No luck this time...")

# References:
# https://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python/
# https://docs.python.org/3/library/collections.html#collections.Counter