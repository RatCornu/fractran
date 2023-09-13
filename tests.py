from fractran import fractran

def test_exemple():
     assert fractran([(3, 2)], (2 ** 3) * (3 ** 4)) == 3 ** (3 + 4)
     assert fractran([(3, 2)], (2 ** 5) * (3 ** 2)) == 3 ** (5 + 2)

def test_final():
     assert True