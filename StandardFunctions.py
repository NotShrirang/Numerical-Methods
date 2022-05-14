r'''
    Python library for standard functions required for numerical methods.
    - Method f()   - returns value of polynomial at given value.
    - Mothod dof() - returns value of derivative of polynomial at given value.
'''
def f(x: int | float, equ_list: list, deg: int) -> int | float :
    '''
    Function for obtaining value of any polynomial at given value of x.
    
    Args : 
        x : value of x
        equ_list = list of coeffs of x in decreasing order.
        deg : degree of polynomial.
    
    Returns: 
        Returns float or int. 
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
        Returns float or int. 
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
