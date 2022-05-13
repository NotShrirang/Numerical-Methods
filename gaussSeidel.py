class GaussSeidel:
    def __init__(self, eq_list) -> None:
        self.equation_list = []
        self.equation_list = eq_list
        i = 0
        for eq in self.equation_list:
            sum = 0
            for item in eq:
                sum = sum + abs(item)
            if( abs(eq[i]) > (sum-abs(eq[i]))):
                print("yes")
            i = i + 1
        # i = 0
        # for eq in self.equation_list:
        #     vars()[f'list{i}'] = []
        #     i = i + 1
        # i = 0
        # for eq in self.equation_list:
        #     i = 0
        #     while(i<(len(eq)-1)):
        #         item = eq[i]
        #         vars()[f'list{i}'].append(item)
        #         i = i + 1
        # i = 0
        # while(i<(len(eq)-1)):
        #     print(vars()[f'list{i}'])
        #     i = i + 1
        # i = 0
        # while(i<(len(eq)-1)):
        #     item = max(vars()[f'list{i}'])
        #     if(item == vars()[f'list{i}'][i]):
        #         print("Yes!")
        #     else:
        #         old_index = vars()[f'list{i}'].index(item)
        #         print(i, old_index)
        #     i = i + 1
        # for eq in self.equation_list:
        #     item = max(eq[1:-1])
        #     eq.remove(item)
        #     self.equation_list[i].insert(i, item)
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
                r = int(input(f"Enter constant term : "))
            else:
                r = int(input(f"Enter coefficient of x{j+1} : "))
            eq.append(r)
            j += 1
        equations_list[i] = eq
        i+=1
    for eq_list in equations_list:
        print(eq_list)
    obj = GaussSeidel(equations_list)