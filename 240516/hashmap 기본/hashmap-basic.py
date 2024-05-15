n = int(input())
d = dict()
for _ in range(n):
    com = input()
    if com.startswith("add"):
        _, k, v = com.split()
        k, v = int(k), int(v)
        d[k] = v
    elif com.startswith("remove"):
        k = int(com.split()[1])
        d.pop(k)    
    else:
        k = int(com.split()[1])
        if k not in d:
            print("None")
        else:
            print(d[k])