#! python3

# SD Computing Studies Assignment
#Task 1:
import random
def guesser():
    x = random.randint(1,100)
    y = 0
    z = 0
    while y != x:
        z+=1
        y = int(input("Guess a number: "))
        if y < x:
            print("The number is higher")
        elif y > x:
            print("The number is lower")
        elif y == x:
            print("That is the number")
            break
    print(f"It took {z} attempts to get {x}")
    return None

def coinflip():
    x = random.randint(0,1)
    y = ""
    while y != "heads" or y !="tails":
        y = input("Will is be heads or tails?: ")
        if y == "heads":
            if x == 0: print("The flip was heads\nYou win(:")
            elif x == 1: print("The flip was tails\nYou lose:(")
            else: print("Error")
            break
        elif y == "tails":
            if x == 0: print("The flip was heads\nYou lose:(")
            elif x == 1: print("The flip was tails\nYou win(:")
            else: print("Error")
            break
        else: print("Enter heads or tails")
    return None
def rps():
    x = random.randint(0,2)
    y = ""
    while y != "rock" or y !="paper" or  y != "scissors":
        y = input("rock, paper or scissors?: ")
        if y == "rock":
            if x == 0: print("Opponent chose rock\nYou draw")
            elif x == 1: print("Opponent chose paper\nYou lose:(")
            elif x == 2: print("Opponent chose scissors\nYou win:)")
            else: print("Error")
            break
        elif y == "paper":
            if x == 1: print("Opponent chose paper\nYou draw")
            elif x == 2: print("Opponent chose scissors\nYou lose:(")
            elif x == 0: print("Opponent chose rock\nYou win:)")
            else: print("Error")
            break
        elif y == "scissors":
            if x == 2: print("Opponent chose scissors\nYou draw")
            elif x == 0: print("Opponent chose rock\nYou lose:(")
            elif x == 1: print("Opponent chose paper\nYou win:)")
            else: print("Error")
        else: print("Enter rock, paper, or scissors")
    return None

def dnd():
    print("D&D Stat chart:")
    lis = ["strength","intelligence","wisdom","dexterity","constitution","charisma"]
    for i in lis:
        x = random.randint(1,6)
        y = random.randint(1,6)
        z = random.randint(1,6)
        print(f"{i}: {x+y+z}")
    return None

def dnd2():
    x = input("Roll 4 and discard lowest or reroll 1's(1/2): ")
    print("D&D Character stat sheet: ")
    lis = ["strength","intelligence","wisdom","dexterity","constitution","charisma"]
    if x == "1":
        for i in lis:
            a = random.randint(1,6)
            b = random.randint(1,6)
            c = random.randint(1,6)
            d = random.randint(1,6)
            print(f"{i}: {(a+b+c+d) - min(a,b,c,d)}  ")
    elif x == "2":
        for i in lis:
            a = random.randint(1,6)
            b = random.randint(1,6)
            c = random.randint(1,6)
            while a==1 or b==1 or c==1: 
                a = random.randint(1,6)
                b = random.randint(1,6)
                c = random.randint(1,6)
            print(f"{i}: {a+b+c} ")
def cards():
    ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    suits = ['C','D','H','S']
    deck = []
    for i in ranks:
        for j in suits:
            deck.append(i+j)
    random.shuffle(deck)


    p1 = []
    p2 = []
    p1.append(deck[0:5])
    p2.append(deck[5:10])
    del deck[0:10]
    print(f"player 1's deck is {p1}\nplayer 2's deck is {p2}\nfinal deck is {deck} ")
