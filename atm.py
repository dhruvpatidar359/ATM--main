""" 
This program/software is a basic ATM(Automated Teller Machine) Software that
can do things like :

1> Login , Signup 
2> Deposit , WithDraw , See Graphs(of deposits and withdraw)
3> Account Details , Transaction history

Special Features of this ATM Project : 

1> It consist of Audio instructions in it
2> It can also show graph of deposits , withdraw
3> Have security system like OTP , that occurs in the same text file 
that is present in this directory

"""


# Importing necessary modules

import pandas as pd
from win32com.client import *
from subprocess import call
import matplotlib.pyplot as plt
import numpy as np
import pygame
import random
import datetime
import re
import cProfile
import pstats
from pstats import SortKey

speaker = Dispatch('SAPI.SpVoice')
df = pd.read_csv('logindata.csv', index_col=0)
df1 = pd.read_csv('transachist.csv', index_col=0)


print('WELCOME TO TATA ATMs')
speaker.Speak('Welcome to tata Automated Teller Machines')



""" This function checks whether the mail is correct or not 
, it checks all the possible mistakes that can be in the gmail
"""


def checkEmail():

    gml = str(input('Gmail ID: '))
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, gml)):

        return gml

    else:
        print("Invalid Email")
        checkEmail()


""" 
This function checks whether the entered password is go to go or 
not , as the password should be secure , should not be to easy
"""


def passCheck():
    l, u, p, d = 0, 0, 0, 0
    s = str(input('Password: '))
    if (len(s) >= 8):
        for i in s:

            # counting lowercase alphabets
            if (i.islower()):
                l += 1

            # counting uppercase alphabets
            if (i.isupper()):
                u += 1

            # counting digits
            if (i.isdigit()):
                d += 1

            # counting the mentioned special characters
            if (i == '@' or i == '$' or i == '_'):
                p += 1
    if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+p+u+d == len(s)):
        return s
    else:
        print("invalid password")
        passCheck()


# As the name suggest , it checks the correctness of aadhar number


def aadharCheck():
    while True:
        try:
            aadhar = int(input('Aadhar No.: '))
        except Exception as e:
            print('Wrong Data')
            speaker.Speak('Wrong Data')
            print('Please Enter Again')
            speaker.Speak('Enter again')
            continue
        if len(str(aadhar)) == 12 and aadhar not in df['aadhar']:
            break

        print('Wrong Data')
        speaker.Speak('Wrong Data')
        print('Please Enter Again')
        speaker.Speak('Enter again')
    return aadhar

# This function help in communicating between CSV file and
# Frontend


def ver(usrnm):
    code = random.randint(1000, 9999)
    f = open('vercode.txt', mode='w')
    f.write(str(code))
    f.close()
    return code


""" 
This is the main driving method of the software , that initiate
program having Login , Sign up and Exit option 
"""


