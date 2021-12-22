""""First way"""

_variable = 1
def test():
    global _variable
    _variable += 1
    print(_variable)
test()


"""Second way"""
var2 = 1
def test2():
    return var2 + 1
print(test2())

"""Global constants"""
PI = 3.1416
"""it has to be declared with uppercase"""
