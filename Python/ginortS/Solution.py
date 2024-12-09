# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
b=[]
s=[]
u=[]
d1=[]
d2=[]
for i in a:
   b.append(i) 
for i in b:
    if i.islower():
        s.append(i)
    if i.isupper():
        u.append(i)
    if i.isdigit() and int(i)%2!=0:
        d1.append(i)
    if i.isdigit() and int(i)%2==0:
        d2.append(i)
s.sort()
u.sort()
d1.sort()
d2.sort()
t=''.join(s+u+d1+d2)
print(t)
