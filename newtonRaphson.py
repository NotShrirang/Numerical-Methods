from StandardFunctions import f, dof
class NewtonRaphson:
    def __init__(self, equ_list) -> None:
        self.__equation = equ_list
        x0 = 0
        x1 = 1
        self.__deg = len(equ_list) - 1
        while((f(x0, self.__equation, self.__deg)*f(x1, self.__equation, self.__deg))>=0):
            x0 +=1
            x1 +=1
        self.__fx = f(x1, self.__equation, self.__deg)
        self.__dfx = dof(x1, self.__equation, self.__deg)
        self.__x1 = x1

    def newtonRaphsonMethod(self):
        x = self.__x1
        fx = self.__fx
        dfx = self.__dfx
        for i in range(10):
            x = x - (fx/dfx)
            fx = f(x, self.__equation, self.__deg)
            dfx = dof(x, self.__equation, self.__deg)
        return x
