#factorial question

def factorial(a):
    import math
    if a>1:
        c=math.factorial(a)
        print(a,'! is equal to',c)
    elif a==0 or a==1:
        print("factorial is 1")
    else:
        print("factorial doesn't exists for negative numbers")
        

