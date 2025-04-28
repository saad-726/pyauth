u_id="user@gmail.com"
u_password="123"
a_id="admin@gmail.com"
a_password="123"
def user():
    print("Welcome user")
def admin():
    print("Welcome admin")
def authenticate(id,password):
    if id==u_id and password==u_password:
        user()
    elif id==a_id and password==a_password:
        admin()
    else:
        print("You are not a registered user")
id=input("Enter your id :")
password=input("Enter your password :")

authenticate(id,password)