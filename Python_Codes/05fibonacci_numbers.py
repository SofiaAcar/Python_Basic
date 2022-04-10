# Fibonacci Numbers
fibo_list = [0, 1]

while 55 not in fibo_list :
    fibo = fibo_list[-1] + fibo_list[-2]
    fibo_list.append(fibo)
    
print(fibo_list)