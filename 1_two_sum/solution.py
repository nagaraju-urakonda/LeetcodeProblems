a = [2,7,45,10]
seen = {}
target = 55

for i, v in enumerate(a):
    need = target - v
    if need in seen:
        print(seen[need], i)
    seen[v] = i
