def fibonacci(n):
    i = 1
    while i < n: 
        i = i + i+1
    n = i
    return(n)

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')