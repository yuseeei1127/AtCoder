nx = map(int, raw_input().split())
l = map(int, raw_input().split())
 
n = nx[0]
x = nx[1]
 
d = 0
i = 1
 
while True:
    if d <= x:
        d += l[i-1]
        i += 1
    if d > x:
        print(i-1)
        break
    if i == n + 1:
      print(i)
      break
  