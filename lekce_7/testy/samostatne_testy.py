
def test_dospely_za_plnou_cenu():
    assert spocitej_slevu_jizdneho(30.0, 35) == 30.0

def test_mladez_za_polovinu():
    assert spocitej_slevu_jizdneho(30.0, 18) == 15.0

def test_senior_za_tretinu():
    assert spocitej_slevu_jizdneho(30.0, 70) == 10.0
