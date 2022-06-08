'''
Task :
   You are given a string .
    Your task is to find out if the string contains: alphanumeric characters,
    alphabetical characters, digits, lowercase and uppercase characters. 
'''


def is_alpha(str):
    for char in str:
        if char.isalpha():
            return True
    return False

    
def is_digits(str):
    for char in str: 
        if char.isdigit():
            return True
    return False

    
def is_alphanum(str):
    for char in str:
        if char.isalnum():
            return True
    return False

    
def is_lower(str):
    for char in str:
        if char.islower():
            return True
    return False

    
def is_upper(str):
    for char in str:
        if char.isupper():
            return True
    return False


s = input()

alphanum = is_alphanum(s)
alpha = is_alpha(s)
digit = is_digits(s)
lower = is_lower(s)
upper = is_upper(s)


for i in [alphanum, alpha, digit, lower, upper]:
    print(i)