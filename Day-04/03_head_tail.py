import random

print('''Flip a coin, 
      1 side for Head and another side for Tail. 
      Let "0 for Head" and "1 for Tail''')
coin_side = random.randint(0,1)
print(coin_side)
if coin_side == 1:
    print("Head")
else:
    print("Tail")


