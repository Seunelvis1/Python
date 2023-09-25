print('Nigeria is an African Country')
Age = [20, 40, 30, 16]

for i in Age:
  print(i)

class Student():
  name = "Adeniran"
  Age = 38
  Gender = "Male"

#Basic Login in Python
print("craate User credentials")

username = input("Enter your Username: ")
password = input("Enter your password: ")
print("You have created an account successfully")
print("Login Now!")
username2 = input("Enter your username: ")
password2 = input("Enter your password: ")

if username == username2 and password == password2:
  print("Login Successful")
else:
  print("Wrong Credentials")

def say_hi(name):
    print("hi", name)