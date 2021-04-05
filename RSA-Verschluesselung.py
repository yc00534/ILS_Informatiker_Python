def rsa_verschluesselung(kette, e, n):
    codiert = ""
    for zeichen in kette:
        codiert = codiert + str(ord(zeichen) ** e % n) + " "
    print(codiert)

rsa_verschluesselung("Geheimtreffenabgesagt", 37, 3713)


def rsa_entschluesseln(kette, d, n):
    decodiert = ""
    einzelneCodierteZeichenAlsArray = kette.split(" ")
    for stelle in range(len(einzelneCodierteZeichenAlsArray)):
        decodiert = decodiert + chr((int(einzelneCodierteZeichenAlsArray[stelle])**d % n))


    print(decodiert)

rsa_entschluesseln("1875 3089 3521 3089 167 186 2373 1815 3089 1366 1366 3089 3233", 97, 3713)
