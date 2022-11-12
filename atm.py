# ATM Calculator
import pandas as pd
from win32com.client import *
import matplotlib.pyplot as plt
import numpy as np
import pygame
import random
import datetime
import re

speaker = Dispatch('SAPI.SpVoice')
df = pd.read_csv('logindata.csv', index_col=0)
df1 = pd.read_csv('transachist.csv', index_col=0)

print('WELCOME TO TATA ATMs')
speaker.Speak('Welcome to t a t a Automated Teller Machines')


def login():
    while True:
        try:
            choice1 = int(input('Choice: '))
        except Exception as e:
            print('Wrong Data')
            speaker.Speak('Wrong Choice')
            continue
        if choice1 > 0 and choice1 < 4:
            break
        print('Wrong Choice')
        speaker.Speak('Wrong Choice')
        print('Enter again')
        speaker.Speak('Enter Again')
        print()
    return choice1


def checkGmail():

    gml = str(input('Gmail ID: '))
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if (re.fullmatch(regex, gml)):

        return gml

    else:
        print("Invalid Email")
        checkGmail()


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


def ver(usrnm):
    code = random.randint(1000, 9999)
    f = open('vercode.txt', mode='w')
    f.write(str(code))
    f.close()
    return code


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

    choice1 = login()

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

        gml = checkGmail()
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

        aadhar = aadharCheck()
        
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
        speaker.Speak('Services Protocols active')
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
        afterlogin(usrnm)


def afterlogin(usrnm):
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

    while True:
        try:
            choice2 = int(input('Choice: '))
            if str(choice2) in list('123456'):
                break
            else:
                print('Wrong Choice, Enter again')
                speaker.Speak('Wrong Choice')
        except Exception as e:
            continue
            print('Wrong Choice, Enter again')
            speaker.Speak('Wrong Choice')

    if choice2 == 5:
        graphmenu(usrnm)

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

        afterlogin(usrnm)

    if choice2 == 2:

        print()
        speaker.Speak('Here is your transaction history')
        print('Transaction History:---------')

        print()
        print(df1[df1['usrnm'] == usrnm])

        print()
        afterlogin(usrnm)

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

        if len(df1) == 30:
            df1.drop(0, axix=0)
            df1.index = range(29)
        df1.to_csv('transachist.csv')

        print()
        afterlogin(usrnm)

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

        if len(df1) == 30:
            df1.drop(0, axix=0)
            df1.index = range(29)
        df1.to_csv('transachist.csv')

        print()
        afterlogin(usrnm)

def graphChoiceChecker():
    while True:
       
        
        A = int(input('Choice: '))
        if str(A) not in "123":
            speaker.Speak("Wrong Choice")
            continue
       
        return A
        
def graphmenu(usrnm):

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
   
    
    A = graphChoiceChecker()
  
  

    day = []
    month = []
    monthname = []
    daymonth = []
    npp = np.arange(1, 13)

    if A == 1:
        C = "Deposit"
        D = B[B["usrnm"] == usrnm]
        D = D[D["stat"] == C]
        Depo = D["amt"]
        Date = D["serno"]+1

        for i in D["date"]:

            i = str(i)
            S = i[6:8]
            E = i[4:6]
            day.append(S)
            month.append(E)
        for i in month:
            for z in L:
                if i == z:
                    monthname.append(L[z])
                else:
                    pass

        q = 0
        for i in day:

            daymonth.append(i+monthname[q])
            q = q+1

        plt.plot(Date, Depo, color="red", label="Deposit", marker="o")

        plt.grid(True)
        plt.legend()
        plt.title("Amount deposited")
        plt.xticks(Date, labels=daymonth)
        plt.xlabel("Date:------------------->>>>>>>>>>>>")
        plt.ylabel("Amount:------------------->>>>>>>>>>>>")
        speaker.Speak('Here is your graph')
        plt.show()

        day = []
        month = []
        monthname = []
        daymonth = []
        afterlogin(usrnm)

    elif A == 2:
        C = "Withdraw"
        D = B[B["usrnm"] == usrnm]
        D = D[D["stat"] == C]

        Date = D["date"]
        withd = D["amt"]
        Date = D["serno"]+1
        for i in D["date"]:

            i = str(i)
            S = i[6:8]
            E = i[4:6]
            day.append(S)
            month.append(E)
        for i in month:
            for z in L:
                if i == z:
                    monthname.append(L[z])
                else:
                    pass

        q = 0
        for i in day:

            daymonth.append(i+monthname[q])
            q = q+1

        plt.plot(Date, withd, color="red", label="Withdraw", marker="o")
        plt.grid(True)
        plt.legend()
        plt.title("Amount withdrawed")
        plt.xlabel("Date:------------------->>>>>>>>>>>>")
        plt.ylabel("Amount:------------------->>>>>>>>>>>>")
        plt.xticks(Date, labels=daymonth)
        speaker.Speak('Here is your graph')
        plt.show()

        day = []
        month = []
        monthname = []
        daymonth = []
        afterlogin(usrnm)

    elif A == 3:
        # DEPOSIT
        dic = {}
        D = B[B["usrnm"] == usrnm]
        D = D[D["stat"] == "Deposit"]
        T = D["month"]
        T = list(T)
        y = 0
        x = 1
        for i in range(0, 12):
            dic[P[y]] = T.count(x)
            y = y+1
            x = x+1

        dicv = list(dic.values())
        # Withdraw
        vic = {}
        S = B[B["usrnm"] == usrnm]
        S = S[S["stat"] == "Withdraw"]
        J = S["month"]
        J = list(J)
        y = 0
        x = 1
        for i in range(0, 12):
            vic[P[y]] = J.count(x)
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

        afterlogin(usrnm)


menu()
