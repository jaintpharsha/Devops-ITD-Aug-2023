def char_count(string):
    freq = {}
    for char in set(string):
        freq[char] = string.count(char)
    return freq

s = "HelloWorldHello"
print(char_count(s))
