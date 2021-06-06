


arr=[]
number=1
attendance=0
while number>0:
    attendance=attendance+1
    name=input('Pls type your name here: ').capitalize()
    if name=='End':
        number=0
    
    else:
        arr.append(name)
        
arrs=[]
b=len(arr)
print('Some of you friends are here also: ')
arr.sort()
for x in arr:
    print(x)

for x in range(b):
    b-=1
    arrs.append(arr[b])

print(arrs)
# arrs=['a','c','b','d']
# arrs.sort()
# print(arrs)
# print(arr.index('Ade'))


