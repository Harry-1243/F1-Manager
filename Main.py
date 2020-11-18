import random
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

#Lap Speeds
OAPCircuit = [330, 175, 315, 110, 185, 270, 155, 275, 300, 130, 255, 310, 265, 300, 310, 150, 245, 220, 90, 190]

# Gear Changes. 0 == N
OAPCircuitG = [0, 8, 4, 8, 3, 4, 7, 4, 7, 7, 3, 6, 8, 7, 7, 8, 4, 6, 5, 2, 4]

# Determining Car speeds in race
car0lapspeed = []
car1lapspeed = []
for x in range(len(OAPCircuit)):
    Randspeed = int(random.randint(1, 5))
    Randposneg = int(random.randint(0, 1))
    if Randposneg == 1:
        car0lapspeed = (OAPCircuit[x] + Randspeed)
        car1lapspeed = (OAPCircuit[x] + Randspeed)
    elif Randposneg == 0:
        car0lapspeed = (OAPCircuit[x] - Randspeed)
        car1lapspeed = (OAPCircuit[x] - Randspeed)
# increasing or decreasing speed depending on the level of aro selected (car0)
if DwnForce0 == 1:
    car0lapspeed[0] = (car0lapspeed[0] - random.randint(0, 5))
    car0lapspeed[1] = (car0lapspeed[1] - random.randint(0, 5))
    car0lapspeed[2] = (car0lapspeed[2] + random.randint(0, 5))
    car0lapspeed[3] = (car0lapspeed[3] + random.randint(0, 5))
    car0lapspeed[4] = (car0lapspeed[4] + random.randint(0, 5))
    car0lapspeed[5] = (car0lapspeed[5] + random.randint(0, 5))
    car0lapspeed[6] = (car0lapspeed[6] - random.randint(0, 5))
    car0lapspeed[7] = (car0lapspeed[7] + random.randint(0, 5))
    car0lapspeed[8] = (car0lapspeed[8] + random.randint(0, 5))
    car0lapspeed[9] = (car0lapspeed[9] - random.randint(0, 5))
    car0lapspeed[10] = (car0lapspeed[10] + random.randint(0, 5))
    car0lapspeed[11] = (car0lapspeed[11] - random.randint(0, 5))
    car0lapspeed[12] = (car0lapspeed[12] + random.randint(0, 5))
    car0lapspeed[13] = (car0lapspeed[13] + random.randint(0, 5))
    car0lapspeed[14] = (car0lapspeed[14] + random.randint(0, 5))
    car0lapspeed[15] = (car0lapspeed[15] - random.randint(0, 5))
    car0lapspeed[16] = (car0lapspeed[16] + random.randint(0, 5))
    car0lapspeed[17] = (car0lapspeed[17] - random.randint(0, 5))
    car0lapspeed[18] = (car0lapspeed[18] + random.randint(0, 5))
    car0lapspeed[19] = (car0lapspeed[19] + random.randint(0, 5))
elif DwnForce0 == 3:
    car0lapspeed[0] = (car0lapspeed[0] + random.randint(0, 5))
    car0lapspeed[1] = (car0lapspeed[1] + random.randint(0, 5))
    car0lapspeed[2] = (car0lapspeed[2] - random.randint(0, 5))
    car0lapspeed[3] = (car0lapspeed[3] - random.randint(0, 5))
    car0lapspeed[4] = (car0lapspeed[4] - random.randint(0, 5))
    car0lapspeed[5] = (car0lapspeed[5] - random.randint(0, 5))
    car0lapspeed[6] = (car0lapspeed[6] + random.randint(0, 5))
    car0lapspeed[7] = (car0lapspeed[7] - random.randint(0, 5))
    car0lapspeed[8] = (car0lapspeed[8] - random.randint(0, 5))
    car0lapspeed[9] = (car0lapspeed[9] + random.randint(0, 5))
    car0lapspeed[10] = (car0lapspeed[10] - random.randint(0, 5))
    car0lapspeed[11] = (car0lapspeed[11] + random.randint(0, 5))
    car0lapspeed[12] = (car0lapspeed[12] - random.randint(0, 5))
    car0lapspeed[13] = (car0lapspeed[13] - random.randint(0, 5))
    car0lapspeed[14] = (car0lapspeed[14] - random.randint(0, 5))
    car0lapspeed[15] = (car0lapspeed[15] + random.randint(0, 5))
    car0lapspeed[16] = (car0lapspeed[16] - random.randint(0, 5))
    car0lapspeed[17] = (car0lapspeed[17] + random.randint(0, 5))
    car0lapspeed[18] = (car0lapspeed[18] - random.randint(0, 5))
    car0lapspeed[19] = (car0lapspeed[19] - random.randint(0, 5))
