

def operation():
    dictx = {}
    with open("test.txt", "r") as newfile:
        line = newfile.readline()
        while line:
            line = line[3:-26]
            if line in dictx:
                dictx[line] += 1
            else:
                dictx[line] = 1
            line  = newfile.readline()
    print(dictx)

if __name__ == "__main__":
    operation()