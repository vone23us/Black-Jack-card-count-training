# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'# HI LO COUNT STRATEGY. The purpose of this program is to teach people how to count cards in the game of Black Jack.# It will also be a training tool so that any user can become proficient at counting cards. The strategy we will use is# called Hi-Lo. We will start by getting the running count. Each card value in the deck is assigned a number.# 10 , j, q, k, a == -1 to count. 2, 3, 4, 5, 6 == count value of +1. 7 8 9 have no value.# As cards are dealt out, a card counting layer must do the math according to each card.# If a string of cards is dealt as follows: 10, J, 3,5,Q then the player determines the value as -1, -1, +1, +1, -1 for# a total value of -1. You must begin the card count after the deck is shuffled with the first card tha is dealt.# The larger the count becomes as you count cards, the more large cards remain in the deck.# If the count is far into the negatives then this means that many of the 10 value cards and aces already been dealt,# and many small cards remain in the deck.# Future development: set up a tracker that takes in a base line of player performance before the use of the program.#                       this way when we can track the users development as he/she becomes more skilled in HI-lo count.#                       set up a top score list to be shared with all users.#  Things we need:##   phase 1: basic functionality##   1: Deck of 52 cards:#       x must be able to have up to 5 decks#       x needs to handle face cards.#       x needs to have 4 suits.#       x logic for Ace = 11 0r 1#       x shuffle##   2: Game rules:#      x closest hand to or on 21 wins game or push if both player and dealer have the same number.#      x Win lose logic both for dealer and player.##   3: Dealer rules:#      x stand on 17#      x hit on anything under 17##   4: player rules:#      x hit, stand##   phase 2: Advanced strategies#       x handle situation when the deck runs out of cards#       betting#       repeat play until out of money or player quits.#       start out with set amount of money, or let the user set the starting amount.#       allow a player to double down on 9, 10, or 11 and after a split.#       split#       x then start again with the same deck (pop out cards from deck after dealt)#       x set up a function to continue playing with the same number of decks from first selection.import random# -----------------------------------------------------------------------------# DEFINE FUNCTIONS / PROGRAM RULES# -----------------------------------------------------------------------------def get_deck():    return [['2♥', 2], ['2♣', 2], ['2♠', 2], ['2♦', 2],            ['3♥', 3], ['3♣', 3], ['3♠', 3], ['3♦', 3],            ['4♥', 4], ['4♣', 4], ['4♠', 4], ['4♦', 4],            ['5♥', 5], ['5♣', 5], ['5♠', 5], ['5♦', 5],            ['6♥', 6], ['6♣', 6], ['6♠', 6], ['6♦', 6],            ['7♥', 7], ['7♣', 7], ['7♠', 7], ['7♦', 7],            ['8♥', 8], ['8♣', 8], ['8♠', 8], ['8♦', 8],            ['9♥', 9], ['9♣', 9], ['9♠', 9], ['9♦', 9],            ['10♥', 10], ['10♣', 10], ['10♠', 10], ['10♦', 10],            ['J♥', 10], ['J♣', 10], ['J♠', 10], ['J♦', 10],            ['Q♥', 10], ['Q♣', 10], ['Q♠', 10], ['Q♦', 10],            ['K♥', 10], ['K♣', 10], ['K♠', 10], ['K♦', 10],            ['A♥', 11], ['A♣', 11], ['A♠', 11], ['A♦', 11]]def get_decks(number_of_decks):    decks = []    for num in range(number_of_decks):        decks += get_deck()    random.shuffle(decks)    return decksdef get_players(player_count):    # players is a tuple of dictionaries    # players = [    #     {'name': 'Player 1', 'cards': [], 'money':50, 'total_bet':0},    #     {'name': 'Player 2', 'cards': [], 'money': 50, 'total_bet': 0},    #     {'name': 'Player 3', 'cards': [], 'money': 50, 'total_bet': 0}    # ]    players = []    for num in range(player_count):        player_name = 'Player ' + str(num + 1)        player = {'name': player_name, 'cards': [], 'money': 50, 'bet': 0, 'is_human': False}        players.append(player)    if player_count == 1:        player['is_human'] = True    return players    # todo if there is only one player ignore the position of player.def input_int(question, min_input=1, max_input=5):    # force 'response' to be less than min_input so that the while loop will run at least once to ask the question.    response = min_input - 1    while response < min_input or response > max_input:        try:            response = int(input(question + ' (' + str(min_input) + '-' + str(max_input) + ')'))        except ValueError:            print('Numbers idiot!')    return responsedef print_cards(player_name, cards):    print(player_name + ': ', end='')    for card in cards:        print(card[0] + ' ', end='')    print(' == ' + str(cards_total(cards)))def cards_total(cards):    total = 0    for card in cards:        total += card[1]    # if the total is greater than 21, then check for As    # For each A found, then deduct 10 until the total is below 21.    if total > 21:        for card in cards:            if (card[0] == 'A♥' or card[0] == 'A♣' or card[0] == 'A♠' or card[0] == 'A♦') and total > 21:                total -= 10    return totaldef check_winners(player, dealer_cards):    if cards_total(player.get('cards')) > 21:        print(player.get('name') + ': Bust... You Lose')    elif cards_total(dealer_cards) > 21:        print(player.get('name') + ': Dealer Busted, You WIN!')    elif cards_total(player.get('cards')) < cards_total(dealer_cards):        print(player.get('name') + ': Dealer Wins!')    elif cards_total(player.get('cards')) > cards_total(dealer_cards):        print(player.get('name') + ': You WIN!')    elif cards_total(player.get('cards')) == cards_total(dealer_cards):        print(player.get('name') + ': Push!')    # todo when dealer total is = to player total on the deal, and player stands.    # todo the program used the push outcome instead of the dealer wins outcome,def check_for_blackjack(cards):    return cards_total(cards) == 21def play_round(deck, players, round_count):    print('Round ', str(round_count))    # DEAL: Players    for player in players:        cards = player.get('cards')        cards.clear()        cards.append(deck.pop(0))        # todo there was a (cards) instead of (0) next to .pop. this was causing the program to crash. why?        print_cards(player.get('name'), cards)    # DEAL: Dealer (hide)    dealer_cards = []    dealer_cards.append(deck.pop(0))    # DEAL: Players    for player in players:        player.get('cards').append(deck.pop(0))        print_cards(player.get('name'), player.get('cards'))    # DEAL: Dealer (show)    dealer_cards.append(deck.pop(0))    print_cards('Dealer ', dealer_cards[1:])    print()    # DEAL: Players    for player in players:        player_cards = player.get('cards')        while cards_total(player_cards) < 22:            if check_for_blackjack(player_cards):                print(player.get('name') + ' has 21!')                break            if player.get('is_human'):                player_option = input('(H)it or (S)tand? ')                print()                if 'h' == player_option.lower():                    player_cards.append(deck.pop(0))                    print_cards(player.get('name'), player_cards)                    print()                elif 's' == player_option.lower():                    print(player.get('name') + ' Stands on ' + str(cards_total(player_cards)))                    print()                    break            else:                # todo basic logic of player sim ... do medium to advanced later                while cards_total(player_cards) <= 16:                    player_cards.append(deck.pop(0))                    print_cards(player.get('name'), player_cards)                break    #todo FUCK YEAH!!! did this shit all on my own!!!!    # DEAL: Dealer. hits on soft 17.    print_cards('Dealer  ', dealer_cards)    just_card = [item[0] for item in dealer_cards]    ace_list = ['A♥', 'A♣', 'A♠', 'A♦']    result = any(elem in just_card for elem in ace_list)    if result and (cards_total(dealer_cards) == 17):        while cards_total(dealer_cards) <= 17:            dealer_cards.append(deck.pop(0))            print_cards('Dealer  ', dealer_cards)    else:        while cards_total(dealer_cards) <= 16:            dealer_cards.append(deck.pop(0))            print_cards('Dealer  ', dealer_cards)    for player in players:        check_winners(player, dealer_cards)    print()def is_play_another_round():    player1_option = input('Play another round? (Y)es or (N)o? ')    if 'y' == player1_option.lower():        return True    return Falsedef shuffle_deck(deck, round_count, training_deck_count):    # Reshuffle logic is based on number of players and number of decks.    # RULE: Only shuffle the deck AFTER five rounds have been played if there is only one player.    # Subtracting 1 from round count will force a shuffle AFTER round 5.    if (round_count - 1) % 5 == 0:        deck = get_decks(int(training_deck_count))        print('Deck has been shuffled')    return deckdef run():    round_count = 1    # Generate the deck    training_deck_count = input_int('How many Decks will you train with?')    deck = get_decks(training_deck_count)    print()    # Number of players    player_count = input_int('How many simulated players?')    print()# todo this was really hard to code because i was having a hard time with the is_human dict.    # Human Player Position if more than one player.    if player_count != 1:        players = get_players(player_count)        player_position = input_int('What is your position?', 1, player_count)        player = players[player_position-1]        player['is_human'] = True        print()    # Kickoff the game    else:        players = get_players(player_count)    play_round(deck, players, round_count)    # Play more rounds    while is_play_another_round():        round_count += 1        deck = shuffle_deck(deck, round_count, training_deck_count)        play_round(deck, players, round_count)# -----------------------------------------------------------------------------# GAME START# -----------------------------------------------------------------------------run()