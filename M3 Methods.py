from StandardFunctions import f, dof
class NewtonRaphson:
    def __init__(self, equ_list) -> None:
        self.equation = equ_list
        x0 = 0
        x1 = 1
        self.deg = len(equ_list) - 1
        while((f(x0, self.equation, self.deg)*f(x1, self.equation, self.deg))>=0):
            # print(f"f({x0}) = {self.f(x0, equation, deg)}")
            # print(f"f({x1}) = {self.f(x1, equation, deg)}")
            x0 +=1
            x1 +=1
        # print(f"f({x0}) = {f(x0, self.equation, deg)}")
        # print(f"f({x1}) = {f(x1, self.equation, deg)}")
        # print(f"Root lies between {x0} and {x1}")
        self.fx = f(x1, self.equation, self.deg)
        self.dfx = dof(x1, self.equation, self.deg)
        self.x1 = x1
        # print(self.newtonRaphsonMethod())

    def newtonRaphsonMethod(self):
        x = self.x1
        fx = self.fx
        dfx = self.dfx
        for i in range(10):
            x = x - (fx/dfx)
            # print(f"Iteration {i+1} : {x}, f(x) = {f(x, equ, deg)}")
            fx = f(x, self.equation, self.deg)
            dfx = dof(x, self.equation, self.deg)
        return x
class BisectionMethod:
    def __init__(self, equ_list) -> None:
        self.equation = equ_list
        x0 = 0
        x1 = 1
        self.deg = len(equ_list) - 1
        while((f(x0, self.equation, self.deg)*f(x1, self.equation, self.deg))>=0):
            x0 +=1
            x1 +=1
        # print(f"f({x0}) = {f(x0, self.equation, deg)}")
        # print(f"f({x1}) = {f(x1, self.equation, deg)}")
        # print(f"Root lies between {x0} and {x1}")
        self.fx1 = f(x0, self.equation, self.deg)
        self.fx2 = f(x1, self.equation, self.deg)
        self.x0 = x0
        self.x1 = x1
        # print(self.bisectionMethod())
        # return self.bisectionMethod()

    def bisectionMethod(self):
        fx1 = self.fx1
        fx2 = self.fx2
        x0 = self.x0
        x1 = self.x1
        root_list = []
        root_list.append(fx1)
        root_list.append(fx2)
        root = (x0+x1)/2
        for itr in range(25):
            i = len(root_list)
            while(i>0):
                prev_root = root_list[i-1]
                if(f(prev_root, self.equation, self.deg)*f(root, self.equation, self.deg))<0:
                    root = (prev_root + root)/2
                    root_list.append(root)
                    break
                i = i - 1
            # print(f"Iteration {itr+1} : {root}, f(x) = {f(root, self.equation, deg)}")
        return root

if __name__ == '__main__':
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