import passwordManager


def menu():
    print("WELCOME TO PASSWORD MANAGEMENT SYSTEM")
    print("-----------------------")
    print("1. Create password")
    print("2. Retrive password")
    print("3. Delete password")
    print("4. List Sites")
    print("5. Quit")
    print("-----------------------\n")

    userInput = int(input("Enter option: "))
    return userInput
