def f(x, equ_list, deg):
    power = deg
    sum = 0
    for coeff in equ_list:
        sum = sum + (coeff * (x**power))
        power = power - 1
    return sum
def dof(x, equ_list, deg):
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
