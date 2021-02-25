from flask import Flask, render_template, request
import random
import time
import threading

global car1lapnumber
totaltime1 = 0
car1lapnumber = 0
laplength = 6
tyre0per = 0
tyre1per = 0
laptime1 = 0
laptime0 = 0
car02bpitted = 0
car12bpitted = 0
currenttyre1 = "Medium"
currenttyre0 = "Medium"
tobtyre1 = ""
global  Finish
Finish = 0
tobtyre0 = ""
car0crash = 0
car1crash = 0
global tyredegrading0
global tyredegrading1
car0crash = 1
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
botpitHAM = 3
botpitBOT = 3
botpitVER = 3
botpitALB = 3
botpitNOR = 3
botpitRIC = 3
botpitOCO = 3
botpitSTR = 3
botpitPER = 3
botpitGRO = 3
botpitMAG = 3
botpitRUS = 3
botpitKVY = 3
botpitPIE = 3
botpitLEC = 3
botpitVET = 3
botpitRAI = 3
botpitGIO = 3
botpitHAM = 3
car0lapnumber = 0
car1lapnumber = 0
HAMlapnumber = 0
BOTlapnumber = 0
VERlapnumber = 0
ALBlapnumber = 0
NORlapnumber = 0
RIClapnumber = 0
OCOlapnumber = 0
STRlapnumber = 0
PERlapnumber = 0
GROlapnumber = 0
MAGlapnumber = 0
RUSlapnumber = 0
KVYlapnumber = 0
PIElapnumber = 0
LEClapnumber = 0
VETlapnumber = 0
RAIlapnumber = 0
GIOlapnumber = 0
totaltime1 = 0
totaltime0 = 0
totaltimeHAM = 0
totaltimeBOT = 0
totaltimeVER = 0
totaltimeALB = 0
totaltimeNOR = 0
totaltimeRIC = 0
totaltimeOCO = 0
totaltimeSTR = 0
totaltimePER = 0
totaltimeGRO = 0
totaltimeMAG = 0
totaltimeRUS = 0
totaltimeKVY = 0
totaltimePIE = 0
totaltimeLEC = 0
totaltimeVET = 0
totaltimeRAI = 0
totaltimeGIO = 0
tyre0per = 0
tyre1per = 0
laptime1 = 0
laptime0 = 0
totaltime1 = 0
car1lapnumber = 0

app = Flask(__name__)
@app.route('/')
def form():
        return render_template('forms.html')  # Linking flask_app.py to forms.html

