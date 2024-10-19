import random
#Tykhon Byshkin and Mohammad Khan 
def start_game():

    colours = ("Red","Yellow", "Green", "Blue")
    ranks = list(range(1,11))
    deck = [(rank, colour) for rank in ranks for colour in colours]
    random.shuffle(deck)
    p1 = [deck.pop(0) for _ in range (7)]
    p2 = [deck.pop(0) for _ in range (7)]
    central_card = deck.pop(0)
    main_loop(p1, p2, deck, central_card, 0)

def main_loop(p1, p2, deck, central_card, whose_turn):
    while len(p1)>0 and len(p2)>0:
        print(f"Player {whose_turn + 1}'s turn, here is your hand {p1}")
        print(f"Central card is: {central_card}")
        ans= int(input("You have a choice. You can (0) draw or (1) play"))
        if ans == 1:
            player_choice = int(input("which card to play?"))-1
            valid = valid_play(central_card, p1[player_choice])
            if valid :
                central_card = p1.pop(player_choice)
        if ans == 0:
            draw_card = deck.pop(0)
            p1.append(draw_card)
        p1,p2 = p2,p1
        whose_turn = (whose_turn + 1) % 2

def valid_play(card1, card2):
    return card1[0] == card2[0] or card[1] == card[1]
start_game()

