a=eval(input())
b=min(a)
c=[b]
d=b[-1]
for i in a:
    for j in a:
        if (d==j[0] and c[0][0]!=j[-1]):
            c.append(j)
            d=j[-1]
            a.remove(j)
            break
b.append(i)
print(c)