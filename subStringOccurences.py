fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)