'''n=10
fact=1
i=1
while i<=n:
    fact=fact*i
    
    i+=1
    print(fact)'''
#armstrong
'''n=6275
p= len(str(n))
n1=n
arm=0
while n!=0:
    arm=arm+(n%10)**p
    n=n//10
if n1==arm:
    print(n1,"is an armstrong number")
else:
    print(n1,"is not armstrong number")'''
#for
n=1533
n1=n
p=len(str(n))
arm=0
for i in range(0,p,1):
    arm=arm+(n%10)**p
    n=n//10
if n1==arm:
    print(n1,"is an armstrong number")
else:
    print(n1,"is not armstrong number")    
    
    