@app.route('/home')
def dwnforce():
    DF0 = request.args.get('DF0', '')
    DF1 = request.args.get('DF1', '')
    DF0 = 0
    DF1 = 1
    # Lap Speeds
    OAPCircuit = [330.0, 175.0, 315.0, 110.0, 185.0, 270.0, 155.0, 275.0, 300.0, 130.0, 255.0, 310.0, 265.0, 300.0, 310.0, 150.0, 245.0, 220.0, 90.0, 190.0] # an bace line speed for each sector

    # Determining Car speeds in race
    for x in range(len(OAPCircuit)):
        Randspeed0 = int(random.randint(1.0, 100.0))
        Randposneg0 = int(random.randint(0, 100))
        if Randposneg0 % 2 == 0: # random speed variation
            car0lapspeed.append((OAPCircuit[x] + Randspeed0))
        else:
            car0lapspeed.append((OAPCircuit[x] - Randspeed0))
        Randspeed1 = int(random.randint(1.0, 100.0))
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
    for x in range(len(OAPCircuit)): # random picking downforce levels for other racers
        u = random.randint(1,100)
        if u % 2 == 0:
            botspeed.append(-1)
        else:
            botspeed.append(1)

    for x in range(len(OAPCircuit)): # calculating sector speed
        botracers.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        HAMlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        BOTlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        VERlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        ALBlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        NORlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        RIClapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        OCOlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        STRlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        PERlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        GROlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        MAGlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        RUSlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        KVYlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        PIElapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        LEClapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        VETlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        RAIlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))
        GIOlapspeed.insert(x, (OAPCircuit[x] + random.randint(1, 5)))

    if DF0 == 1: # Applying differnces to speed depending on aro levels
        for x in range(19):
            car0lapspeed.append(car0lapspeed[x] + (plusminushigh[x] * random.randint(0, 5)))

    elif DF0 == 3: # Applying differnces to speed depending on aro levels
        for x in range(19):
            car0lapspeed.append(car0lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))

    # increasing or decreasing speed depending on the level of aro selected by user
    if DF1 == 1: # Applying differnces to speed depending on aro levels
        for x in range(19):
            car1lapspeed.append(car1lapspeed[x] + (plusminushigh[x] * random.randint(0, 5)))

    elif DF1 == 3: # Applying differnces to speed depending on aro levels
        for x in range(19):
            car1lapspeed.append(car1lapspeed[x] + (plusminuslow[x] * random.randint(0, 5)))

    for x in range(len(car1lapspeed)): # giving variation to the speeds for the bots
            botracers.insert(x, (botracers[x] + (u * random.randint(1, 5))))

    for x in range(20): # calculating time taken between sectors from speed and distance
        sectorgaptime0.insert(x, float(0.2615 / (car1lapspeed[x]/3600.0)))
        sectorgaptime1.insert(x, float(0.2615 / (car0lapspeed[x]/3600.0)))
        sectorgaptimeHAM.insert(x, float(0.2615 / (HAMlapspeed[x]/3600.0)))
        sectorgaptimeBOT.insert(x, float(0.2615 / (BOTlapspeed[x]/3600.0)))
        sectorgaptimeVER.insert(x, float(0.2615 / (VERlapspeed[x]/3600.0)))
        sectorgaptimeALB.insert(x, float(0.2615 / (ALBlapspeed[x]/3600.0)))
        sectorgaptimeNOR.insert(x, float(0.2615 / (NORlapspeed[x]/3600.0)))
        sectorgaptimeRIC.insert(x, float(0.2615 / (RIClapspeed[x]/3600.0)))
        sectorgaptimeOCO.insert(x, float(0.2615 / (OCOlapspeed[x]/3600.0)))
        sectorgaptimeSTR.insert(x, float(0.2615 / (STRlapspeed[x]/3600.0)))
        sectorgaptimePER.insert(x, float(0.2615 / (PERlapspeed[x]/3600.0)))
        sectorgaptimeGRO.insert(x, float(0.2615 / (GROlapspeed[x]/3600.0)))
        sectorgaptimeMAG.insert(x, float(0.2615 / (MAGlapspeed[x]/3600.0)))
        sectorgaptimeRUS.insert(x, float(0.2615 / (RUSlapspeed[x]/3600.0)))
        sectorgaptimeKVY.insert(x, float(0.2615 / (KVYlapspeed[x]/3600.0)))
        sectorgaptimePIE.insert(x, float(0.2615 / (PIElapspeed[x]/3600.0)))
        sectorgaptimeLEC.insert(x, float(0.2615 / (LEClapspeed[x]/3600.0)))
        sectorgaptimeVET.insert(x, float(0.2615 / (VETlapspeed[x]/3600.0)))
        sectorgaptimeRAI.insert(x, float(0.2615 / (RAIlapspeed[x]/3600.0)))
        sectorgaptimeGIO.insert(x, float(0.2615 / (GIOlapspeed[x]/3600.0)))

    race()
    return render_template('home.html', car1lapnumber=car1lapnumber, tyre1per=tyre1per, totaltime1=totaltime1, car0lapnumber=car0lapnumber, tyre0per=tyre0per, totaltime0=totaltime0)

