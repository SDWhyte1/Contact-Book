import sqlite3
count = 0
carryOn = True
conn = sqlite3.connect('contactdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Contact;


CREATE TABLE Contact (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    address TEXT,
    number INTEGER,
    email TEXT
)
''')
while carryOn:

    name = input(str("Please enter the name: "))

    #print(name, address, number, email)

    answer = input("Please select whether you would like to add, update or delete from the contact book: ")
    answer = answer.lower()
    if answer == 'add':
        address = input("Please enter the address interested in: ")
        number = int(input("Please enter the phone number: "))
        email = input(str("Please enter the email address: "))
        if email.find("@") == -1:
            print("Please enter an email address")
            exit()
        cur.execute('''INSERT OR REPLACE INTO Contact
        (name, address, number, email)
            VALUES ( ?, ?, ?, ? )''',
            ( name, address, number, email) )
        count = count +1

    elif answer == "update" and count >= 1:
        #updateName = input("Please enter the name of the Contact you wish to update: ")
        updateAddress = input("Please enter the new Address: ")
        updateNumber = input("Please enter the new Phone Number: ")
        updateEmail = input("Please enter the new Email: ")
        if updateEmail.find("@") == -1:
            print("Please enter an email address")
            exit()
        cur.execute(''' UPDATE Contact
        SET address = ?,
        number = ?,
        email = ?
        WHERE name = ?; ''', (updateAddress, updateNumber,updateEmail,name))


    elif answer == "delete" and count >= 1:
        #deleteName = input("Please enter the name of the Contact you wish to delete: ")
        cur.execute('''DELETE FROM Contact
        where name = ? ''', (name,))

    else:
        print("Please enter a valid input")


    conn.commit()

    more = input("Do you have more db queries to execute, input y or n: ")
    if more != "y":
        carryOn = False
