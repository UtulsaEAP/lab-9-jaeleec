def fibonacci(n):
    if n <=1:
       return n
    else: 
        return (fibonacci(n-1) + fibonacci(n-2))

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')