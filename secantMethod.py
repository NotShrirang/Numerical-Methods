import lambdaFunction
class SecantMethod:
    def secantMethod(self, exp) -> int | float:
        x0, x1, fx0, fx1 = lambdaFunction.lambdafunction("from math import *", f"\ndef f(x):\n\ty = {exp}\n\treturn y", f"\ndef m():\n\tx0 = 0\n\tx1 = 1\n\twhile(1):\n\t\ty0 = f(x0)\n\t\ty1 = f(x1)\n\t\tif((y0*y1)<=0):\n\t\t\tbreak\n\t\telse:\n\t\t\tprint(x0, x1)\n\t\tx0 = x0 + 1\n\t\tx1 = x1 + 1\n\tfx0 = f(x0)\n\tfx1 = f(x1)\n\treturn x0, x1, fx0, fx1", caller=f"m()")
        print(x0, x1, fx0, fx1)
        root_list = []
        root_list.append((x0, fx0))
        root_list.append((x1, fx1))
        root = x1 - (((x1-x0)/(fx1 - fx0))*fx1)
        for itr in range(25):
            i = len(root_list)
            while(i>0):
                prev_root = root_list[i-1][0]
                value_prev_root = root_list[i-1][1]
                value_root = lambdaFunction.lambdafunction("from math import *", f"\ndef f(x):\n\ty = {exp}\n\tprint(y)\n\treturn y", caller=f"f({root})")
                if((value_prev_root * root) < 0):
                    root = root - (((root-prev_root)/(value_root - value_prev_root))*value_root)
                    root_list.append((root, value_root))
                    break
                i = i - 1
        return root
if __name__ == '__main__':
    exp = input("Enter equation : ")
    obj = SecantMethod()
    obj.secantMethod(exp)