import random
import time

def pit0():
    pitQ = input("do you want to pit car0 next lap")
    if pitQ == yes:
        print("What would tyre would you like to change to?")
        print("1. Soft")
        print("2. Medium")
        print("3.Hard")
        tobtyre0 = input()
        if tobtyre0 == 1:
            for x in range(sectorgaptime0):
                sectorgaptime0.append(sectorgaptime0[x] - 0.6)
            tyredegrading0 = 2
            sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25))

        elif tobtyre0 == 2:
            tyredegrading0 = 3
            sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25))

        elif tobtyre0 == 1:
            for x in range(sectorgaptime0):
                sectorgaptime0.append(sectorgaptime0[x] + 0.7)
            tyredegrading0 = 4
            sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25))
    else:
        print("Ok")


def pit1():
    pitQ = input("do you want to pit car1 next lap")
    if pitQ == yes:
        print("What would tyre would you like to change to?")
        print("1. Soft")
        print("2. Medium")
        print("3.Hard")
        tobtyre1 = input()
        if tobtyre1 == 1:
            for x in range(sectorgaptime1):
                sectorgaptime1.append(sectorgaptime1[x] - 0.6)
            tyredegrading1 = 2
            sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25))

        elif tobtyre1 == 2:
            tyredegrading1 = 3
            sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25))
        elif tobtyre1 == 1:
            for x in range(sectorgaptime1):
                sectorgaptime1.append(sectorgaptime1[x] + 0.7)
            tyredegrading1 = 4
            sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25))
    else:
        print("Ok")

laplength = 6
car02bpitted = 0
car12bpitted = 0
currenttyre1 = ""
currenttyre0 = ""
tobtyre1 = ""
tobtyre0 = ""
car0crash = 0
car1crash = 0
tyredegrading1 = 6
tyredegrading0 = 6
car1lapspeed = []
car0lapspeed = []
HAMlapspeed = []
BOTlapspeed = []
VERlapspeed = []
ALBlapspeed = []
NORlapspeed = []
RIClapspeed = []
OCOlapspeed = []
STRlapspeed = []
PERlapspeed = []
GROlapspeed = []
MAGlapspeed = []
RUSlapspeed = []
KVYlapspeed = []
PIElapspeed = []
LEClapspeed = []
VETlapspeed = []
RAIlapspeed = []
GIOlapspeed = []
sectorgaptime0 = []
sectorgaptime1 = []
sectorgaptimeHAM = []
sectorgaptimeBOT = []
sectorgaptimeVER = []
sectorgaptimeALB = []
sectorgaptimeNOR = []
sectorgaptimeRIC = []
sectorgaptimeOCO = []
sectorgaptimeSTR = []
sectorgaptimePER = []
sectorgaptimeGRO = []
sectorgaptimeMAG = []
sectorgaptimeRUS = []
sectorgaptimeKVY = []
sectorgaptimePIE = []
sectorgaptimeLEC = []
sectorgaptimeVET = []
sectorgaptimeRAI = []
sectorgaptimeGIO = []

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

for x in range(len(OAPCircuit[x])):
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
# increasing or decreasing speed depending on the level of aro selected
plusminushigh = [-1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1]
plusminuslow = [1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1]

botracers = [HAMlapspeed, BOTlapspeed, VERlapspeed, ALBlapspeed, NORlapspeed, RIClapspeed, OCOlapspeed, STRlapspeed, PERlapspeed, GROlapspeed, MAGlapspeed, RUSlapspeed, KVYlapspeed, PIElapspeed, LEClapspeed, VETlapspeed, RAIlapspeed, GIOlapspeed]
botspeed = []
for x in range(len(OAPCircuit[x])):
    u = random.randint(1,100)
    if u % 2 == 0:
        botspeed.append(-1)
    else:
        botspeed.append(1)
    botracers[x].append(OAPCircuit[x] + (botspeed[x] * u))


if DwnForce0 == 1:
    for x in range(19):
        car0lapspeed.append(car0lapspeed[x] + (plusminushigh[x] * random.randint(0, 5)))

elif DwnForce0 == 3:
    for x in range(19):
        car0lapspeed.append(car0lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))

# increasing or decreasing speed depending on the level of aro selected by user
if DwnForce1 == 1:
    for x in range(19):
        car1lapspeed.append(car1lapspeed[x] + (plusminushigh[x] * random.randint(0, 5)))

elif DwnForce1 == 3:
    for x in range(19):
        car1lapspeed.append(car1lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))

for x in range(len(car1lapspeed)):
    botracers[x].append(botracers[x] + (u * random.randint(1, 5)))


racersectortime = [sectorgaptime0, sectorgaptime1, sectorgaptimeHAM, sectorgaptimeBOT, sectorgaptimeVER, sectorgaptimeALB, sectorgaptimeNOR, sectorgaptimeRIC,  sectorgaptimeOCO, sectorgaptimeSTR, sectorgaptimePER, sectorgaptimeGRO, sectorgaptimeMAG, sectorgaptimeRUS, sectorgaptimeKVY, sectorgaptimePIE, sectorgaptimeLEC, sectorgaptimeVET, sectorgaptimeRAI, sectorgaptimeGIO]
for x in range(20):
    for i in range(len(car1lapspeed)):
        racersectortime[x].append(0.2615 / (racersectortime[i]/3600))

while laplength > 0:
    for x in range(len(car1lapspeed)):
        lapnumber = (lapnumber + 1)
        totaltime0 = (totaltime0 + sectorgaptime0[x])
        totaltime1 = (totaltime1 + sectorgaptime1[x])
        totaltimeHAM = (totaltimeHAM + sectorgaptimeHAM[x])
        totaltimeBOT = (totaltimeBOT + sectorgaptimeBOT[x])
        totaltimeVER = (totaltimeVER + sectorgaptimeVER[x])
        totaltimeALB = (totaltimeALB + sectorgaptimeALB[x])
        totaltimeNOR = (totaltimeNOR + sectorgaptimeNOR[x])
        totaltimeRIC = (totaltimeRIC + sectorgaptimeRIC[x])
        totaltimeOCO = (totaltimeOCO + sectorgaptimeOCO[x])
        totaltimeSTR = (totaltimeSTR + sectorgaptimeSTR[x])
        totaltimePER = (totaltimePER + sectorgaptimePER[x])
        totaltimeGRO = (totaltimeGRO + sectorgaptimeGRO[x])
        totaltimeMAG = (totaltimeMAG + sectorgaptimeMAG[x])
        totaltimeRUS = (totaltimeRUS + sectorgaptimeRUS[x])
        totaltimeKVY = (totaltimeKVY + sectorgaptimeKVY[x])
        totaltimePIE = (totaltimePIE + sectorgaptimePIE[x])
        totaltimeLEC = (totaltimeLEC + sectorgaptimeLEC[x])
        totaltimeVET = (totaltimeVET + sectorgaptimeVET[x])
        totaltimeRAI = (totaltimeRAI + sectorgaptimeRAI[x])
        totaltimeGIO = (totaltimeGIO + sectorgaptimeGIO[x])
        pit0()
        pit1()
        tyredegrading()
        tyredegrading1 = (tyredegrading1 - 1)
        tyredegrading0 = (tyredegrading0 - 1)


def tyredegrading():
    tyre0per = ((tyredegrading0/lapnumber) * 100)
    tyre1per = ((tyredegrading1/lapnumber) * 100)
    print(tyre0per, "%")
    print(tyre1per, "%")
    if tyre0per <= 0:
        print("car0 out of race")
        car0crash = 1
    elif tyre1per <= 0:
        print("car1 out of race")
        car1crash = 1
