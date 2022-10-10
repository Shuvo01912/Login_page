# this is basic text line login page
import time
print("Secure Login ..................")

class user:
    name = ' '
    email = ''
    password = ''
    login=  False

    def login(self):
        email = input("Enter Your Gmail : ")
        password = input("Enter Your Password : ")
        if email == self.email and password == self.password :
            login = True
            print("login Successfully")
        else:
            print("Login Failed :) ")
user.name='Shuvo'
user.email = 'shuvo@gmail.com'
user.password = "1234"

shuvo=user()
shuvo.login()
print('Surff Application ')
time.sleep(5)