def menu():
    print('TATA ATMs')
    print()

    print('''
1. Login
2. Sign up
3. Exit''')

    print()
    speaker.Speak('Enter your choice')
    print('Enter your choice(1 or 2 or 3)')

    choice1 = call(["./choiceLogin"])

    print()

    if choice1 == 3:
        print('Have a Good Day')
        speaker.Speak('Have a good day')

    if choice1 == 2:
        print('Welcome to Account Creator')
        speaker.Speak('Welcome to account creator')
        print('Please provide these informations kindly')
        speaker.Speak('Kindly provide necessary informations')
        print()

        # gml = checkEmail()
        call(["./checkEmail"])
        f = open("checkEmail.txt", "r")
        gml = f.read()

        f.close()
        print()

        usrnm = str(input('UserName: '))
        print()

        passw = passCheck()
        print()

        name = str(input('Full Name: '))
        print()

        while True:
            gender = str(input('Gender(m or f): '))
            if gender in list('mMfF'):
                break

            print('Wrong data')
            speaker.Speak('Wrong data')
            print('Please enter again')
            speaker.Speak('Enter again')
        print()

        call(["./aadharCheck"])
        # aadhar = call(["./aadharCheck"])

        ff = open("checkAadhar.txt", "r")
        aadhar = ff.read()
        ff.close()

        while True:

            if usrnm in df.index:
                print('Username already in use, type another one')
                speaker.Speak('Username already in use')
                usrnm = str(input('UserName: '))

            if usrnm not in df.index:
                break

        df.loc[usrnm, 'gml'] = gml
        df.loc[usrnm, 'passw'] = passw
        df.loc[usrnm, 'amount'] = 0
        df.loc[usrnm, 'name'] = name
        df.loc[usrnm, 'gender'] = gender
        df.loc[usrnm, 'aadhar'] = aadhar

        print('Your account has been created')
        speaker.Speak('Your account has been created')
        print('Enjoy our services')
        speaker.Speak('Enjoy our Services')
        print()

        df.to_csv('logindata.csv')
        print()

        pygame.time.wait(2000)
        menu()

    if choice1 == 1:

        print('Welcome Sir\\Madam')
        print('Security Protocols Active')
        speaker.Speak('Security Protocols active')
        print()

        while True:
            usrnm = str(input('Username: '))
            if usrnm in df.index:
                break
            print('Wrong Username')
            speaker.Speak('Wrong data input')

        while True:

            passw = str(input('Password: '))

            a = df.loc[usrnm, 'passw']

            if type(a) == np.float64:
                a = int(a)

            if passw == str(a):
                break

            print('Wrong Password')
            speaker.Speak('Wrong Password')

        print()
        afterLogin(usrnm)


""" 
This is the second most important driving function that drives 
the function after the login stage , here you can access to the 
Graphs , Account Information and many more things
"""


