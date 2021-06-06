# arrA=[]
# arrA.extend(range(1,11))
# print(arrA)
# from itertools import permutations
# print(list(permutations([1,2,3,4])))

allarr=[]
def reverse(string, length, l, r) :
	if (l < 0 or r >= length or l > r) :
		return string
	
	while (l < r) :
		c = string[l]
		string[l] = string[r]
		string[r] = c
    
		l += 1
		r -= 1
    
	return string
def reversort(arr):
    totalcost=0
    allarr=arr
    for i in range(0,len(arr)-1):
        arrs=[]
        usedi=i+1
        for q in range(i,len(arr)):
            
            arrs.append(allarr[q])
            
        minvalue=min(arrs)
        j=arr.index(minvalue)+1
        totalcost+=j-usedi+1   
        allarr=reverse(allarr,len(allarr),i,j-1) 
 
    return totalcost
    
from itertools import permutations
def instances(arr):    
    comb=permutations(arr,len(arr))    
    return list(comb)

cases=int(input(''))
for case in range (0,cases):
    bigArr=[]
    length,cost=(input().split(' '))
    length=int(length)
    cost=int(cost)
    
    for x in range (1,length+1):
        exist=False
        bigArr.append(x)
        resultlist=[]
    if length<10:
        allinstance=instances(bigArr)

        for y in allinstance:
        
             
            costResult=reversort(list(y))
                # resultlist.append(costResult)

                
            if costResult==cost:
                    exist=True
                    text=' '.join(str(x) for x in list(y))
                    print('Case #'+str(case+1) + ': ' +str(text))
                    break
            
    
    if not exist and length<10:
        print('Case #'+str(case+1) + ': IMPOSSIBLE')
    elif length>=10:
        arrs=[]
        arr=[]
        rounds=int(length/10)
        for x in range(1,length+1):
            arr.append(x)
            
            if len(arr)==9:
                arrs.append(arr)
                arr=[]
                print(len(arrs))
            if length-len(arrs)*9 <9:
                print(999999999)
                remain=[]
                remain.extend(range(len(arrs)*9,length))
                arrs.append(remain)
        print(arrs)

        

