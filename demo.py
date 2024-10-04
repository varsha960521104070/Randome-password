import random
print("Welcome to random password generated")
randomchars = "ABCDEFGHIJKLMNOPQRSTUVWXYAabcdefghijklmnopqrstuvwxyz@#$%&"
ranofpsw = int(input("Please ender the number of passwords to be generated: "))
pwdlen = int(input("Please ender the lenght of the password needed: "))
print("Here are your randome password:")
for x in range(ranofpsw):
    pwd =''
    for chars in range(pwdlen):
        pwd = pwd + random.choice(randomchars)
    print(pwd)
