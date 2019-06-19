import random
a = random.randint(1, 10)
count = 0
while 1:
    x = input("Guess the number please or type EXIT: ")
    if a == "exit":
        print("your score is this:", count)
        break
    if a == x:
        count += 1
        print("Wow! You guessed the number")
    elif a > x:
        print("too high")
    elif a < x:
        print("too small")