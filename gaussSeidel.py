class GaussSeidel:
    def __init__(self) -> None:
        pass
    def gaussSeidel():
        pass

if __name__ == '__main__':
    while(True):
        try:
            x = int(input("Enter no of equation : "))
        except:
            print("Enter valid choice!")
            continue
        equations_list = [[None]]*x
        break
    i = 0
    eq_form = ""
    for itr in range(x):
        if(itr == x - 1):
            eq_form = eq_form + f"a{itr+1}x{itr+1} = c"
            break 
        else:
            eq_form = eq_form + f"a{itr+1}x{itr+1} + "
    print("Equation type : ", eq_form)
    while i<x:
        j = 0
        eq = []
        print(f"\nEquation {i+1} : ")
        while j<=x:
            if(j == x):
                r = input(f"Enter constant term : ")
            else:
                r = input(f"Enter coefficient of x{j+1} : ")
            eq.append(r)
            j += 1
        equations_list[i] = eq
        i+=1
    print(equations_list)