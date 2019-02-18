string = 'AABCAAADA'
k = 3
k = len(string)//k



lt = [string[i:i+len(string)//k] for i in range(0, len(string), len(string)//k)]
for s in lt:
    u = ""
    for i in range(0, len(s)):
        if s[i] not in u:
            u += s[i]
    print(u)
