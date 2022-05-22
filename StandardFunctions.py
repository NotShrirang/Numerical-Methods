r'''
    Python library for standard functions required for numerical methods.
    - Method f() - returns value of polynomial at given value.
    - Method dof() - returns value of derivative of polynomial at given value.
    - Method value() - returns value of expression at given value of x. 
'''
import lambdaFunction
def f(x: int | float, equ_list: list, deg: int) -> int | float :
    '''
    Function for obtaining value of any polynomial at given value of x.
    
    Args : 
        x : value of x
        equ_list = list of coeffs of x in decreasing order.
        deg : degree of polynomial.
    
    Returns: 
        returns float or int. 
    '''
    power = deg
    sum = 0
    for coeff in equ_list:
        sum = sum + (coeff * (x**power))
        power = power - 1
    return sum
def dof(x: int | float, equ_list: list, deg: int) -> int | float:
    '''
    Function for obtaining value of derivative of any polynomial at given value of x.
    
    Args : 
        x : value of x
        equ_list = list of coeffs of x in decreasing order.
        deg : degree of polynomial.
    
    Returns: 
        returns float or int. 
    '''
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

def value(exp : str, x : int | float) -> int | float:
    '''
    Function for obtaining value of given expression at given value of x.

    Args :
        exp : Expression
        x : value of x
    
    Returns :
        returns float or int.
    '''
    return lambdaFunction.lambdafunction("def f(x):", f"\n\treturn {exp}", caller=f"f({x})")