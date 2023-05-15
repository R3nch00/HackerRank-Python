a = "abcdefghijklmnopqrstuvwxyz" #String of all alphabets

def print_rangoli(size):
    lines = [] #Empty list to store output
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1): # Lower part
        print(lines[row].center(width, '-'))
        
    for row in range(size): # Upper part
        print(lines[row].center(width, '-'))    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)