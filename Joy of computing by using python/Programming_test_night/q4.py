n=int(input())
a=[]
for i in range(2,n+1):
  count=0
  for j in range(1,i+1):
    if i%j==0:
      count+=1
  if count==2:
    a.append(i)
for k in range(len(a)-1):
  if((a[k+1]-a[k])<3):
    print('(',end='')
    print(a[k],end='')
    print(',',a[k+1],end='')
    print(')')