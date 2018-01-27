fh=open("C:\\myprojects\\python_practice\\rub.txt","r")
text=fh.read()
print(text)
for x in text:
 if x.isupper():
  print("the number is %s" %x )
  print("happy")