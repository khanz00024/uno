# Tykhon Byshkin and Mohammad Khan
#changes = +2,skip turn, card remix, saying UNO, input not valid card protection
import random
import time

def start_game():
    colours = ("Red", "Yellow", "Green", "Blue")
    ranks = list(range(1, 11))
    actions = ["skip turn", "+2"]
    deck = [(rank, colour) for rank in ranks for colour in colours] + [(action, colour) for colour in colours for action
                                                                       in actions]+[("change colour") for _ in range(2)]
    random.shuffle(deck)
    p1 = [deck.pop(0) for _ in range(7)]
    p2 = [deck.pop(0) for _ in range(7)]
    central_deck = [deck.pop(0)]
    main_loop(p1, p2, deck, central_deck, 0)


def main_loop(p1, p2, deck, central_deck, whose_turn):
    while len(p1) > 0 and len(p2) > 0:
        print(f"Player {whose_turn + 1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_deck[0]}")
        validcards = []
        for card in p1:
            if valid_play(central_deck[0], card):
                validcards.append((card, p1.index(card) + 1))
        if validcards == []:
            print("you must draw")
            time.sleep(1)
            p1.append(deck.pop(0))
            p1, p2 = p2, p1
            whose_turn = (whose_turn + 1) % 2
            continue

        ans = int(input("You have a choice. You can (0) draw or (1)play. "))

        if ans == 1:
            print(validcards)
            player_choice = int(input("which card to play? ")) - 1
            valid = valid_play(central_deck[0], p1[player_choice])
            while not valid:
                player_choice = int(input("which card to play? ")) - 1
                valid = valid_play(central_deck[0], p1[player_choice])

            if valid:

                central_deck.insert(0, p1.pop(player_choice))

            # Check if player has only one card left
            if len(p1) == 1:
                uno_call = input("You have only one card left! Say 'UNO': ")
                if uno_call != "UNO":
  
                    print("You didn't say 'UNO'! Drawing two penalty cards...")
                    p1.append(deck.pop(0))
                    p1.append(deck.pop(0))

        if ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)
        if central_deck[0][0] == "+2":
            p2.append(deck.pop(0))
            p2.append(deck.pop(0))

        if deck == []:
            deck = central_deck
            central_deck.clear()
            random.shuffle(deck)
            central_deck = [deck.pop(0)]
        p1, p2 = p2, p1
        if central_deck[0][0] == "skip turn":
            whose_turn += 1
        whose_turn = (whose_turn + 1) % 2
    print(f"Player{whose_turn+1} won")

def valid_play(card1, card2):
    if card2=="change colour":
        return True
    return card1[0] == card2[0] or card1[1] == card2[1]


start_game()
