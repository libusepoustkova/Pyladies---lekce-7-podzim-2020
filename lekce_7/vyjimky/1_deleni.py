def ziskej_delenec():
    return int(input('Zadej Delenec: '))

def ziskej_delitel():
    return int(input('Zadej Delitel: '))

def vydel(delenec, delitel):

    return delenec / delitel

delenec = ziskej_delenec()
delitel = ziskej_delitel()
podil = vydel(delenec, delitel)

print(f"{delenec} deleno {delitel} je {podil}")
