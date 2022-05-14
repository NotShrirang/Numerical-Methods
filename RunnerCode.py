from newtonRaphson import NewtonRaphson
from bisection import BisectionMethod
deg = int(input("Enter degree of equation : "))
equ = []
i = deg
while(i>=0):
    equ.append(int(input(f"coefficient of x^{i} :")))
    i = i - 1
while(True):
    try:
        x = int(input("Enter\n1. Newton Raphson Method\n2. Bisection Method.\n3. Exit\n-->"))
    except:
        print("Enter choice again!")
        continue
    match x:
        case 1 : 
            obj = NewtonRaphson(equ_list = equ)
            print(obj.newtonRaphsonMethod()) 
        case 2 : 
            obj = BisectionMethod(equ_list = equ)
            print(obj.bisectionMethod())
        case 3 : exit()
        case _ : pass