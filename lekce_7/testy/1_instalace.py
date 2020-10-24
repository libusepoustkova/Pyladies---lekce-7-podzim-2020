#1. Instalujte knihovnu pytest
#     - python -m pip install pytest ... pip je modul
#     - Pokud je vse v poradku: Successfully installed iniconfig-1.1.1 py-1.9.0 pytest-6.1.1 toml-0.10.1
#
# 2. Spousteni testu
#    - python -m pytest -v [jmeno-souboru.py]
#    - python -m pytest -v 1_instalace.py
#1_instalace.py::test_secti PASSED                                                                                [100%]
#================================================== 1 passed in 0.02s ==================================================
def secti(a, b):
    return a + b

def test_secti():
    assert secti(1, 2) == 3
