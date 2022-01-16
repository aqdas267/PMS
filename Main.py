import passwordManager

def menu():
    print("WELCOME TO PASSWORD MANAGEMENT SYSTEM")
    print("-----------------------")
    print("1. Create password")
    print("2. Retrive password")
    print("3. Update Password")
    print("4. Delete password")
    print("5. List Sites")
    print("6. Quit")
    print("-----------------------\n")

    userInput = int(input("Enter option: "))
    return userInput

passwordAttempts = 0
while(True):
    try:
        password = input("Enter master password: ")
        if(not passwordManager.masterHashComapare(password)):
            if (passwordAttempts > 1):
                print("\n**TOO MANY WRONG ATTEMPTS**\n")
                raise SystemExit(0)
            else:
                print("\n**WRONG PASSWORD**\n")
                passwordAttempts += 1
                continue
        else:
            print("\nPASSWORD CORRECT\n")
            break
    except FileNotFoundError:
        print("\nMaster password file doesn't exist. Creating master file. Initializing Database.\n")
        passwordManager.createMasterHashFile(password)
        break

while(True):
  
    try:
        choice = menu()
        if (choice < 1 or choice > 5):
            print("\n**INVALID MENU OPTION**\n")
    except ValueError:
        print("\n**INVALID MENU OPTION**\n")
        continue

    if (choice == 1):
        site = input("Enter site name: ")
        if (site == "site"):
            print("\n**INVALID SITE NAME**\n")
            continue
        try:
            if (passwordManager.readCsv(site) != None):
                print("\n**SITE ALREADY EXISTS**\n")
                continue
        except FileNotFoundError:
            pass
        username = input("Enter username for %s: " % site)
        password = input("Enter simple password to be hashed: ")
        try:
            length = int(input("Enter length of hashed password (1-128): "))
        except ValueError:
            print("\n**NO INPUT SETTING LENGTH TO 16**\n")
            length = 16
        hashTuple = passwordManager.hashPassword(password, length)
        passwordManager.writeCsv(site, username, hashTuple[0], hashTuple[1])
        print("\nPASSWORD HASHED AND SAVED SUCCESSFULLY\n")

    if (choice == 2):
        site  = input("Enter site to retrive: ")
        if (site == "site"):
            print("\n**INVALID SITE NAME**\n")
            continue
        try:
            if (passwordManager.readCsv(site) == None):
                print("\n**NO SITE FOUND**\n")
                continue
            else:
                csvRow = passwordManager.readCsv(site)
                print("\n")
                print("SITE: %s" % csvRow[0])
                print("USERNAME: %s" % csvRow[1])
                print("PASSWORD: %s" % csvRow[3])
                print("\n")
        except FileNotFoundError:
            print("\n**PASSWORDS FILE DOES NOT EXIST, CREATE A PASSWORD**\n")

    if (choice == 3):
        site = input("Enter site to update password")
        if (site == "site"):
            print("\n**INVALID SITE NAME**")
            continue
        elif (passwordManager.readCsv(site) == None):
            print("\n**NO SITE FOUND**\n")
            continue
        else:
            passwordManager.updateusePass(site)
            print("\nPASSWORD SUCCESSFULLY UPDATED\n")       

    if (choice == 4):
        site = input("Enter site to delete: ")
        if (site == "site"):
            print("\n**INVALID SITE NAME**\n")
            continue
        elif (passwordManager.readCsv(site) == None):
            print("\n**NO SITE FOUND**\n")
            continue
        else:
            passwordManager.deleteCsv(site)
            print("\nSITE DELETED SUCCESSFULLY\n")
    
    if (choice == 5):
        if (passwordManager.listSites()):
            counter = 1
            print("\n")
            for site in passwordManager.listSites():
                print("%i: %s" % (counter,site))
                counter += 1
            print("\n")
        else:
            print("\nNO SITES IN FILE\n")
        
    if (choice == 6):
        print("\nGOODBYE! :)\n")
        break
