n=int(input("length\n"))
x=[]
for i in range(n):
    print('element ',i)
    x.append(int(input()))
max_numb=max(x)
min_numb=min(x)
for i in range(len(x)):
    if x[i]==max_numb: x[i]=min_numb
    elif x[i]==min_numb: x[i]=max_numb
print('new array: ',x)
