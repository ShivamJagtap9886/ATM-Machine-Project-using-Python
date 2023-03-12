while True:
    balance = 10000
    print(" ATM ")
    print('''
    Please select one of the option from below:
    1)  Balance
    2)  Withdraw
    3)  Deposite
    4)  Quit
    ''')
    try:
        Option = int(input('Enter your Option:'))
    except Exception as e:
        print('Error:',e)
        print('Enter 1,2,3 or 4 only')
        continue
    if Option == 1:
        print('Balance $',balance)
    if Option == 2:
        print('Balance $',balance)
        withdraw = float(input('Enter Withdrow amount:'))
        if withdraw > 0:
            forwordbalance = (balance - withdraw)
            print('Remaining balance',forwordbalance)
        elif withdraw > balance:
            print('Insufficient Balance')
        else:
            print('None withdrow made')
    if Option == 3:
        print('Balance $',balance)
        Deposite = float(input('Enter Deposite Amount $'))
        if Deposite > 0:
            forwordbalance = (balance + Deposite)
            print('Forword Balance $ ',forwordbalance)
        else:
            print('None Deposite Mode')
    if Option == 4:
        print('Thanks for visiting us')
        exit()