'''
python decorators
'''
def start_end_decorator(func):
    
    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('End')
        
    return wrapper

@start_end_decorator
def add5(x):
    return x+5
    
# print_name = start_end_decorator(print_name)
add5(10)