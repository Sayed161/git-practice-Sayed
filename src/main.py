from datetime import date
print("Name : Sheikh Sayed")
print(date.today())

def calculator(a,b):
    if(a>b):
        add(a,b)
    if(b>a):
        subtract(a,b)
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(b-a)

def multiply(a,b):
    print(a*b)