from encdec import *
from getpass import getpass
from data.user import user
from database import database
from settings import settings


# instance for settings
sett = settings()
db = database()
key = load_key()
dec = decrypt(user,key)

passwd = getpass('Enter your Password : ')

def UI():
    print('1 : Add Data')
    print('2 : Update Record')
    print('3 : Delete Record')
    print('4 : Exit')
    return sett.integer_in('Enter Here : ')

incorrect = 0

while 1:
    sett.cls()
    if passwd == dec:
        print('Records Are :-\n')
        db.viewall()
        ch = UI()
        if ch == 1:
            desc = input("Enter The Decription : ")
            p = getpass("Enter The Password : ")
            enc = encrypt(msg=p,key=key)
            db.insert(desc,enc.decode())
            print('Added..')

        elif ch == 2:
            i = input("Enter The ID : ")
            p = getpass("Enter The New Password : ")
            enc = encrypt(p,key)
            db.update(i,enc.decode())
            print("Updated...")

        elif ch == 3:
            i = input("Enter The ID : ")
            db.delete(i)
            print('Deleted')
        else:
            print("Exit")
            break
    elif incorrect ==3:
            print('Database is gong to deleted...')
    else:
        print('incorrect..') 
        incorrect+=1
    sett.sec(1)
    