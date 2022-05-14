import StandardFunctions
class BisectionMethod:
    '''
    Class for bisection Method.

    Args : 
        class constructor takes arguments.
        equ_list : list of coeffs of x terms in polynomial.

    Syntax :
        obj = BisectionMethod(equ_list = mylist)
    '''
    def __init__(self, equ_list) -> None:
        self.__equation = equ_list
        x0 = 0
        x1 = 1
        self.deg = len(equ_list) - 1
        while((StandardFunctions.f(x0, self.__equation, self.deg)*StandardFunctions.f(x1, self.__equation, self.deg))>=0):
            x0 +=1
            x1 +=1
        self.__fx1 = StandardFunctions.f(x0, self.__equation, self.deg)
        self.__fx2 = StandardFunctions.f(x1, self.__equation, self.deg)
        self.__x0 = x0
        self.__x1 = x1

    def bisectionMethod(self) -> int | float:
        '''
        Method for obtaining one root of given polynomial.

        Args : 
            none
        
        Returns : 
            returns root as int or float.
        '''
        fx1 = self.__fx1
        fx2 = self.__fx2
        x0 = self.__x0
        x1 = self.__x1
        root_list = []
        root_list.append(fx1)
        root_list.append(fx2)
        root = (x0+x1)/2
        for itr in range(25):
            i = len(root_list)
            while(i>0):
                prev_root = root_list[i-1]
                if(StandardFunctions.f(prev_root, self.__equation, self.deg)*StandardFunctions.f(root, self.__equation, self.deg))<0:
                    root = (prev_root + root)/2
                    root_list.append(root)
                    break
                i = i - 1
        return root