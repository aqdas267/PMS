import hashlib
import secrets
import csv

CSV_FILE = "passwords.csv"
MASTER_HASH_FILE = "master.txt"

def masterHashComapare(password):
    master = open(MASTER_HASH_FILE)
    masterLines = master.read().splitlines()
    salt = masterLines[0]
    hash = hashlib.sha512((salt + password).encode('utf-8')).hexdigest()
    if (hash == masterLines[1]):
        return True
    else:
        return False

def createMasterHashFile(password):
    with open(CSV_FILE, mode='w') as password_file:
        password_writer = csv.writer(password_file, delimiter=',', quotechar='"')
        password_writer.writerow(["site", "username", "salt", "hash"])
    master = open(MASTER_HASH_FILE, 'w')
    salt = secrets.token_hex(64)
    hash = hashlib.sha512((salt + password).encode('utf-8')).hexdigest()
    master.write("%s\n" % salt)
    master.write("%s\n" % hash)
    master.close()

def hashPassword(password, length):
    salt = secrets.token_hex(64)
    hash = hashlib.sha512((salt + password).encode('utf-8')).hexdigest()
    hash = hash[:length]
    return salt,hash

