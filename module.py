#!/Users/matthewshakespeare/Desktop/Coding/python/module.py (3.8.2)

"""module.py- an example of python module"""

__counter = 0

def suml(list):
    global __counter
    __counter += 1
    sum = 0   
    for el in list:
        sum += el
    return sum

def prodl(list):
    global __counter
    __counter += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but i can do some tests for you")
    l = [i + l for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)
