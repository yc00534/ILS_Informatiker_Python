#Permutationen für eine Liste

from random import shuffle

def mischen(karten: list, wiederholungen: int):
    noch_mal = 1
    while noch_mal <= wiederholungen:
        shuffle(karten)
        print("Durchgang: ", noch_mal)
        print(karten)
        noch_mal = noch_mal + 1

spielkarten = []

index = 1
while index <= 32:
    spielkarten.append(index)
    index = index + 1

print(spielkarten)
print("TYP:", type(spielkarten))
mischen(spielkarten, wiederholungen=22)