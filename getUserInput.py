# salary=input("please input your salary")
# bonus=input('please input your bonus')
# payCheck=float(salary)+float(bonus)
# print(payCheck*5)

    
# print('{0:d}+{1:d}'.format(salary,bonus))

# Trying to get and display todays dates
# import datetime
# currentTime=datetime.date.today()
# print(currentTime.strftime('%d,%b,%Y'))


if 5>2:
    #do Not put space between your 5 and 2;
  print("Five is greater than two!")
  
  #you can know the type of data you are working with
# number=34
# print(number)
# compl=-2+5j
# newcompl=4j
# print(compl*newcompl)
#string operations in Python

# word="Mkhitaryan Roma"
# print(word[9:12])
# print(word.strip())
# print(word.__len__())
# print(len(word))

# If statement with OR and 'AND'
# if 3<5 and 2==8:
#   print('Yes')

  if 3<5 or 2==8:
    print('YEP')
# print(word.split('a '))

#  PYTHON OPERATORS

data=18
data=data|6
# print(data/3)
print(data)


# and, or, is, not, is not. STATEMENT is PYTHON

a=6
b=6
print(a is not b)

#Arrays are of 4 types in Python
# 1. List
# A List is a type of array that is ordered and changeable
# e.g
thislist=list(('Mango','PawPaw','Oranges','Tangerine','Cashew','Coconut'))
# print(len(thislist))
# myList=['Apple','dinosaur','Cyrup','Ball']

# thislist.append('Tangerine')
# print(thislist)
# x=(thislist.count('Tangerine'))
# print(x)
# def myFunc(e):
# return len(e)
# myList.sort(reverse=False)
# print(myList)

# Dictionaries

diction={

}

diction['eyes']=2
diction['nose']=2
diction['sex']='Male'
diction['hair']='infinity'
del diction['hair']
print(diction)

# TUPLE TYPE OF ARRAY (UNCHANGEABLE)
thistuple=tuple(("Banana","orange","cocnjut","lemon","lime"))
print(thistuple[1])
print(thistuple)

#SET TYPE OF ARRAY (UNORDERED UNINDEXED)
thisset=set(("OYO","Ibadan","kogi","lokoja","Kwara"))
thisset.add('Borno')
thisset.remove('OYO')
print(thisset)
print(len(thisset))



# DICTIONARY TYPE OF ARRAY INDEXED UNORDERED CHANGEABLE

dicti={
  "banana":"yellow",
  "egg":"Brown"
}
dicti['name']="Fruit"
print(dicti)


#PYthon Conditions
a=44
b=54
if a>b :
  print('a is greater than b')
elif a==b:
    print('a is equal to b')
else:
  print('b is greater than a')


  # print(i)
# a=10
 
# while a<20:
#   if a==15:
#     break
#   a+=1
#   print(a)
# nam=input('Please input your name ')
# age=input('pleae type you age ')
# town=input('where are you from ')



# myDiction={'name':nam,
# 'age':age,
# "city":town
#   }
# print(myDiction)


# if name=='Giroud':
#   print('Benz is better than  you')


# FOr Loop in PYthon
array=['david','oba','buzzy','tchilas','tobi']
for x in array:
  if x=='buzzy':
    print('Its your birthday dude')
    break
  print(x)


for x in range(0,10,2):
  print(x)


# for x in array:
  
#  if x=='buzzy':
#   break
#   print('Its your birthday dude')
#   print(x)
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(5)
def func(e=2):
  print(2+e)
func(6)
# DEfault function parameters
def check(country='Nigeria'):
  print("I'm from "+country)
check('Britain')
check()

# Return values

def ret(x=8):
  return x*5
print(ret())


# LANMBDA function

lamn=lambda i: i*2
print(lamn(2))

lamn2=lambda x,y,z: (x+y)/z
print(lamn2(2,6,4))

def my(x):
  return 8*3

print(my(6))
# def myfunc(n):
#   return lambda i: i*n

# doubler = myfunc(2)
# tripler = myfunc(3)
# val = 11
# print(i)
# print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))



def fun(n):
 return lambda i: i*n


double = fun(4)
print(double(3))

def myfunc(n):
 return lambda i: i*n

doubler = myfunc(2)
print(doubler(6))


# Classes and Objects
class turtl:
  def __init__(self,age,name):
    self.name=name
    self.age=age
  def par(sel):
      print('Hello Mr.'+sel.name)
p2=turtl(14,'KLI')
p2.par()
      

class joy:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def par(self):
    print('Hello '+self.name)


p1=joy('Adeola',344)
p1.par()


import mymodule
mymodule.hel('Jonathan')
# p1=turtl(12,'TY')
# print(p1.age)
# print(p1.name)
# print(p1)
myName='Faithful'
class lautech:
  def __init__(self,name='Daniel',age=35):
    self.name=name
    self.age=age
  def prince(self):
      print('Hello '+self.name)
      print("I'm {0:d} years old".format(self.age))
      
faith=lautech(myName,22)
faith.prince()
Tolu=lautech('Tchu',22)
Tolu.age=21
# Tolu.prince()
Tolu.prince()
tayo=lautech()
tayo.prince()

def mul(x,y):
  return x*y

ret=mul(3,2)
print(ret)
import mults as mul
print(mul.multiply(2,10))
squa=mul.square(7)
name=mul.person1['name']
nose=mul.person1['nose']
print(squa)
print('my name is '+name+' and I have {0:d} nose'.format(nose))
multsDir=dir(mul)
print(multsDir)
import platform as pt
dit=dir(pt)
print(dit)
div=pt.system()


from mults import set2019 as glorius
leng=len(glorius)
bestPlayer=glorius[leng-1]
print(bestPlayer+' is the best player in our set')
trial=0
def game(k=5):
 k=k-1
 
 
 guess=int(input('Try your luck and win $100,000 by guessing a number between 1 and 10 Guess Here: '))
 import random as rd
 numb=rd.randint(0,10)
 print('The computer guessed:',numb)
 if guess==numb:
   
   print("SO lucky you have a great guessing power and you've won the Cash price ")
 elif guess-numb==1 or guess-numb==2 or guess-numb==-1 or guess-numb==-2 :
   
   print(k)
   print('{0:d} trials more'.format(k))
   print('So close try again bruhhhhhhhhhhhhhhhh')
   game(k)
 elif (k==0):
   print('SORRY GAMEOVER')
   

 
 else:
   
   
   print('{0:d} trials more'.format(k))
   print('Try again')
   game(k)

 
game()
