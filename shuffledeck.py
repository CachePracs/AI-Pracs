from itertools import product
from random import shuffle

deck=list(product(range(1,14),['spade','heart','diamond','club']))
shuffle(deck)
print("You got:")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
