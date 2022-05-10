def f(x, equ_list, deg):
    power = deg
    sum = 0
    for coeff in equ_list:
        sum = sum + (coeff * (x**power))
        power = power - 1
    return sum
def dof(x, equ_list, deg):
    power = deg
    diff = [0]*power
    i = 0
    j = power
    while(i<power):
        new_coeff = equ_list[i] * j
        diff[i] = new_coeff
        j = j - 1
        i = i + 1
    return f(x, diff, (len(diff)-1))

class NewtonRaphson:
    def __init__(self, equ_list) -> None:
        equation = equ_list
        x0 = 0
        x1 = 1
        while((f(x0, equation, deg)*f(x1, equation, deg))>=0):
            # print(f"f({x0}) = {self.f(x0, equation, deg)}")
            # print(f"f({x1}) = {self.f(x1, equation, deg)}")
            x0 +=1
            x1 +=1
        print(f"f({x0}) = {f(x0, equation, deg)}")
        print(f"f({x1}) = {f(x1, equation, deg)}")
        print(f"Root lies between {x0} and {x1}")
        fx = f(x1, equation, deg)
        dfx = dof(x1, equation, deg)
        print(self.newtonRaphsonMethod(x1, fx, dfx))

    def newtonRaphsonMethod(self, x, fx, dfx):
        for i in range(10):
            x = x - (fx/dfx)
            print(f"Iteration {i+1} : {x}, f(x) = {f(x, equ, deg)}")
            fx = f(x, equ, deg)
            dfx = dof(x, equ, deg)
        return x
class BisectionMethod:
    def __init__(self, equ_list) -> None:
        self.equation = equ_list
        x0 = 0
        x1 = 1
        while((f(x0, self.equation, deg)*f(x1, self.equation, deg))>=0):
            x0 +=1
            x1 +=1
        print(f"f({x0}) = {f(x0, self.equation, deg)}")
        print(f"f({x1}) = {f(x1, self.equation, deg)}")
        print(f"Root lies between {x0} and {x1}")
        fx1 = f(x0, self.equation, deg)
        fx2 = f(x1, self.equation, deg)
        print(self.bisectionMethod(fx1, fx2, x0, x1))
    def bisectionMethod(self, fx1, fx2, x0, x1):
        root_list = []
        root_list.append(fx1)
        root_list.append(fx2)
        root = (x0+x1)/2
        for itr in range(25):
            i = len(root_list)
            while(i>0):
                prev_root = root_list[i-1]
                if(f(prev_root, self.equation, deg)*f(root, self.equation, deg))<0:
                    root = (prev_root + root)/2
                    root_list.append(root)
                    break
                i = i - 1
            print(f"Iteration {itr+1} : {root}, f(x) = {f(root, self.equation, deg)}")
        return root

if __name__ == '__main__':
    deg = int(input("Enter degree of equation : "))
    equ = []
    i = deg
    while(i>=0):
        equ.append(int(input(f"coefficient of x^{i} :")))
        i = i - 1
    x = int(input("Enter\n1. Newton Raphson Method\n2. Bisection Method.\n3. Exit\n-->"))
    match x:
        case 1 : obj = NewtonRaphson(equ_list = equ)
        case 2 : obj = BisectionMethod(equ_list = equ)
        case 3 : exit()
        case _ : pass