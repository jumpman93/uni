def compute_harmonic_series(n):
    i = 1
    equal = 0.0
    for i in range(1, n+1):
        equal = equal + 1/i
    print (equal)


def get_fibonacci_sequence(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a)

        temp = a
        a = b
        b = temp + b
    return a

def print_pattern(hgt, wdt, str1: str, str2: str):

    string = ''
    
    for hor in range(wdt):
        hor_string = str1 + str2
        print(hor_string, end='')
    
    for ver in range(hgt):
            ver_string = str1 + str2
            print(ver_string)

    
       
print_pattern(4,3,'!@','$$$')
