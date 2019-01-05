import random


def get_deck():
    card_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card_names_values = set(zip(card_names, card_values))
    suits = ['♥', '♠', '♦', '♣']
    deck = []

    for suit in suits:
        for card_name_value in card_names_values:
            card = {"name": card_name_value[0] + suit,
                    "value": card_name_value[1]}  # why is card_name_value[1] and not [0].
            deck.append(card)  # how does it know to iterate after card_name_value [0]?

    card1 = random.choice(deck)
    print(card1)

    
get_deck()

# another deck
['2♥', 2], ['2♣', 2], ['2♠', 2], ['2♦', 2],
            ['3♥', 3], ['3♣', 3], ['3♠', 3], ['3♦', 3],
            ['4♥', 4], ['4♣', 4], ['4♠', 4], ['4♦', 4],
            ['5♥', 5], ['5♣', 5], ['5♠', 5], ['5♦', 5],
            ['6♥', 6], ['6♣', 6], ['6♠', 6], ['6♦', 6],
            ['7♥', 7], ['7♣', 7], ['7♠', 7], ['7♦', 7],
            ['8♥', 8], ['8♣', 8], ['8♠', 8], ['8♦', 8],
            ['9♥', 9], ['9♣', 9], ['9♠', 9], ['9♦', 9],
            ['10♥', 10], ['10♣', 10], ['10♠', 10], ['10♦', 10],
            ['J♥', 10], ['J♣', 10], ['J♠', 10], ['J♦', 10],
            ['Q♥', 10], ['Q♣', 10], ['Q♠', 10], ['Q♦', 10],
            ['K♥', 10], ['K♣', 10], ['K♠', 10], ['K♦', 10],
            ['A♥', 11], ['A♣', 11], ['A♠', 11], ['A♦', 11]]

