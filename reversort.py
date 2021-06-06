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
def defarr():
    return allarr

cases=int(input(''))
for x in range (0,cases):
    totalcost=0
    arrayLength=int(input(''))
    arr=list(map (int,input().split(' ')))
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
 
    print('Case #'+str(x+1) + ': ' +str(totalcost))
        

