import sys
from turtle import right

lvl = 1
def rules():
    print("You have 3 tries")

def lvl1():
    
    Levelnum = "1"
    leternum = "5"
    rightans = "kumot"
    clue1 =  " Minsan manipis minsan makapal"
    clue2 = " Malamig"

    print("Level " + Levelnum)
    print(leternum + " Letter word")
    ans = input()
    if str(ans.lower()) != rightans:
        
        print("Wrong")
        print("Clue 1: " + clue1)
        ans = input()
        if str(ans.lower()) != rightans:
            print("Wrong")
            print("Clue 2: "+clue2)
            ans = input()
            if str(ans.lower()) != rightans:
                 print("Game over")
                 sys.exit()

def lvl2():
    print("RIGHT")
    Levelnum = "2"
    leternum = "7"
    rightans = "charger"
    clue1 =  "papatayin kita pag di motot binigay sakin"
    clue2 = "thunder electric"

    print("Level " + Levelnum)
    print(leternum + " Letter word")
    ans = input()
    if str(ans.lower()) != rightans:
        
        print("Wrong")
        print("Clue 1: " + clue1)
        ans = input()
        if str(ans.lower()) != rightans:
            print("Wrong")
            print("Clue 2: "+clue2)
            ans = input()
            if str(ans.lower()) != rightans:
                 print("Game over")
                 sys.exit()

def lvl3():
    print("RIGHT")
    Levelnum = ""
    leternum = ""
    rightans = ""
    clue1 =  ""
    clue2 = ""

    print("Level " + Levelnum)
    print(leternum + " Letter word")
    ans = input()
    if str(ans.lower()) != rightans:
        
        print("Wrong")
        print("Clue 1: " + clue1)
        ans = input()
        if str(ans.lower()) != rightans:
            print("Wrong")
            print("Clue 2: "+clue2)
            ans = input()
            if str(ans.lower()) != rightans:
                 print("Game over")
                 sys.exit()   




    


rules()
lvl1()
lvl2()