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
for x in range(2,20):
    # i.e 2 to 19
    # From 2 to  Since 1 is not a prime Number
    arrs.append(x)
    # appending all possible intergers 2 to 19 into the array
    a=0
    for y in range(2,x):
        # it wont check for 2. becos it's range(2,2). There is no number between 2 nd 2
        factor=0
        
        if x%y==0:
            # Reminder of a factor is always 0
            factor+=1
            if factor>0:
                # The 2 factors of a Prime is 1 nd Itself.But the two factor are not used in the code
                
                try:
                    arr.index(x)
                except ValueError:

                    arr.append(x)      
                    #appending non Primes          
print(arr)
primeNo=[]

for x in arrs:
    for y in arr:
        # Removing Non Primes from the bigger array to leave Primes only
        if x!=y:
            try:
                arr.index(x)
                primeNo.index(x)
            except ValueError:
                primeNo.append(x)
    if primeNo.count(x)==1:
        primeNo.remove(x)
        print(primeNo)
print(max(primeNo))
