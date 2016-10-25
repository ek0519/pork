from random import shuffle, choice, sample

heart = '♥'
spade = '♠'
diamond = '♦'
club = '♣'
poker =[]
Card_suits = [heart, spade, diamond, club]

for s in Card_suits:
    for n in range(1,14):
        poker.append((s,n))
shuffle(poker)

def dealer():
    name =[]
    for i in range(5):
        card = poker.pop()
        name.append(card)
    return name
try:
    player01 = dealer()
    print(player01)
except IndexError:
    print('牌發完了')


