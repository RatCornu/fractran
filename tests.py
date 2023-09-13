from fractran import fractran

def test_addition():
     assert fractran([(3, 2)], (2 ** 3) * (3 ** 4)) == 3 ** (3 + 4)
     assert fractran([(3, 2)], (2 ** 5) * (3 ** 2)) == 3 ** (5 + 2)

def test_multiplication():
     assert fractran([(455, 33), (11, 13), (1, 11), (3, 7), (11, 2), (1, 3)], (2**2) * (3**2) == 5 ** (2*2))

def test_final():
     fractions = [(17,65), (133,34), (17,19), (23,17), (2233,69), (23,29), (31,23), (74,341), (31,37), (41,31), (129,287), (41,43), (13,41), (1,13), (1,3)]
     x = 1
     n = 78*5**x
     print(fractran(fractions, n))

test_multiplication()
