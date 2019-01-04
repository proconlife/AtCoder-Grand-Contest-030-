a,b,c=map(int,input().split())
 
d=b+c
if a+b<c: d-=(c-(a+b)-1)
print(d)
