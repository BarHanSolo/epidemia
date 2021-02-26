import random

def estTable(animalCond):
    animalList = []

    for a in animalCond:
        for x in range(a[0]):
            animalList.append((a[1],a[2]))

    return animalList

def breed(animals):
    animalsList = animals
    for a in animalsList:
        if (a[0])>=2 and (a[0])<=4:
            if random.random() < (0.15 + random.uniform(-0.02, 0.02)):
                if random.random() < countIllWithAge(animalsList, a[0])/countWithAge(animalsList, a[0]):
                    animalsList.append((0, 4))
                else:
                    animalsList.append((0, 0))
        elif (a[0])>=5:
            if random.random() < (0.10 + + random.uniform(-0.01, 0.01)):
                if random.random() < countIllWithAge(animalsList, a[0])/countWithAge(animalsList, a[0]):
                    animalsList.append((0, 4))
                else:
                    animalsList.append((0, 0))
    return animalsList

def countIll(animals):
    ill = 0
    for a in animals:
        if a[1]>1:
            ill += 1
    return ill

def countIllWithAge(animals, age):
    ill = 0
    for a in animals:
        if a[1]>1 and a[0] == age:
            ill += 1
    return ill

def countWithAge(animals, age):
    withAge = 0
    for a in animals:
        if a[0] == age:
            withAge += 1
    return withAge


def dieAge(animals):
    # średnie wieki zwierząt przeliczone z odchylenia standardowego (suma 18) 4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,8
    animalsList = animals
    for id, a in enumerate(animalsList):
        if (a[0]==4 or a[0]==8) and random.random() < (1/18):
            animalsList.pop(id)
        elif (a[0]==5 or a[0]==7) and random.random() < (5/18):
            animalsList.pop(id)
        elif a[0]==6 and random.random() < (6/18):
            animalsList.pop(id)
    return animalsList

def dieIllness(animals):
    animalsList = animals
    for id, a in enumerate(animalsList):
        if (a[0] > 0 and a[0] <= 3) and random.random() < (0.2 + random.uniform(-0.05, 0.05)):
            animalsList.pop(id)
        elif (a[0] >= 4 and a[0] <= 5) and random.random() < (0.3 + random.uniform(-0.07, 0.07)):
            animalsList.pop(id)
        elif a[0] >= 6 and random.random() < (0.5 + random.uniform(-0.15, 0.15)):
            animalsList.pop(id)
    return animalsList

def die(animals):
    animals = dieAge(animals)
    animals = dieIllness(animals)
    return animals

def infect(animals, contagiousness, contact):
    animalsList = animals
    for id, a in enumerate(animalsList):
        for x in range(contact):
            if random.choice(animalsList)[1] > 1 and random.random() < (contagiousness/100):
                animalsList[id] = (animalsList[id][0], 4) #4 preinfection state; it will change to 3 with passtime
    return animalsList

def passTime(animals): #changes illnes numbers with time
    animalsList = animals
    for id, a in enumerate(animalsList):
        if a[1]>0:
            animalsList[id] = (animalsList[id][0]+1, animalsList[id][1]-1)
        else:
            animalsList[id] = (animalsList[id][0] + 1, animalsList[id][1])
    return animalsList #state of the beggining of next period


def makeSimulation(length, contagiousness, contact):
    simulationLength = length
    contagiousnessPercent = contagiousness
    contactAnimals = contact
    animalCond = [
        (60, 1, 0),  # 60 zwierząt w wieku 1, które nie są chore
        (20, 1, 1),  # 20 zwierząt w wieku 1, które mają czasową odporność
        (10, 1, 3),  # 10 zwierząt w wieku 1, faza 1 choroby
        (10, 1, 2),  # 10 zwierząt w wieku 1, faza 2 choroby

        (60, 2, 0),
        (30, 2, 1),
        (10, 2, 3),
        (20, 2, 2),

        (70, 3, 0),
        (10, 3, 1),
        (5, 3, 3),
        (10, 3, 2),

        (60, 4, 0),
        (10, 4, 1),
        (10, 4, 3),
        (5, 4, 2),

        (20, 5, 0),
        (20, 5, 1),
        (7, 5, 3),
        (3, 5, 2),

        (10, 6, 0),
        (5, 6, 1),
        (6, 6, 3),
        (4, 6, 2),

        (10, 7, 0),
        (3, 7, 2),
    ]  # initial conditions for animals: tuples (count, age, illness)
    animals = estTable(animalCond)  # estabilshes table of animals based on the animalCond

    for x in range(simulationLength):  # every loop is one time unit
        # print(countIll(animals))
        print(len(animals))

        animals = infect(animals, contagiousnessPercent, contactAnimals)
        animals = breed(animals)
        animals = die(animals)
        animals = passTime(animals)

        print("Year: " + str(x))
        print(countIll(animals))
        # for a in animals:
        #    print(a)
        # print(len(animals))


if __name__ == '__main__':
    makeSimulation(20, 5, 10)