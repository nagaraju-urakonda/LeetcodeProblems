s = "leetcode"
count = {}
for ch in s:
  count[ch] = count.get(ch,0)+1
for i,k in enumerate(s):
  if count[k] == 1:
    print(1)
print(-1)
