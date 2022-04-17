n = input()
n = list(n)
n = sorted(n)
for i in range(len(n)):
  for j in range(len(n)):
    for k in range(len(n)):
      print(n[i],end='')
      print(n[j],end='')
      print(n[k],end='')
      print()