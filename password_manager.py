user_id = input("Enter the Username: ")
password = input("Enter the Password: ")

def add():
    with open("password.txt", "a") as f:
        f.write(user_id , "|", password + "/n")