# increasing or decreasing speed depending on the level of aro selected by user (car1)
if DwnForce1 == 1:
    car1lapspeed[0] = (car1lapspeed[0] - random.randint(0, 5))
    car1lapspeed[1] = (car1lapspeed[1] - random.randint(0, 5))
    car1lapspeed[2] = (car1lapspeed[2] + random.randint(0, 5))
    car1lapspeed[3] = (car1lapspeed[3] + random.randint(0, 5))
    car1lapspeed[4] = (car1lapspeed[4] + random.randint(0, 5))
    car1lapspeed[5] = (car1lapspeed[5] + random.randint(0, 5))
    car1lapspeed[6] = (car1lapspeed[6] - random.randint(0, 5))
    car1lapspeed[7] = (car1lapspeed[7] + random.randint(0, 5))
    car1lapspeed[8] = (car1lapspeed[8] + random.randint(0, 5))
    car1lapspeed[9] = (car1lapspeed[9] - random.randint(0, 5))
    car1lapspeed[10] = (car1lapspeed[10] + random.randint(0, 5))
    car1lapspeed[11] = (car1lapspeed[11] - random.randint(0, 5))
    car1lapspeed[12] = (car1lapspeed[12] + random.randint(0, 5))
    car1lapspeed[13] = (car1lapspeed[13] + random.randint(0, 5))
    car1lapspeed[14] = (car1lapspeed[14] + random.randint(0, 5))
    car1lapspeed[15] = (car1lapspeed[15] - random.randint(0, 5))
    car1lapspeed[16] = (car1lapspeed[16] + random.randint(0, 5))
    car1lapspeed[17] = (car1lapspeed[17] - random.randint(0, 5))
    car1lapspeed[18] = (car1lapspeed[18] + random.randint(0, 5))
    car1lapspeed[19] = (car1lapspeed[19] + random.randint(0, 5))
elif DwnForce1 == 3:
    car1lapspeed[0] = (car1lapspeed[0] + random.randint(0, 5))
    car1lapspeed[1] = (car1lapspeed[1] + random.randint(0, 5))
    car1lapspeed[2] = (car1lapspeed[2] - random.randint(0, 5))
    car1lapspeed[3] = (car1lapspeed[3] - random.randint(0, 5))
    car1lapspeed[4] = (car1lapspeed[4] - random.randint(0, 5))
    car1lapspeed[5] = (car1lapspeed[5] - random.randint(0, 5))
    car1lapspeed[6] = (car1lapspeed[6] + random.randint(0, 5))
    car1lapspeed[7] = (car1lapspeed[7] - random.randint(0, 5))
    car1lapspeed[8] = (car1lapspeed[8] - random.randint(0, 5))
    car1lapspeed[9] = (car1lapspeed[9] + random.randint(0, 5))
    car1lapspeed[10] = (car1lapspeed[10] - random.randint(0, 5))
    car1lapspeed[11] = (car1lapspeed[11] + random.randint(0, 5))
    car1lapspeed[12] = (car1lapspeed[12] - random.randint(0, 5))
    car1lapspeed[13] = (car1lapspeed[13] - random.randint(0, 5))
    car1lapspeed[14] = (car1lapspeed[14] - random.randint(0, 5))
    car1lapspeed[15] = (car1lapspeed[15] + random.randint(0, 5))
    car1lapspeed[16] = (car1lapspeed[16] - random.randint(0, 5))
    car1lapspeed[17] = (car1lapspeed[17] + random.randint(0, 5))
    car1lapspeed[18] = (car1lapspeed[18] - random.randint(0, 5))
    car1lapspeed[19] = (car1lapspeed[19] - random.randint(0, 5))

print(car0lapspeed)
print(car1lapspeed)

