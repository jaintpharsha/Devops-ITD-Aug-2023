def sorts(num):
    for in1, i in enumerate(num):
        for in2, j in enumerate(num[:-1]):
            if i < j:
                num[in1],num[in2]=num[in2],num[in1]
    return num


def sorts2(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[i] < num[j]:
                num[i],num[j]=num[j],num[i]
    return num


num = [2,11,10,4,61,7]
print(num)

print(sorts2(num))
    
                