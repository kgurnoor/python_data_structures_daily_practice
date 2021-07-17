# cook your dish here
T = int(input())
for i in range(T):
    n = input()
    if (n =="B" or n == "b"):
        print("BattleShip")
    elif (n == "C" or n == "c"):
        print("Cruiser")
    elif (n == "D" or n == "d"):
        print("Destroyer")
    else:
        print("Frigate")