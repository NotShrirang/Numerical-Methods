import lambdaFunction
class SimpsonOneThird:
    def integrate(self, exp : str, startIndex, endIndex) -> float | str:
        self.__exp = exp
        self.__y = []
        self.__startIndex = startIndex
        self.__endIndex = endIndex
        
        h = (self.__endIndex - self.__startIndex)/1000000
        self.__y = self.f(self.__exp, self.__startIndex, self.__endIndex, h)
        i = 1
        yodd = []
        yeven = []
        while(i<len(self.__y)):
            if(i == (len(self.__y)-1)):
                break
            if(i%2==1):
                yodd.append(self.__y[i])
            elif(i%2==0):
                yeven.append(self.__y[i])
            i = i + 1
        try:
            integral = (h/3)*((self.__y[0] + self.__y[-1]) + 4*(sum(yodd)) + 2*(sum(yeven)))
            integral = round(integral, 8)
            return integral
        except:
            return "Math Error"
    def f(self, exp : str, a, b, h) -> list:
        return(lambdaFunction.lambdafunction("from math import *","\ndef f():", f"\n\tx = {a}", f"\n\th = {h}", "\n\tl = []\n\tl2 = []", f"\n\twhile(x<={b}):", "\n\t\tl.append(x)", "\n\t\tx = x + h", "\n\tfor x in l:", f"\n\t\ty = {exp}", "\n\t\tl2.append(y)", "\n\treturn l2", caller=f"f()"))

if __name__ == '__main__':
    obj = SimpsonOneThird()
    exp = input("Enter equation : ")
    a = float(input("from : "))
    b = float(input("To : "))
    print(obj.integrate(exp, a, b))