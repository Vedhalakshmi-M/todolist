import random
print("welcome to random password generator!")
randomchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
num_of_passwords=int(input("Please enter number of password to be generated:"))
password_len=int(input("Please enter length of password to be generated:"))
print("Here are your paasword:")
for x in range(num_of_passwords):
    pwd=""
    for chars in range(password_len):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
