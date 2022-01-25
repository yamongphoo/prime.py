#login system

from time import sleep

counter = 0

while True:

    username = 'client404'
    password = 'client040'

    Name = input("please input username: ")
    Pass = input("please enter your passcode: ")

    if (Name == username and Pass == password):
        print("Login Successful!...")
        break

    elif( Name != username ):
        print (" Incorrect username, please try again")
        counter += 1

    elif( Pass != password):
        print(" Incorrect passcode, please try again")
        counter += 1

    if (counter == 2):
        print(" login suspended ,please wait for a moment....")
        for i in range (1,4):
            print(f'{i}s')
            sleep(2)
            counter = 0
    
