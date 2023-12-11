
def frequency(word):
    lst = word.split()
    result = {}
    for word in lst:
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result


txt = "Fear leads to anger anger leads to hatred hatred leads to conflict conflict leads to suffering"
print(frequency(txt))