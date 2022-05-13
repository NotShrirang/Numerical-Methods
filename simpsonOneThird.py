import lambdaFunction
class SimpsonOneThird:
    def integrate(self, exp : str, _startIndex, _endIndex):
        self.exp = exp
        self.y = []
        self._startIndex = _startIndex
        self._endIndex = _endIndex

        h = (self._endIndex - self._startIndex)/1000000
        self.y = self.f(exp, self._startIndex, self._endIndex, h)
        i = 1
        yodd = []
        yeven = []
        while(i<len(self.y)):
            if(i == (len(self.y)-1)):
                break
            if(i%2==1):
                yodd.append(self.y[i])
            elif(i%2==0):
                yeven.append(self.y[i])
            i = i + 1
        try:
            integral = (h/3)*((self.y[0] + self.y[-1]) + 4*(sum(yodd)) + 2*(sum(yeven)))
            integral = round(integral, 8)
            return integral
        except:
            return "Math Error"
    def f(self, exp : str, a, b, h):
        return(lambdaFunction.lambdafunction("from math import *","\ndef f():", f"\n\tx = {a}", f"\n\th = {h}", "\n\tl = []\n\tl2 = []", f"\n\twhile(x<={b}):", "\n\t\tl.append(x)", "\n\t\tx = x + h", "\n\tfor x in l:", f"\n\t\ty = {exp}", "\n\t\tl2.append(y)", "\n\treturn l2", caller=f"f()"))

if __name__ == '__main__':
    obj = SimpsonOneThird()
    exp = input("Enter equation : ")
    a = float(input("from : "))
    b = float(input("To : "))
    print(obj.integrate(exp, a, b))