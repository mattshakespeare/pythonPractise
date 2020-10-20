myList = [8, 10, 6, 2, 4]

for i in range(len(myList)- 1):
    if myList[i] > myList[i + 1]:
        myList[i], myList[i + 1] = myList[i + 1], myList[i]
print(myList)

myList1 = [5, 2, 78, 65, 4, 2, 44]
swapped = True

while swapped:
    swapped = False
    for i in range(len(myList1)- 1):
        if myList1[i] > myList1[i + 1]:
            swapped = True
            myList1[i], myList1[i+1] = myList1[i+1], myList1[i]
print(myList1)