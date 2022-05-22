import StandardFunctions
class NewtonRaphson:
    '''
    Class for Newton - Raphson Method.

    Args : 
        class constructor takes arguments.
        equ_list : list of coeffs of x terms in polynomial.

    Syntax :
        obj = NewtonsRaphson(equ_list = mylist)
    '''
    def __init__(self, equ_list) -> None:
        self.__equation = equ_list
        x0 = 0
        x1 = 1
        self.__deg = len(equ_list) - 1
        while((StandardFunctions.f(x0, self.__equation, self.__deg)*StandardFunctions.f(x1, self.__equation, self.__deg))>=0):
            x0 +=1
            x1 +=1
        self.__fx = StandardFunctions.f(x1, self.__equation, self.__deg)
        self.__dfx = StandardFunctions.dof(x1, self.__equation, self.__deg)
        self.__x1 = x1

    def newtonRaphsonMethod(self) -> int | float:
        '''
        Method for obtaining one root of given polynomial.

        Args : 
            none
        
        Returns : 
            returns root as int or float.
        '''
        x = self.__x1
        fx = self.__fx
        dfx = self.__dfx
        for i in range(10):
            x = x - (fx/dfx)
            fx = StandardFunctions.f(x, self.__equation, self.__deg)
            dfx = StandardFunctions.dof(x, self.__equation, self.__deg)
        return x
