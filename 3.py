##n=bin(int(input()))
##print(n)
##a=[]
##c=1
##for i in range(1,len(n)):
##    if(n[i-1]==n[i]):
##        c+=1
##        a.append(c)
##    else:
##        c=1
##print(max(a))        


a=bin(int(input()))
b=1
c=0
for i in range(len(a)-3):
    if a[i+2]==a[i+3]:
        b+=1
    else:
        c=max(c,b)
        b=1
        continue
print(c)    
