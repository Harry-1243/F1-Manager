import random
import time
laplength = 6
print("Please enter settings for car 1")

# user inputted car settings
print("Input level of downforce:")
print("1: High")
print("2: Medium")
print("3: Low")
DwnForce0 = int(input())

# user inputted car settings
print("Please enter settings for car 2")
print("Input level of downforce:")
print("1: High")
print("2: Medium")
print("3: Low")
DwnForce1 = int(input())

# Lap Speeds
OAPCircuit = [330, 175, 315, 110, 185, 270, 155, 275, 300, 130, 255, 310, 265, 300, 310, 150, 245, 220, 90, 190]

# Gear Changes. 0 == N
OAPCircuitG = [0, 8, 4, 8, 3, 4, 7, 4, 7, 7, 3, 6, 8, 7, 7, 8, 4, 6, 5, 2, 4]

# Determining Car speeds in race
car0lapspeed = []
car1lapspeed = []
for x in range(len(OAPCircuit)):
    Randspeed0 = int(random.randint(1, 100))
    Randposneg0 = int(random.randint(0, 100))
    if Randposneg0 % 2 == 0:
        car0lapspeed.append((OAPCircuit[x] + Randspeed0))
    else:
        car0lapspeed.append((OAPCircuit[x] - Randspeed0))
    Randspeed1 = int(random.randint(1, 100))
    Randposneg1 = int(random.randint(0, 100))
    if Randposneg1 % 2 == 0:
        car1lapspeed.append((OAPCircuit[x] + Randspeed1))
    else:
        car1lapspeed.append((OAPCircuit[x] - Randspeed1))
# increasing or decreasing speed depending on the level of aro selected (car0)
plusminushigh = [-1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1]
plusminuslow = [1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1]

if DwnForce0 == 1:
    for x in range(19):
        car0lapspeed.append(car0lapspeed[x]+(plusminushigh[x] * random.randint(0, 5)))

elif DwnForce0 == 3:
    for x in range(19):
        car0lapspeed.append(car0lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))

# increasing or decreasing speed depending on the level of aro selected by user (car1)
if DwnForce1 == 1:
    for x in range(19):
        car1lapspeed.append(car1lapspeed[x] + (plusminushigh[x] * random.randint(0, 5)))

elif DwnForce1 == 3:
    for x in range(19):
        car1lapspeed.append(car1lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))
sectorgaptime0 = []
sectorgaptime1 = []
for x in range(len(car0lapspeed)):
    sectorgaptime0.append(0.2615 / (car0lapspeed[x]/3600))
    sectorgaptime1.append(0.2615 / (car1lapspeed[x]/3600))
lapnum0 = int(0)
lapnum1 = int(0)
time0 = int(0)
time1 = int(0)
p = 0
q = 0
for x in range(1):
    for y in range(1):
        while lapnum0 <= 19:
            time0 = (time0 + sectorgaptime0[y])
            lapnum0 = (lapnum0 + 1)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Car 0")
            print("speed", car0lapspeed[p])
            print("time", time0)
            print("Sector:", p)
            p = (p + 1)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(sectorgaptime0[y])
        print("End of race car0")
    for z in range(1):
        while lapnum1 <= 19:
            time1 = (time1 + sectorgaptime1[z])
            lapnum1 = (lapnum1 + 1)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Car 1")
            print("speed", car1lapspeed[q])
            print("time", time1)
            print("Sector:", q)
            q = (q + 1)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(sectorgaptime1[z])
        print("End of race car1")

print("End of race!")
print("Car0:", time0, "Car1:", time1)
if time1 > time0:
    print("Car0 is the winner")
elif time0 > time1:
    print("Car1 is the winner")
else:
    print("It was a tie!!!!")

