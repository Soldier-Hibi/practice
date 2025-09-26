n = int(input())
fib_list = [] 
a = 0
b = 1

for _ in range(n): 
    fib_list.append(a)
    fib = a + b
    a = b
    b = fib
print(fib_list)