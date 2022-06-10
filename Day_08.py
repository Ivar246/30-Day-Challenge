def print_rangoli(size):
    # your code goes here
  
    for i in range(size):
        for j in range(i+1, size):
            print('-', end='')
        for j in range(i+1):
            print(chr(97+(size-1)-j), end='-')
        for j in range(i):
            print(chr(97+(size)+(j-i)), end='-')
        print()
    for i in range(size-1):
        for j in range(i+1):
            print(' ', end='')
        for j in range(i, size-1):
            print('*', end='')
        for j in range(i+1, size-1):
            print('*', end='')
        print()
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)