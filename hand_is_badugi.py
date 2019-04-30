def hand_is_badugi(hand):
    badugi = set()
    for rank,suit in hand:
        badugi.add(rank)
        badugi.add(suit)
        if (len(badugi) == (2*len(hand))):
            return True
    return False

print(hand_is_badugi([('queen', 'hearts'), ('six', 'diamonds'), ('deuce', 'spades'), ('jack','clubs')]))
print(hand_is_badugi([('queen', 'hearts'), ('six', 'diamonds'), ('deuce', 'spades'), ('queen','clubs')]))
print(hand_is_badugi([('queen', 'hearts'), ('six', 'diamonds'), ('deuce', 'spades'), ('jack','spades')]))
