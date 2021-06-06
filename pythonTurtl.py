print(35)
# input('Press a button\n')
a,b,c=1,2,3
print(c)
list,lis=['Ade',1,'Tobi','Oba',12],[1,2,3,4]
total=(list+lis)
print(total[2:89])
dict={}
dict['name']='Obaloluwa'
dict['age']=17
dict['collges']='UNILORIN'
dict['Friend']=['David','Joel','Silas']
print(dict)
print(dict['Friend'])
print(dict.keys())
print(dict.values())
print(oct(234))
# data=complex(3[,4])
# print(data)
no1=2
no2=2
no3=no1&no2
print(bin(no3))
# no2=input('Press a button\n')
# if no1==9:
#     no1//=5
#     print(no1)
# print(eval(no1+no2))
# no2=int(input('Press a button\n'))
# print(type(no2))
# while type(no2)=='int':
#     print('Less than 99')
#     no2+=1
# else:
    # print('Finish looping')
for x in range(1,12):
    
    for j in range(1,12):
        
        print(x*j,end=" ")
    print("END")

list=iter([1,2,3,4])
print(next(list))


import math
# print(math.ceil(10.000000))
# print(math.exp(100))
# print(math.log10(100))
# print(math.modf(-12.30009)[1])
# print(round(3.987,2))
# print(math.sqrt(3))
# print(pow(3,3))
import random
dat=[1,2,3,4,5,6,7,8,9]
random.shuffle(dat)
# data=random.choice('Hello World')
print(dat)
# print(math.sin(30*math.pi/180))
# print(math.sin(3*math.pi/180))
print(math.sin(math.degrees(30)))
# print(math.degrees(math.asin(.5)))
print(math.asin(1))
print(math.asin(1)*180/math.pi)
# for x in range(0,11,2):
#     print(x)
# while True:
#     try:
#         print(next(list),end=":")
#     except StopIteration:
#         sys.exit()
#     print(x, end=" ")
str = '123lk8'
lis=['oyo','ekiti','ondo','osun','lagos','edo']
print ("str.center(40, 'a') : ", str.center(35, 'a'))
# list.append(list[2])
# list[2]='Ilorin'
# print(list)
# print(max(list))
list=[]
for x in range(5):
    list.append(x)
# print(str.zfill(10))
list+=lis
list.insert(1,'Ogbomoso')
print(list)
list.pop(0)
print(list)

loca=list.index('osun')
print(loca)
print(len(list))

# for x in range(loca,len(list)-1):
#     print(x)
#     list.pop(x)

 
# print(list)
# # list.remove('Ogbomoso')
# print(list)
# print(list.index('oyo'))
# print(max(list))

tuple1=tuple(list)
print(tuple1)

arr={'name':'David','class':'100L','Location':'Eberu'}
# print(arr)
print(arr.keys())
print(type(arr))
print(arr.values())
print(type(6))

arr1=arr.copy()
print(arr1)
myTuple=('age','size','height','height',)
dict1=dict.fromkeys(myTuple,100)
dict1.setdefault('sex','female')
print(dict1)

arrTup=dict.items()
print(arrTup)
print(dict.get('age','op'))

list=[]
obj={'name':'JJ','age':23,'School':'NC'}
print(list(obj.values()))

def myname(SN,FN):
    print(SN+FN)
    return