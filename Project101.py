import random
q1 = input("If they want to roll a dice or not?[yes-y , No-n]")

if q1=="y" :
    no = random.randint(1,6)
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[ 0 0 ]")
        print("[0 0 0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
     
    if q1 =="n" :
        print("exit")


