import hashlib
from operator import truediv
import secrets
import csv
from tabnanny import check
from urllib import request

CSV_FILE = "passwords.csv"
MASTER_HASH_FILE = "master.txt"

def masterHashComapare(password):
    master = open(MASTER_HASH_FILE)
    masterLines = master.read().splitlines()
    token = masterLines[0]
    hash = hashlib.sha512((token + password).encode('utf-8')).hexdigest()
    if (hash == masterLines[1]):
        return True
    else:
        return False

def paswordshahash(password):
    hashedpass = hashlib.sha1(password.encode())
    return hashedpass.hexdigest().upper()

def checkhash(hashedpass):
    setpass=hashedpass[:5]
    r = request.get("https://api.pwnedpasswords.com/range/"+setpass)   
    return r.text

def passinhibp(pw):
    list=checkhash(paswordshahash(pw))     
    for line in list.splitlines():
        con=line.split(":")
        if con[0] == paswordshahash(pw)[5:]:
            return True
        else:
            pass
    return False        



def createMasterHashFile(password):
    with open(CSV_FILE, mode='w') as password_file:
        password_writer = csv.writer(password_file, delimiter=',', quotechar='"')
        password_writer.writerow(["site", "username", "token", "hash"])
    master = open(MASTER_HASH_FILE, 'w')
    token = secrets.token_hex(64)
    hash = hashlib.sha512((token + password).encode('utf-8')).hexdigest()
    master.write("%s\n" % token)
    master.write("%s\n" % hash)
    master.close()

def hashPassword(password, length):
    token = secrets.token_hex(64)
    hash = hashlib.sha512((token + password).encode('utf-8')).hexdigest()
    hash = hash[:length]
    return token,hash


def checkingPass(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def writeCsv(site, username, token, hash):
    try:
        readCsv("site")
    except FileNotFoundError:
        with open(CSV_FILE, mode='a') as password_file:
            password_writer = csv.writer(password_file, delimiter=',', quotechar='"')
            password_writer.writerow(["site", "username", "token", "hash"])
    with open(CSV_FILE, mode='a') as password_file:
            password_writer = csv.writer(password_file, delimiter=',', quotechar='"')
            password_writer.writerow([site, username, token, hash])


def readCsv(site):
    with open(CSV_FILE) as password_file:
        password_reader = csv.reader(password_file, delimiter=',')
        line_count = 0
        for row in password_reader:
            if(line_count != 0):
                if (row[0] == site):
                    return row
            line_count += 1


def updateusePass(site):
    listupdate=[]
    with open(CSV_FILE) as password_file:
        password_reader=csv.reader(password_file, delimiter=',')
        print("Change Password?")
        username=input("please enter username")
        for row in password_reader:
            for field in row:

                    if field==username: 
                        listupdate=listupdate.append(row) 
                        newpass=input("Enter new password")
                        listupdate[0][1] = newpass

        updatepassword(listupdate)

def updatepassword(listupdate):
       with open(CSV_FILE) as password_file:
            Writer=csv.writer(password_file)
            Writer.writerows(listupdate)
            print("File has been updated")





def deleteCsv(site):
    changes = list()
    with open(CSV_FILE) as password_file:
        password_reader = csv.reader(password_file, delimiter=',')
        for row in password_reader:
            if (row[0] != site):
                changes.append(row)

    with open(CSV_FILE, mode="w") as password_file:
        password_writer = csv.writer(password_file, delimiter=',', quotechar='"')
        password_writer.writerows(changes)


def listSites():
    with open(CSV_FILE) as password_file:
        password_reader = csv.reader(password_file, delimiter=',')
        sites = list()
        line_count = 0
        for row in password_reader:
            if (line_count != 0):
                sites.append(row[0])
            line_count += 1
    return sites

