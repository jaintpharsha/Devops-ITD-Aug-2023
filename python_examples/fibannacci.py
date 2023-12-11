# -*- coding: utf-8 -*-

def fibonacci(num):
    rtn = [0,1]
    for i in range(num):
        rtn.append(sum(rtn[-2:]))
    return rtn



def fibonacci2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        for i in range(2,n):
            print(i-1,i-2)
            return fibonacci2(i-1) + fibonacci2(i-2)

print(fibonacci2(10))