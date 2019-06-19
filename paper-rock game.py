while True:
    z = input("Do you want to play? Enter y for yes or n for no.")
    if z == "y":
        a = input("What do you want to play, player 1?")
        b = input("What do you want to play, player 2?")
        if a==b:
            print("It's a tie.")
            elif (a == "p" and b == "r") or (a == "r" and b == "s") or (a == "s" and b == "p"):
                print("Player 1 wins. Congratulations!")
            elif (a == "p" and b == "s") or (a == "r" and b == "p") or (a == "s" and b == "r"):
                print("Player 2 wins. Congratulations!")
            else:
                print("You typed something wrong. Please, try again. This time enter p, r or s.")