def tyredegrading():
    global tyredegrading1
    global tyredegrading0
    global tyre0per
    global tyre1per
    tyre0per = ((tyredegrading0/laplength) * 100) # making a percentage of tyre effectiveness / tyreware for car 0
    tyre1per = ((tyredegrading1/laplength) * 100) # making a percentage of tyre effectiveness / tyreware for car 1
    if tyre0per <= 0:
        global car0crash
        car0crash = 1
    elif tyre1per <= 0:
        global car1crash
        car1crash = 1

def pit1(): # Pit function for car 1
    global tyredegrading1
    global tyredegrading0
    tobtyre1 = request.args.get('Car1', '') # inporting the choice of tyre from home.html
    if tobtyre1 == "Soft":
        for x in range(sectorgaptime1):
            sectorgaptime1.append(sectorgaptime1[x] - 0.6) # decreasing time between sectors so car1 goes faster
        tyredegrading1 = 2 # number of laps untill tyres ware out
        sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25)) # time taken from changing tyres

    elif tobtyre1 == "Medium":
        tyredegrading1 = 3 # number of laps untill tyres ware out
        sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25)) # time taken from changing tyres
    elif tobtyre1 == "Hard":
        for x in range(sectorgaptime1):
            sectorgaptime1.append(sectorgaptime1[x] + 0.7)# increasing time between sectors so car1 goes slower

        tyredegrading1 = 4 # number of laps untill tyres ware out
        sectorgaptime1.append(sectorgaptime1[x] + random.randint(15, 25)) # time taken from changing tyres

def pit0(): # Pit function for car 0
    tobtyre0 = request.args.get('Car0', '') # inporting the choice of tyre from home.html
    if tobtyre0 == "Soft":
        for x in range(sectorgaptime0):
            sectorgaptime0.append(sectorgaptime0[x] - 0.6) # decreasing time between sectors so car0 goes faster
        tyredegrading0 = 2 # number of laps untill tyres ware out
        sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25)) # time taken from changing tyres

    elif tobtyre0 == "Medium":
        tyredegrading0 = 3 # number of laps untill tyres ware out
        sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25)) # time taken from changing tyres

    elif tobtyre0 == "Hard":
        for x in range(sectorgaptime0):
            sectorgaptime0.append(sectorgaptime0[x] + 0.7) # increasing time between sectors so car0 goes slower
        tyredegrading0 = 4 # number of laps untill tyres ware out
        sectorgaptime0.append(sectorgaptime0[x] + random.randint(15, 25)) # time taken from changing tyres

def car1R():
    global totaltime1
    global car1lapnumber
    global tyredegrading1
    while car1lapnumber != 10:
        car1lapnumber = (car1lapnumber + 1) # car's lap number
        for y in range(len(car1lapspeed)):
            totaltime1 = (totaltime1 + sectorgaptime1[y]) # calculating time taken for entire race
            tyredegrading()
            time.sleep(sectorgaptime1[y])
        laptime1 = totaltime1 # lap time
        pit1()
        tyredegrading1 = (tyredegrading1 - 1)
        if car1crash == 1:
            car1lapnumber = (10)

def car0R():
    global totaltime0
    global car0lapnumber
    global tyredegrading0
    while car0lapnumber != 10:
        car0lapnumber = (car0lapnumber + 1)  # car's lap number
        for y in range(len(sectorgaptime0)):
            totaltime0 = (totaltime0 + sectorgaptime0[y])  # calculating time taken for entire race
            tyredegrading()
            time.sleep(sectorgaptime1[y])
        laptime0 = totaltime0  # lap time
        tyredegrading0 = (tyredegrading0 - 1)
        if car0crash == 1:
            car1lapnumber = (10)
#enamy driver laps

