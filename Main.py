from flask import Flask, render_template, request
import sys
import random
import time


app = Flask(__name__)
@app.route('/')
def form():
        return render_template('forms.html')  # Linking flask_app.py to forms.html

@app.route('/home')
def dwnforce():
    DF0 = request.args.get('DF0', '') # Inporting the downforce choice from the forms
    DF1 = request.args.get('DF1', '')
    laplength = 6
    car02bpitted = 0
    car12bpitted = 0
    currenttyre1 = "Medium"
    currenttyre0 = "Medium"
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
    # Lap Speeds
    OAPCircuit = [330, 175, 315, 110, 185, 270, 155, 275, 300, 130, 255, 310, 265, 300, 310, 150, 245, 220, 90, 190] # an bace line speed for each sector


    # Determining Car speeds in race
    for x in range(len(OAPCircuit)):
        Randspeed0 = int(random.randint(1, 100))
        Randposneg0 = int(random.randint(0, 100))
        if Randposneg0 % 2 == 0: # random speed variation
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
    for x in range(len(OAPCircuit)): # random picking downforce levels for other racers
        u = random.randint(1,100)
        if u % 2 == 0:
            botspeed.append(-1)
        else:
            botspeed.append(1)
        print(len(botracers), file=sys.stderr)
        botracers.insert(x, (OAPCircuit[x] + (botspeed[x] * u)))

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


    racersectortime = [sectorgaptime0, sectorgaptime1, sectorgaptimeHAM, sectorgaptimeBOT, sectorgaptimeVER, sectorgaptimeALB, sectorgaptimeNOR, sectorgaptimeRIC,  sectorgaptimeOCO, sectorgaptimeSTR, sectorgaptimePER, sectorgaptimeGRO, sectorgaptimeMAG, sectorgaptimeRUS, sectorgaptimeKVY, sectorgaptimePIE, sectorgaptimeLEC, sectorgaptimeVET, sectorgaptimeRAI, sectorgaptimeGIO]
    for x in range(20): # calculating time taken between sectors from speed and distance
        for i in range(len(car1lapspeed)):
            racersectortime.insert(x, (0.2615 / (racersectortime[i]/3600)))

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
    while lapnumber != 10:
        (lapnumber + 1)

        while car1lapnumber != 10:
            car1lapnumber = (car1lapnumber + 1) # car's lap number
            for y in range(len(car1lapspeed)):
                totaltime1 = (totaltime1 + sectortimegap1[y]) # calculating time taken for entire race
                tyredegrading()
            laptime1 = totaltime1 # lap time
            pit1()

        while car0lapnumber != 10:
            car0lapnumber = (car0lapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltime0 = (totaltime0 + sectortimegap0[y])
                tyredegrading()
            laptime0 = totaltime0
            pit0()

            #enamy driver laps

        while HAMlapnumber != 10:

            HAMlapnumber = (HAMlapnumber + 1) # drivers lap number
            for y in range(len(car0lapspeed)):
                totaltimeHAM = (totaltimeHAM + sectortimegapHAM[y]) # total lap time
            laptimeHAM = totaltimeHAM # laptime
            if botpitHAM != 0:
                ab = random.randint(1, 100)
                if ab % 2 == 0: # randomly pick wether driver should pit
                    totaltimeHAM = (totaltimeHAM + random.randint(15, 25)) # adding time for pit
                    botpitHAM = botpitHAM - 1 # driver can pit max 3 times

        while BOTlapnumber != 10:
            BOTlapnumber = (BOTlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeBOT = (totaltimeBOT + sectortimegapBOT[y])
            laptimeBOT = totaltimeBOT
            if botpitBOT != 0:
                ac = random.randint(1, 100)
                if ac % 2 == 0:
                    totaltimeBOT = (totaltimeBOT + random.randint(15, 25))
                    botpitBOT = (botpitBOT - 1)


        while VERlapnumber != 10:
            VERlapnumber = (BOTlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeVER = (totaltimeVER + sectortimegapVER[y])
            laptimeVER = totaltimeVER
            if botpitVER != 0:
                ad = random.randint(1, 100)
                if ad % 2 == 0:
                    totaltimeVER = (totaltimeVER + random.randint(15, 25))
                    botpitVER = (botpitVER - 1)


        while ALBlapnumber != 10:
            ALBlapnumber = (ALBlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeALB = (totaltimeALB + sectortimegapALB[y])
            laptimeALB = totaltimeALB
            if botpitALB != 0:
                ae = random.randint(1, 100)
                if ae % 2 == 0:
                    totaltimeALB = (totaltimeALB + random.randint(15, 25))
                    botpitALB = (botpitALB - 1)


        while NORlapnumber != 10:
            NORlapnumber = (NORlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeNOR = (totaltimeNOR + sectortimegapNOR[y])
            laptimeNOR = totaltimeNOR
            if botpitNOR != 0:
                af = random.randint(1, 100)
                if af % 2 == 0:
                    totaltimeNOR = (totaltimeNOR + random.randint(15, 25))
                    botpitNOR = (botpitNOR - 1)


        while RIClapnumber != 10:
            RIClapnumber = (RIClapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeRIC = (totaltimeRIC + sectortimegapRIC[y])
            laptimeRIC = totaltimeRIC
            if botpitRIC != 0:
                ag = random.randint(1, 100)
                if ag % 2 == 0:
                    totaltimeRIC = (totaltimeRIC + random.randint(15, 25))
                    botpitRIC = (botpitRIC - 1)


        while OCOlapnumber != 10:
            OCOlapnumber = (OCOlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeOCO = (totaltimeOCO + sectortimegapOCO[y])
            laptimeOCO = totaltimeOCO
            if botpitOCO != 0:
                ah = random.randint(1, 100)
                if ah % 2 == 0:
                    totaltimeOCO = (totaltimeOCO + random.randint(15, 25))
                    botpitOCO = (botpitOCO - 1)


        while STRlapnumber != 10:
            STRlapnumber = (OCOlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeSTR = (totaltimeSTR + sectortimegapSTR[y])
            laptimeSTR = totaltimeSTR
            if botpitSTR != 0:
                ai = random.randint(1, 100)
                if ai % 2 == 0:
                    totaltimeSTR = (totaltimeSTR + random.randint(15, 25))
                    botpitSTR = (botpitSTR - 1)


        while PERlapnumber != 10:
            PERlapnumber = (PERlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimePER = (totaltimePER + sectortimegapPER[y])
            laptimePER = totaltimePER
            if botpitPER != 0:
                aj = random.randint(1, 100)
                if aj % 2 == 0:
                    totaltimePER = (totaltimeSTR + random.randint(15, 25))
                    botpitPER = (botpitPER - 1)


        while GROlapnumber != 10:
            GROlapnumber = (GROlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeGRO = (totaltimeGRO + sectortimegapGRO[y])
            laptimeGOR = totaltimeGOR
            if botpitGRO != 0:
                ak = random.randint(1, 100)
                if ak % 2 == 0:
                    totaltimeGRO = (totaltimeGOR + random.randint(15, 25))
                    botpitGRO = (botpitGRO - 1)


        while MAGlapnumber != 10:
            MAGlapnumber = (MAGlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeMAG = (totaltimeMAG + sectortimegapMAG[y])
            laptimeMAG = totaltimeMAG
            if botpitMAG != 0:
                al = random.randint(1, 100)
                if al % 2 == 0:
                    totaltimeMAG = (totaltimeMAG + random.randint(15, 25))
                    botpitMAG = (botpitMAG - 1)


        while RUSlapnumber != 10:
            RUSlapnumber = (RUSlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeRUS = (totaltimeRUS + sectortimegapRUS[y])
            laptimeRUS = totaltimeRUS
            if botpitRUS != 0:
                am = random.randint(1, 100)
                if am % 2 == 0:
                    totaltimeRUS = (totaltimeRUS + random.randint(15, 25))
                    botpitRUS = (botpitRUS - 1)



        while KVYlapnumber != 10:
            KVYlapnumber = (KVYlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeKVY = (totaltimeKVY + sectortimegapKVY[y])
            laptimeKVY = totaltimeKVY
            if botpitKVY != 0:
                an = random.randint(1, 100)
                if an % 2 == 0:
                    totaltimeKVY = (totaltimeKVY + random.randint(15, 25))
                    botpitKVY = (botpitKVY - 1)


        while PIElapnumber != 10:
            PIElapnumber = (PIElapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimePIE = (totaltimePIE + sectortimegapPIE[y])
            laptimePIE = totaltimePIE
            if botpitPIE != 0:
                ao = random.randint(1, 100)
                if ao % 2 == 0:
                    totaltimePIE = (totaltimePIE + random.randint(15, 25))
                    botpitPIE = (botpitPIE - 1)


        while LEClapnumber != 10:
            LEClapnumber = (LEClapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeLEC = (totaltimeLEC + sectortimegapLEC[y])
            laptimeLEC = totaltimeLEC
            if botpitLEC != 0:
                ap = random.randint(1, 100)
                if ap % 2 == 0:
                    totaltimeLEC = (totaltimeLEC + random.randint(15, 25))
                    botpitLEC = (botpitLEC - 1)


        while VETlapnumber != 10:
            VETlapnumber = (VETlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeVET = (totaltimeVET + sectortimegapVET[y])
            laptimeVET = totaltimeVET
            if botpitVET != 0:
                aq = random.randint(1, 100)
                if aq % 2 == 0:
                    totaltimeVET = (totaltimeVET + random.randint(15, 25))
                    botpitVET = (botpitVET - 1)


        while RAIlapnumber != 10:
            RAIlapnumber = (RAIlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeRAI = (totaltimeRAI + sectortimegapRAI[y])
            laptimeRAI = totaltimeRAI
            if botpitRAI != 0:
                ar = random.randint(1, 100)
                if ar % 2 == 0:
                    totaltimeRAI = (totaltimeRAI + random.randint(15, 25))
                    botpitRAI = (botpitRAI - 1)


        while GIOlapnumber != 10:
            GIOlapnumber = (GIOlapnumber + 1)
            for y in range(len(car0lapspeed)):
                totaltimeGIO = (totaltimeGIO + sectortimegapGIO[y])
            laptimeGIO = totaltimeGIO
            if botpitGIO != 0:
                at = random.randint(1, 100)
                if at % 2 == 0:
                    totaltimeGIO = (totaltimeGIO + random.randint(15, 25))
                    botpitGIO = (botpitGIO - 1)


        tyredegrading1 = (tyredegrading1 - 1)
        tyredegrading0 = (tyredegrading0 - 1)
        print(totaltime1)
        return render_template ('home.html', car0lapnumber=car0lapnumber, laptime1=laptime1, currenttyre0=currentyre0, tyreware0=tyreware0, laptime0=laptime0, currenttyre1=currentyre1, tyreware1=tyreware1, car1lapnumber=car1lapnumber)

def pit1(): # Pit function for car 1
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


def tyredegrading():
        tyre0per = ((tyredegrading0/lapnumber) * 100) # making a percentage of tyre effectiveness / tyreware for car 0
        tyre1per = ((tyredegrading1/lapnumber) * 100) # making a percentage of tyre effectiveness / tyreware for car 1
        if tyre0per <= 0:
            print("car0 out of race")
            car0crash = 1
        elif tyre1per <= 0:
            print("car1 out of race")
            car1crash = 1

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


