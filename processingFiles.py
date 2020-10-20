from os import strerror

try:
    cnt = 0
    s = open("processingPython", "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file: ", cnt)
except IOError as e:
    print("I/O error occured: ", strerr(e.errno))

try:
    ccnt = lcnt = 0
    s = open('processingPython', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file: ", ccnt)
    print("Line in file:       ", lcnt)
except IoError as e:
    print("I/O error occurred:", strerr(e.erno))

try:
    fo = open('newtext.txt', 'wt')
    for i in range(10):
        s = "Line #" + str(i+1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))

stream = open("newtext.txt", "rt")
print(stream.read())
