users = {}


def terminate():
    print()
    print("Summary info: the program contains " + str(len(users)), "users.")
    quit()


def processAddUser():
    user = input("Enter a username")
    user_tk = users.get(user)
    if user_tk == None:
        fname = input("Enter First Name")
        lname = input("Enter Last Name")
        about = input("Enter 'about me' section")
        info = [fname, lname, about]
        users[user] = info
        print(users)
        print("added")


def processEditUser():
    username = input("Enter the username to edit: ")
    user = users.get(username)
    if not user == None:
        fname = input("Enter First Name")
        lname = input("Enter Last Name")
        about = input("Enter 'about me' section")
        info = [fname, lname, about]
        users[username] = info
        print(username, users[username])
    else:
        print("Could not find:", username)


def processDeleteUser():
    user = input("Enter the username: ")
    user_tk = users.get(user)
    if not user_tk == None:
        del users[user]
        print("User: " + user + " deleted")
    else:
        print("Could not find:", user)


def processPrintUser():
    firstName = input("Enter first name: ")
    user = users.get(firstName)
    if not user == None:
        print(user)
