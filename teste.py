print("Hello World")

testing = input("Did you have a good day (y/n): ").lower()

while True:
    if testing == "y":
        print("Very nice")
        break
    elif testing == "n":
        print("I hope better days come")
        break
    else:
        print("not a valid answer lol")