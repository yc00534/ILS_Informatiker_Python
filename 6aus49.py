n = 49
k = 6

def fakultaetMethode(i):
    fakultaet = 1
    while i > 0:
        fakultaet = fakultaet * i
        i = i - 1
    return fakultaet

print((fakultaetMethode(n)) / (fakultaetMethode(k) * fakultaetMethode(n - k)))
