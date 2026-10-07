from bonjour import saluer
def test_saluer_Malak():
   assert saluer("Malak") == "Bonjour Malak"
def test_saluer_vide():
   assert saluer("") == "Bonjour "