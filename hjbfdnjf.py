# dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
# print ("Values : ", list(dict.values()))
obj={'name':'JJ','age':23,'School':'NC'}
print(list(obj.values()))

import datetime
import time


k=(2020,9,22,12,35,00,00,00,00)
loct=time.mktime(k)
# print('Today is',loct[2],'/',loct[1],'/',loct[0])
import calendar

print(calendar.month(2020,5))


def call():
    print(8888)
    data=datetime.datetime.now()
    print(data.strftime('Today is %A'))
    
call()
ticks=time.time()
print(time.localtime(loct))
# print(ticks)
t = (2015, 12, 31, 10, 39, 45, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.localtime(t)))

def callMe(str,*ty):
    print('Outputs are:')
    for x in ty:
        print(x)
    # params=999
    

    return
    
    

callMe(8,23,34,33,3)

sum=lambda a,b: a+b
print(sum(10,10))


# foobj=open('foo.txt','w')
# foobj.write('1111111111111111\nyyyyyyyyyyyyyyyyyyyyy\nxxxxxxxxxxxxxxxx')
# foobj.close()
# foobj=open('foo.txt','r')
# letter=foobj.readline(1)
# print(letter+'88')
import os
# os.chdir('')
fdata=os.getcwd()
print(fdata)
# os.mkdir('lll.html')
# os.remove('yyy.js')

# fo = open("food.html", "wb")
# print ("Name of the file: ", fo.name)
# fid = fo.fileno()
# print ("File Descriptor: ", fid)
# # Close opend file
# fo.close()
# print(os.getcwd())
# newObj=open('ProLang.txt','w+')
# # newObj.write('1111111111111111111111111111111\n')
# newObj.write('C#\nPython\nC++\nJava\nSwift')
# print(newObj.name)
# newObj=open('proLang.txt','r')
# # newObj.close()
# print(newObj.readline())
# for x in range(100):
#     data=next(newObj,'')
#     print('%s'%(data))
ret=os.access('foo.txt',os.F_OK)
print(ret)
fet=os.access('lang.html',os.F_OK)
print(fet)

def celciusToKelvin(conv):
    assert(conv>0),"noooooooo"
    return 273+conv

print(celciusToKelvin(-8))













# import sys
# print(sys.path)
# import pythonTurtl 
# pythonTurtl.myname('JJ','AFO')

# arr=[]
# for x in range(1,300):


#     arr.append(x)
    
# arrs=[]
# for x in arr:
#     if x%2==0 or x%3==0:
#         arrs.append(x)
# print('2 nd 3',len(arrs))

# arrs=[]
# for x in arr:
#     if x%2==0 or x%5==0:
#         arrs.append(x)
# print('2 nd 5',len(arrs))


# arrs=[]
# for x in arr:
#     if x%3==0 or x%5==0:
#         arrs.append(x)
# print('3 nd 5',len(arrs))



# arr=[]
# for x in range(1,300):
#     arr.append(x)

# arrs=[]
# for x in arr:
#     if x%2==0 or x%3==0 or x%5==0:
#         arrs.append(x)
# print('all',len(arrs))

# arrs=[]
# for x in arr:
      #     if x%5==0:
#         arrs.append(x)

# print('2 only',len(arrs))
