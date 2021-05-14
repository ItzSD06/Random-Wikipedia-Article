import wikipedia #importing the module

print("--Random Wikipedia Article Generator--")
print("0. Exit")
print("1. Search New Topic")

while True:
    print("\n")
    choice = int(input("Enter 0 for Exit and 1 for New Topic (0 or 1): "))#new topic or exit
    print("\n")
    if choice == 0:#if-else statement
        print("We can't wait to see you again, bye bye...")
        break
    elif choice == 1:
        title = wikipedia.random(1)
        print("Would you like to read about - ", title)
        while True:#while True loop
            confirmchoice = input("Enter y for yes and n for no (y or n): ")
            if confirmchoice == "y" or confirmchoice == "Y":
                summary = wikipedia.summary(title)
                url = wikipedia.page(title).url
                print("\n")
                print(summary)
                print("Read more at -",url)
                break
            elif confirmchoice == "n" or confirmchoice == "N":
                break
            else:
                print("Please enter y or n.")
                continue
    else:
        print("Please enter only 0 or 1")
        continue
