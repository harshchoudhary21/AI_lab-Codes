import random

def f(x):
    return -1*(x**2)+5*x-6

def hill_climbing():
    lower_limit = -5
    upper_limit = 5
    x = random.uniform(lower_limit,upper_limit)
    step_size = 1
    while True:   
        best_x = None
        best_x_val = float('-inf')
        for  i in [x+step_size,x-step_size]:
            if lower_limit <= i <= upper_limit:
                val = f(i)
                if val > best_x_val:
                    best_x_val = val
                    best_x = i
        if best_x_val <= f(x):
            return x
        x = best_x
    
print(hill_climbing())

        
   
       
       