import lambdaFunction
class SimpsonThreeEighth:
    def integrate(self, exp : str, _startIndex, _endIndex) -> float | str:
        self._exp = exp
        self._y = []
        self._startIndex = _startIndex
        self._endIndex = _endIndex

        h = (self._endIndex - self._startIndex)/1000000
        self._y = self.f(self._exp, self._startIndex, self._endIndex, h)
        i = 1
        y3 = []
        yelse = []
        while(i<(len(self._y)-1)):
            if(i%3==0):
                y3.append(self._y[i])
            else:
                yelse.append(self._y[i])
            i = i + 1
        try:
            integral = ((3*h)/8)*((self._y[0] + self._y[-1]) + 2*(sum(y3)) + 3*(sum(yelse)))
            integral = round(integral, 8)
            return integral
        except:
            return "Math Error"
    def f(self, exp : str, a, b, h) -> list:
        return(lambdaFunction.lambdafunction("from math import *","\ndef f():", f"\n\tx = {a}", f"\n\th = {h}", "\n\tl = []\n\tl2 = []", f"\n\twhile(x<={b}):", "\n\t\tl.append(x)", "\n\t\tx = x + h", "\n\tfor x in l:", f"\n\t\ty = {exp}", "\n\t\tl2.append(y)", "\n\treturn l2", caller=f"f()"))

if __name__ == '__main__':
    obj = SimpsonThreeEighth()
    exp = input("Enter equation : ")
    a = float(input("from : "))
    b = float(input("To : "))
    print(obj.integrate(exp, a, b))