while True:
    a = int(input("enter some number:"))
    b = []

    for i in range(1,100):
        num = a%i
        if num == 0:
            b.append(i)
            print(b)
            x=input("do u wanna try again? Y or N")
            if x == "n" or "N":
                break

    
