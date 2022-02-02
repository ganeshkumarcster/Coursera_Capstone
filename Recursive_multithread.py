import datetime as dt

def date_dif(dat,vnam):
    td=dt.datetime.now()
    #Vc_dt=dt.datetime.strptime(dat,'%d%m%y')
    Vc_dt = dat

    if (int(Vc_dt.strftime('%y')) < 20):
        print('Entered Year is :',Vc_dt.strftime('%y'))
        return 0
#diff=td - Vc_dt
    print("Date entered :", Vc_dt, "curr dt:", td)
    if td < Vc_dt:
        return 0

#return next due 
    if vnam == 1:
        nxt_dt=Vc_dt+dt.timedelta(days=84)
    else:
        nxt_dt = Vc_dt + dt.timedelta(days=21)
    print('Your 2nd dose date is :', nxt_dt)
    if nxt_dt > td:
        print('Your due is :', nxt_dt)
    elif (nxt_dt < td):
        print('You run out of overdue and make it next due asap!...')

    return nxt_dt

def inp_fun():
    Name=input('Enter your Name:')
    age=int(input('Enter your Age in numbers:'))
    if ( age<=0 ):
        print('Invalid input! Enter the details again: ')

    return age

def valdation(age):

    if (age >= 18):
        dos1=input('Have you taken 1st dose').lower()
        if (dos1 == 'yes' or dos1 == 'no'):
            pass
        else:
            print('Invalid input')
            valdation(age)

        if (dos1 == 'yes'):
            Vcname = int(input('Enter 1-covishield , 2-covaxin :'))

            if (Vcname < 0 or Vcname > 2):
                print(" Invalid input! ")
                valdation(age)
            try:
                date1 = dt.datetime.strptime(input('Enter date of dose1 in ddmmyy:'),'%d%m%y')
            except ValueError:
                print('Try again')
                valdation(age)

            nxt_dt=date_dif(date1,Vcname)
            if (nxt_dt == 0):
                print("Entered date/Year is invalid ")
                valdation(age)
        elif (dos1 == 'no'):
            print('Kindly register with details and wait for your turn')

    elif (age >= 0 and age < 18):
            print('Drive for below 18 year old will held later')
    exit()

##### main Function starts here  ####
def mainclass():
    i=inp_fun()
    if i > 0:
        valdation(i)
    else:
        mainclass()

mainclass()





            










