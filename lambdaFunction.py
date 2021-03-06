'''
Library for writing lambda functions of multiple lines.
- Method lambdafunction() - returns list or string. 
'''
import os
def lambdafunction(*args: str, caller: str): 
    '''
    Function to write lambda function with multiple lines. 

    Args : 
        *args (str)  : Lines of code. One line per argument.
        caller (str) : Function name to be executed.
    
    Returns : 
        Returns whatever return type mentioned in *args.
    
    Syntax :
        lambdafunction("arg1", "arg2", ..., caller='caller function')

    '''
    with open('lambdaInternal.py', 'w') as f:
        for line in args:
            f.write(line)
        f.write("\n\ndef main():\n")
        f.write(f"\treturn {caller}")
    
    try:
        import lambdaInternal  
        ret = lambdaInternal.main()
        os.remove('lambdaInternal.py')
        return ret
    except:
        os.remove('lambdaInternal.py')
        return "An error occured! Check your code..."