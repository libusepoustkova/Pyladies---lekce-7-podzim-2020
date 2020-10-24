def ziskej_vek_uzivatele():
    while True:
        vekRetezec = input('Zadej prosim svuj vek!\n')

        # Co se stane kdyz uzivatel zada retezec nebo desetinne cislo?
        try:
            vek = int(vekRetezec)
        except ValueError: #slo by sem dat i Exception:
            print(f"{vekRetezec} neni platne cele cislo!")
            continue #jde to zpatky na vhile

        if vek < 0:
            print("Vek nemuze byt zaporne cislo!")
        elif vek > 120:
            print("To asi zertujes?")
        else:
            print("Vse je v poradku.")
            return vek

vek_uzivatele = ziskej_Vek_uzivatele()
print(f"Uzivatel zadal vek {vek_uzivatele}")
