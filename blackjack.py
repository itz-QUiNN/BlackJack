import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

deck = []

for suit in suits:
    for rank in ranks:
        deck.append(suit + ' ' + rank)

def calc_value(card):
    rank = card.split(' ')[1]
    if rank in ('Jack', 'Queen', 'King'):
        return 10
    elif rank == 'Ace':
        return 11
    else:
        for i in range(0, 8):
            if rank == ranks[i]:
                return i + 2

user_hand = []
dealer_hand = []

for _ in range(2):
    user_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
    dealer_hand.append(deck.pop(random.randint(0, len(deck) - 1)))

print('User hand:', user_hand)
print('Dealer hand:', dealer_hand[0])

user_score = calc_value(user_hand[0]) + calc_value(user_hand[1])
dealer_score = calc_value(dealer_hand[0]) + calc_value(dealer_hand[1])

while True:
    if user_score > 21:
        print('User busted. Dealer wins.')
        break
    elif user_score == 21:
        print('User wins.')
        break
    else:
        user_choice = input('Do you want to hit or stand? (h/s): ')
        if user_choice.lower() == 'h':
            user_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
            user_score += calc_value(user_hand[-1])
            print('User hand:', user_hand)
            print('User score:', user_score)
        elif user_choice.lower() == 's':
            break

while dealer_score < 17:
    dealer_hand.append(deck.pop(random.randint(0, len(deck) - 1)))
    dealer_score += calc_value(dealer_hand[-1])
    print('Dealer hand:', dealer_hand)
    print('Dealer score:', dealer_score)

if dealer_score > 21 or dealer_score > user_score:
    print('Dealer busted. User wins.')
elif dealer_score == user_score:
    print('It\'s a tie.')
else:
    print('Dealer wins.')