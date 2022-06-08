#split and join

def split_and_join(line):
    # write your code here
    splitted_string = line.split(' ')
    joined_string = '-'.join(splitted_string)
    
    return joined_string

    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)