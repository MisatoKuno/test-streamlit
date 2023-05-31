# #メインプログラム
# import porker_game

# def main():
#     game=poker_game.Pokergame()
#     game.main()

# if __name__=="__main__":
#     main()

import random
import itertools

cards=[{"marks":mark,"nums":num} for mark,num in itertools.product(range(1,4+1),range(1,13+1))]
random.shuffle(cards)
hand=cards[:5]
                                                                   
for i in range(4):
    for j in range(i+1,5):
        if hand[i]["nums"]>hand[j]["nums"]:
            tmp=hand[i]
            hand[i]=hand[j]
            hand[j]=tmp
            print(hand)