def HAMR():
    global totaltimeHAM
    global HAMlapnumber
    botpitHAM = 3
    while HAMlapnumber != 10:
        HAMlapnumber = (HAMlapnumber + 1) # drivers lap number
        for y in range(len(car0lapspeed)):
            totaltimeHAM = (totaltimeHAM + sectorgaptimeHAM[y]) # total lap time
            time.sleep(sectorgaptimeHAM[y])
        if botpitHAM != 0:
            ab = random.randint(1, 100)
            if ab % 2 == 0: # randomly pick wether driver should pit
                totaltimeHAM = (totaltimeHAM + random.randint(15, 25)) # adding time for pit
                botpitHAM = botpitHAM - 1 # driver can pit max 3 times

def BOTR():
    global totaltimeBOT
    global BOTlapnumber
    botpitBOT = 3
    while BOTlapnumber != 10:
        BOTlapnumber = (BOTlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeBOT = (totaltimeBOT + sectorgaptimeBOT[y])
            time.sleep(sectorgaptimeBOT[y])
        if botpitBOT != 0:
            ac = random.randint(1, 100)
            if ac % 2 == 0:
                totaltimeBOT = (totaltimeBOT + random.randint(15, 25))
                botpitBOT = (botpitBOT - 1)

def VERR():
    global totaltimeVER
    global VERlapnumber
    botpitVER = 3
    while VERlapnumber != 10:
        VERlapnumber = (VERlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeVER = (totaltimeVER + sectorgaptimeVER[y])
            time.sleep(sectorgaptimeVER[y])
        if botpitVER != 0:
            ad = random.randint(1, 100)
            if ad % 2 == 0:
                totaltimeVER = (totaltimeVER + random.randint(15, 25))
                botpitVER = (botpitVER - 1)

def ALBR():
    global totaltimeALB
    global ALBlapnumber
    botpitALB = 3
    while ALBlapnumber != 10:
        ALBlapnumber = (ALBlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeALB = (totaltimeALB + sectorgaptimeALB[y])
            time.sleep(sectorgaptimeALB[y])
        if botpitALB != 0:
            ae = random.randint(1, 100)
            if ae % 2 == 0:
                totaltimeALB = (totaltimeALB + random.randint(15, 25))
                botpitALB = (botpitALB - 1)

def NORR():
    global totaltimeNOR
    global NORlapnumber
    botpitNOR = 3
    while NORlapnumber != 10:
        NORlapnumber = (NORlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeNOR = (totaltimeNOR + sectorgaptimeNOR[y])
            time.sleep(sectorgaptimeNOR[y])
        if botpitNOR != 0:
            af = random.randint(1, 100)
            if af % 2 == 0:
                totaltimeNOR = (totaltimeNOR + random.randint(15, 25))
                botpitNOR = (botpitNOR - 1)

def RICR():
    global totaltimeRIC
    global RIClapnumber
    botpitRIC = 3
    while RIClapnumber != 10:
        RIClapnumber = (RIClapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeRIC = (totaltimeRIC + sectorgaptimeRIC[y])
            time.sleep(sectorgaptimeRIC[y])
        if botpitRIC != 0:
            ag = random.randint(1, 100)
            if ag % 2 == 0:
                totaltimeRIC = (totaltimeRIC + random.randint(15, 25))
                botpitRIC = (botpitRIC - 1)

def OCOR():
    global totaltimeOCO
    global OCOlapnumber
    botpitOCO = 3
    while OCOlapnumber != 10:
        OCOlapnumber = (OCOlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeOCO = (totaltimeOCO + sectorgaptimeOCO[y])
            time.sleep(sectorgaptimeOCO[y])
        if botpitOCO != 0:
            ah = random.randint(1, 100)
            if ah % 2 == 0:
                totaltimeOCO = (totaltimeOCO + random.randint(15, 25))
                botpitOCO = (botpitOCO - 1)

def STRR():
    global totaltimeSTR
    global STRlapnumber
    botpitSTR = 3
    while STRlapnumber != 10:
        STRlapnumber = (STRlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeSTR = (totaltimeSTR + sectorgaptimeSTR[y])
            time.sleep(sectorgaptimeSTR[y])
        if botpitSTR != 0:
            ai = random.randint(1, 100)
            if ai % 2 == 0:
                totaltimeSTR = (totaltimeSTR + random.randint(15, 25))
                botpitSTR = (botpitSTR - 1)

def PERR():
    global totaltimePER
    global PERlapnumber
    botpitPER = 3
    while PERlapnumber != 10:
        PERlapnumber = (PERlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimePER = (totaltimePER + sectorgaptimePER[y])
            time.sleep(sectorgaptimePER[y])
        if botpitPER != 0:
            aj = random.randint(1, 100)
            if aj % 2 == 0:
                totaltimePER = (totaltimeSTR + random.randint(15, 25))
                botpitPER = (botpitPER - 1)

def GROR():
    global totaltimeGRO
    global GROlapnumber
    botpitGRO = 3
    while GROlapnumber != 10:
        GROlapnumber = (GROlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeGRO = (totaltimeGRO + sectorgaptimeGRO[y])
            time.sleep(sectorgaptimeGRO[y])
        if botpitGRO != 0:
            ak = random.randint(1, 100)
            if ak % 2 == 0:
                totaltimeGRO = (totaltimeGOR + random.randint(15, 25))
                botpitGRO = (botpitGRO - 1)

def MAGR():
    global totaltimeMAG
    global MAGlapnumber
    botpitMAG = 3
    while MAGlapnumber != 10:
        MAGlapnumber = (MAGlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeMAG = (totaltimeMAG + sectorgaptimeMAG[y])
            time.sleep(sectorgaptimeMAG[y])
        if botpitMAG != 0:
            al = random.randint(1, 100)
            if al % 2 == 0:
                totaltimeMAG = (totaltimeMAG + random.randint(15, 25))
                botpitMAG = (botpitMAG - 1)

def RUSR():
    global totaltimeRUS
    global RUSlapnumber
    botpitRUS = 3
    while RUSlapnumber != 10:
        RUSlapnumber = (RUSlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeRUS = (totaltimeRUS + sectorgaptimeRUS[y])
            time.sleep(sectorgaptimeRUS[y])
        if botpitRUS != 0:
            am = random.randint(1, 100)
            if am % 2 == 0:
                totaltimeRUS = (totaltimeRUS + random.randint(15, 25))
                botpitRUS = (botpitRUS - 1)

def KVYR():
    global totaltimeKVY
    global KVYlapnumber
    botpitKVY = 3
    while KVYlapnumber != 10:
        KVYlapnumber = (KVYlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeKVY = (totaltimeKVY + sectorgaptimeKVY[y])
            time.sleep(sectorgaptimeKVY[y])
        if botpitKVY != 0:
            an = random.randint(1, 100)
            if an % 2 == 0:
                totaltimeKVY = (totaltimeKVY + random.randint(15, 25))
                botpitKVY = (botpitKVY - 1)

def PIER():
    global totaltimePIE
    global PIElapnumber
    botpitPIE = 3
    while PIElapnumber != 10:
        PIElapnumber = (PIElapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimePIE = (totaltimePIE + sectorgaptimePIE[y])
            time.sleep(sectorgaptimePIE[y])
        if botpitPIE != 0:
            ao = random.randint(1, 100)
            if ao % 2 == 0:
                totaltimePIE = (totaltimePIE + random.randint(15, 25))
                botpitPIE = (botpitPIE - 1)

def LECR():
    global totaltimeLEC
    global LEClapnumber
    botpitLEC = 3
    while LEClapnumber != 10:
        LEClapnumber = (LEClapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeLEC = (totaltimeLEC + sectorgaptimeLEC[y])
            time.sleep(sectorgaptimeLEC[y])
        if botpitLEC != 0:
            ap = random.randint(1, 100)
            if ap % 2 == 0:
                totaltimeLEC = (totaltimeLEC + random.randint(15, 25))
                botpitLEC = (botpitLEC - 1)

def VETR():
    global totaltimeVET
    global VETlapnumber
    botpitVET = 3
    while VETlapnumber != 10:
        VETlapnumber = (VETlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeVET = (totaltimeVET + sectorgaptimeVET[y])
            time.sleep(sectorgaptimeVET[y])
        if botpitVET != 0:
            aq = random.randint(1, 100)
            if aq % 2 == 0:
                totaltimeVET = (totaltimeVET + random.randint(15, 25))
                botpitVET = (botpitVET - 1)

def RAIR():
    global totaltimeRAI
    global RAIlapnumber
    botpitRAI = 3
    while RAIlapnumber != 10:
        RAIlapnumber = (RAIlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeRAI = (totaltimeRAI + sectorgaptimeRAI[y])
            time.sleep(sectorgaptimeRAI[y])
        if botpitRAI != 0:
            ar = random.randint(1, 100)
            if ar % 2 == 0:
                totaltimeRAI = (totaltimeRAI + random.randint(15, 25))
                botpitRAI = (botpitRAI - 1)

def GIOR():
    global totaltimeGIO
    global GIOlapnumber
    botpitGIO = 3
    while GIOlapnumber != 10:
        GIOlapnumber = (GIOlapnumber + 1)
        for y in range(len(car0lapspeed)):
            totaltimeGIO = (totaltimeGIO + sectorgaptimeGIO[y])
            time.sleep(sectorgaptimeGIO[y])
        if botpitGIO != 0:
            at = random.randint(1, 100)
            if at % 2 == 0:
                totaltimeGIO = (totaltimeGIO + random.randint(15, 25))
                botpitGIO = (botpitGIO - 1)

#Functions for each car (multi threading)
t1 = threading.Thread(target=car1R)
t2 = threading.Thread(target=car0R)
t3 = threading.Thread(target=HAMR)
t4 = threading.Thread(target=BOTR)
t5 = threading.Thread(target=VERR)
t6 = threading.Thread(target=ALBR)
t7 = threading.Thread(target=NORR)
t8 = threading.Thread(target=RICR)
t9 = threading.Thread(target=OCOR)
t10 = threading.Thread(target=STRR)
t11 = threading.Thread(target=PERR)
t12 = threading.Thread(target=GROR)
t13 = threading.Thread(target=MAGR)
t14 = threading.Thread(target=RUSR)
t15 = threading.Thread(target=KVYR)
t16 = threading.Thread(target=PIER)
t17 = threading.Thread(target=LECR)
t18 = threading.Thread(target=VETR)
t19 = threading.Thread(target=RAIR)
t20 = threading.Thread(target=GIOR)

def race():
    print(laplength)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()
    t17.start()
    t18.start()
    t19.start()
    t20.start()
    Finish = 1
    return render_template('home.html', car1lapnumber=car1lapnumber, tyre1per=tyre1per, laptime1=laptime1, car0lapnumber=car0lapnumber, tyre0per=tyre0per, laptime0=laptime0, Finish=Finish)

@app.route('/podium')
def podium():
    LB = [totaltime1, totaltime0, totaltimeHAM, totaltimeBOT, totaltimeVER, totaltimeALB, totaltimeNOR, totaltimeRIC, totaltimeOCO, totaltimeSTR, totaltimePER, totaltimeGRO, totaltimeMAG, totaltimeRUS, totaltimeKVY, totaltimePIE, totaltimeLEC, totaltimeVET, totaltimeRAI, totaltimeGIO]
    numItems = len(LB) # get number of items in the array
    for i in range(numItems - 2):
        for j in range(numItems - i - 2):
            if LB[j] > LB[j + 1]:
                temp = LB[j]
                LB[j] = LB[j + 1]
                LB[j + 1] = temp


    return render_template('podium.html')  # Linking flask_app.py to podium.html
