def number_pattern(n):
    if not isinstance(n, int):
        return print("Argument must be an integer.")
    elif n<= 0:
        return print("Argument must be a positive integer.")
    
    for i in range(1, n+1):
        print(str(i), end= " ")
    
number_pattern(64)