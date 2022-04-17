st = input()
nst = ""
for i in st:
  if(ord(i) >=65 and ord(i) <=90):
    if(ord(i)+3>90):
      nst += chr(ord(i)+3-26)
    else:
      nst += chr(ord(i)+3)
  elif(ord(i) >=97 and ord(i) <=122):
    if(ord(i)-9<97):
      nst += chr(ord(i)-9+26)
    else:
      nst += chr(ord(i)-9)
  elif(ord(i) >=48 and ord(i) <=57):
    if(ord(i)-5<48):
      nst += chr(ord(i)-5+10)
    else:
      nst += chr(ord(i)-5)
  elif(ord(i) == 32):
    nst += chr(ord(i)+1)
  else:
    nst+=i
print(nst,end="")