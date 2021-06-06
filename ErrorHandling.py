# data=input('Type your age here ')
# try:
#     print(int(data/0))
# except :

#     import sys
#     err=sys.exc_info()[0]
#     print(err)

# finally:
#     print('uessssssss')

class ss3:
    'Men in the SS3 Class then!'
    table=5
    def __init__(self,data,age):
       
        self.data=data
        self.age=age
        ss3.table+=1
    def sayName(self):
        print(self.age)
        print(ss3.table)
        
tio=ss3('OBA',17)

tio.data='DAVID'
print(getattr(tio,'data'))
tio.sayName()
fav=ss3('Favour',16)
fav.sayName()
# print(tio.__doc__)
# print(tio.__dict__)