def afterLogin(usrnm):
    print('Welcome {}'.format(df.loc[usrnm, 'name']))
    speaker.Speak('Welcome {}'.format(df.loc[usrnm, 'name']))
    print()

    print('''
    1. Account Information
    2. Transaction History
    3. Deposit Money
    4. Withdraw Money
    5. Graphical Representation
    6. Exit''')

    print()

    choice2 = call(["./choiceAfterLogin"])

    if choice2 == 5:
        graphMenu(usrnm)

    if choice2 == 6:
        menu()

    if choice2 == 1:
        print('''Status: Active
    Name: {}
    Gender: {}
    Aadhar: {}
    Balance: Rs.{}
    Gmail: {}
    At Risk : No'''.format(df.loc[usrnm, 'name'], df.loc[usrnm, 'gender'], df.loc[usrnm, 'aadhar'], df.loc[usrnm, 'amount'], df.loc[usrnm, 'gml']))

        afterLogin(usrnm)

    if choice2 == 2:

        print()
        speaker.Speak('Here is your transaction history')
        print('Transaction History:---------')

        print()
        print(df1[df1['usrnm'] == usrnm])

        print()
        afterLogin(usrnm)

    if choice2 == 3:

        code = ver(usrnm)
        print()
        print('Type Verification Code to proceed>>>>>')
        print('Type verification code')
        print('You\'ve got a verification code in a text file in the same directory')
        speaker.Speak('Type verification code to proceed')
        print()
        while True:
            try:
                cd = int(input('Code: '))
                if cd == code:
                    print('User Verified')
                    speaker.Speak('Welcome user')
                    print()
                    break
                else:
                    print('Wrong code')
                    speaker.Speak('Wrong Choice')
                    print('Type again')
                    continue
                    print()
            except Exception as e:
                print('Wrong code')
                speaker.Speak('Wrong Choice')
                print('Type again')
                print()
                continue

        while True:
            try:
                csh = int(input('Amount of Cash to be deposited: '))
                if csh > 0:
                    break
                print('Wrong Data')
                speaker.Speak('Wrong Choice')

            except Exception as e:
                print('Wrong Data')
                speaker.Speak('Wrong Choice')
                continue

        x = datetime.datetime.now()
        y_x = str(x.year)
        m_x = str(x.month)
        d_x = str(x.day)
        if len(m_x) == 1:
            m_x = '0' + m_x
        if len(d_x) == 1:
            d_x = '0' + d_x
        g = len(df1)

        df1.loc[g, 'date'] = y_x + m_x + d_x
        df1.loc[g, 'month'] = m_x

        df.loc[usrnm, 'amount'] = df.loc[usrnm, 'amount'] + csh
        df.to_csv('logindata.csv')
        df1.loc[g, 'amt'] = csh
        df1.loc[g, 'stat'] = 'Deposit'
        df1.loc[g, 'usrnm'] = usrnm

        print('Cash Deposited')
        speaker.Speak('Cash Deposited')

        df1.to_csv('transachist.csv')

        print()
        afterLogin(usrnm)

    if choice2 == 4:

        code = ver(usrnm)
        print()
        print('Type Verification Code to proceed>>>>>')
        speaker.Speak('Type verification code to proceed')
        print('You\'ve got a verification code in a text file in the same directory')
        print()
        while True:
            try:
                cd = int(input('Code: '))
            except Exception as e:
                print('Wrong code')
                speaker.Speak('Wrong Code')
                print('Type again')
                print()
                continue
            if cd == code:
                print('User Verified')
                print()
                break
            print('Wrong code')
            speaker.Speak('Wrong Code')
            print('Type again')
            print()

        while True:
            try:
                csh = int(input('Amount of Cash to Withdraw: '))

            except Exception as e:

                print('Wrong Data')
                speaker.Speak('Wrong data')
                continue

            if csh > 0 and csh < df.loc[usrnm, 'amount']:
                break
            print('Wrong Data')
            speaker.Speak('Wrong data')

        x = datetime.datetime.now()
        y_x = str(x.year)
        m_x = str(x.month)
        d_x = str(x.day)
        if len(m_x) == 1:
            m_x = '0' + m_x
        if len(d_x) == 1:
            d_x = '0' + d_x
        g = len(df1)

        df1.loc[g, 'date'] = y_x + m_x + d_x
        df1.loc[g, 'month'] = m_x

        df.loc[usrnm, 'amount'] = df.loc[usrnm, 'amount'] + csh
        df.to_csv('logindata.csv')
        df1.loc[g, 'amt'] = csh
        df1.loc[g, 'stat'] = 'Withdraw'
        df1.loc[g, 'usrnm'] = usrnm

        print('Cash Withdrawn')
        speaker.Speak('Cash withdrawn')

        df1.to_csv('transachist.csv')

        print()
        afterLogin(usrnm)


# As the name suggest a choice checker function for graphs


def graphChoiceChecker():
    while True:

        A = int(input('Choice: '))
        if str(A) not in "123":
            speaker.Speak("Wrong Choice")
            continue

        return A


""" 
This is the third important driving function that drives the
function for the graph purposes
"""


