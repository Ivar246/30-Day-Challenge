string = input()

string_method = ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']

for meth in string_method:
    for char in string:
        if (f"{char}.{meth}"):
            print(True)
            break
        else:
            print(False)