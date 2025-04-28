# Predefined admin and user credentials
u_id = "user@gmail.com"
u_password = "123"
a_id = "admin@gmail.com"
a_password = "123"

# Lists to store registered users
userID = []
userPassword = []

def register():
    n_id = input("Enter your id: ")
    n_password = input("Enter your password: ")
    
    if n_id != "" and n_password != "":
        userID.append(n_id)
        userPassword.append(n_password)
        print("User registered successfully!\n")
    else:
        print("Retry and make sure not to leave it empty.\n")

def user():
    print("Welcome user\n")

def admin():
    print("Welcome admin\n")

def authenticate(id, password):
    if id == u_id and password == u_password:
        user()
    elif id == a_id and password == a_password:
        admin()
    elif id in userID:
        index = userID.index(id)
        if userPassword[index] == password:
            user()
        else:
            print("Incorrect password.\n")
    else:
        print("You are not a registered user.")
        choice = input("Type 'yes' to enroll a new user (yes/no): ")
        if choice.lower() == "yes":
            register()
        else:
            print("Exiting...")

# Main program flow
id = input("Enter your id: ")
password = input("Enter your password: ")

authenticate(id, password)
