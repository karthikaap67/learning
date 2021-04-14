def showNumbers(lmt):
    for i in range(0, lmt + 1):
        if i % 2 == 0:
            print("{} EVEN".format(i))
        else:
            print("{} ODD".format(i))



if __name__ == "__main__":
    inp = int(input("Enter a limit: "))
    showNumbers(inp)
