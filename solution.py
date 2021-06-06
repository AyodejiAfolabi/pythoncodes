# arr=[1,2]

# for x in arr:
#     a=len(arr)
#     p=arr[a-1]
#     q=arr[a-2]
           
#     print(arr)
#     if p+q<100:
        
#         arr.append(p+q)
# # LOOP ENDS HERE
# sum=0           
# print(arr)
# for x in arr:
#     if x%2==0:
#         sum+=x
# print(arr)
# print(sum)
arrs=[1,2,3]
# print(arrs(4))
arr=[]
arrs=[]
for x in range(2,600851475143):
    if 600851475143%x==0:
        arr.append(x)

for x in arr:
        
    for y in range(2,x):
        factor=0
        
        if x%y==0:
            
            factor+=1
            if factor>0:
                
                try:
                    arrs.index(x)
                except ValueError:

                    arrs.append(x)            
primeNo=[]

for x in arr:
    for y in arrs:
        if x!=y:
            primeNo=x
            # try:
            #     # arr.index(x)
            #     primeNo.index(x)
            # except ValueError:
            #     primeNo.append(x)
    # if primeNo.count(x)==1:
    #     primeNo.remove(x)
print(primeNo)