def graphMenu(usrnm):

    speaker.Speak('Welcome to advanced a i graphical stat calculator')
    print("*******Choose the type of data that you want to see*******")
    print("""1:Deposit""")
    print("""2:Withdraw""")
    print("3:Approx transaction per month")
    L = {"01": "Jan", "02": "Feb", "03": "March", "04": "April", "05": "May", "06": "June",
         "07": "July", "08": "Aug", "09": "Sept", "10": "Oct", '11': "Nov", '12': "Dec"}
    P = ["Jan", "Feb", "March", "April", "May", "June",
         "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    B = pd.read_csv("transachist.csv")

    choiceForGraph = graphChoiceChecker()

    day = []
    month = []
    monthName = []
    dayMonth = []
    npp = np.arange(1, 13)

    if choiceForGraph == 1:
        depString = "Deposit"
        seriesUsr = B[B["usrnm"] == usrnm]
        seriesUsr = seriesUsr[seriesUsr["stat"] == depString]
        Depo = seriesUsr["amt"]
        Date = seriesUsr["serno"]+1

        for i in seriesUsr["date"]:

            i = str(i)
            seriesUser3 = i[6:8]
            E = i[4:6]
            day.append(seriesUser3)
            month.append(E)
        for i in month:
            for z in L:
                if i == z:
                    monthName.append(L[z])
                else:
                    pass

        q = 0
        for i in day:

            dayMonth.append(i+monthName[q])
            q = q+1

        plt.plot(Date, Depo, color="red", label="Deposit", marker="o")

        plt.grid(True)
        plt.legend()
        plt.title("Amount deposited")
        plt.xticks(Date, labels=dayMonth)
        plt.xlabel("Date:------------------->>>>>>>>>>>>")
        plt.ylabel("Amount:------------------->>>>>>>>>>>>")
        speaker.Speak('Here is your graph')
        plt.show()

        day = []
        month = []
        monthName = []
        dayMonth = []
        afterLogin(usrnm)

    elif choiceForGraph == 2:
        depString = "Withdraw"
        seriesUsr = B[B["usrnm"] == usrnm]
        seriesUsr = seriesUsr[seriesUsr["stat"] == depString]

        Date = seriesUsr["date"]
        withdraw = seriesUsr["amt"]
        Date = seriesUsr["serno"]+1
        for i in seriesUsr["date"]:

            i = str(i)
            seriesUser3 = i[6:8]
            E = i[4:6]
            day.append(seriesUser3)
            month.append(E)
        for i in month:
            for z in L:
                if i == z:
                    monthName.append(L[z])
                else:
                    pass

        q = 0
        for i in day:

            dayMonth.append(i+monthName[q])
            q = q+1

        plt.plot(Date, withdraw, color="red", label="Withdraw", marker="o")
        plt.grid(True)
        plt.legend()
        plt.title("Amount withdrawed")
        plt.xlabel("Date:------------------->>>>>>>>>>>>")
        plt.ylabel("Amount:------------------->>>>>>>>>>>>")
        plt.xticks(Date, labels=dayMonth)
        speaker.Speak('Here is your graph')
        plt.show()

        day = []
        month = []
        monthName = []
        dayMonth = []
        afterLogin(usrnm)

    elif choiceForGraph == 3:

        # DEPOSIT
        dic = {}
        seriesUsr = B[B["usrnm"] == usrnm]
        seriesUsr = seriesUsr[seriesUsr["stat"] == "Deposit"]
        monthSeries = seriesUsr["month"]
        monthSeries = list(monthSeries)
        y = 0
        x = 1
        for i in range(0, 12):
            dic[P[y]] = monthSeries.count(x)
            y = y+1
            x = x+1

        dicv = list(dic.values())
        # Withdraw
        vic = {}
        seriesUser3 = B[B["usrnm"] == usrnm]
        seriesUser3 = seriesUser3[seriesUser3["stat"] == "Withdraw"]
        monthSeries3 = seriesUser3["month"]
        monthSeries3 = list(monthSeries3)
        y = 0
        x = 1
        for i in range(0, 12):
            vic[P[y]] = monthSeries3.count(x)
            y = y+1
            x = x+1

        vicv = list(vic.values())
        # Deposit bar
        plt.bar(npp, dicv, color='orange', width=0.2, label="Deposit")
        # withdraw bar
        plt.bar(npp+0.2, vicv, color='red', width=0.2, label="Withdraw")
        plt.xticks(npp, labels=P)
        plt.grid(True)
        plt.legend()
        plt.ylabel("No. of approx transactions per month")
        plt.xlabel("Month")
        plt.title('Approx transaction per month')
        speaker.Speak('Here is your graph')
        plt.show()

        afterLogin(usrnm)


# This is the driver function

if __name__ == "__main__":
    cProfile.run("menu()", "output.dat")

    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
