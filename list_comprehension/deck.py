def deck():
    return [
            [suit, value] for suit in ["spades", "clubs", "diamonds", "hearts"]
                          for value in range(1, 14)]

def sort_deck(deck):
    deck = sorted(deck, key=lambda card: card[1])
    return sorted(deck, key=lambda card: card[0])