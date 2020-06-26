from datetime import datetime
def my_progm():
    print('Please enter your date of birth in yyyy/mm/dd format')
    #a=input()
    #b=datetime.date()
    #print(dir(datetime))
    #print(help(datetime.date))
    b=input()
    c=datetime.strptime(b,'%d/%m/%y')
    print(c)
    d=datetime.today()
    print(d)
    e=d-c
    print(e)
    f=datetime.strftime(e,'%d')
    print(f)
    #print(dir(date))
   #print(date.today())
    #print((datetime.date(2020-12-12))
    #print(type(b))

if __name__=='__main__':
    my_progm()

    
