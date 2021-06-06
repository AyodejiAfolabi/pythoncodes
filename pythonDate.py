import datetime
thisday=datetime.datetime.now()
print(thisday)
print(thisday.year)
print(thisday.strftime('%A'))
print(thisday.strftime('%B'))
# print(thisday.strftime('%C))
somedate=datetime.datetime(2019,7,20,4,50,00)
print(somedate)
print('Todays date is ', thisday.strftime('%A'), thisday.strftime('%d'), 'of', thisday.strftime('%B'), thisday.strftime('%Y') )
arr1=['Tobi']
arr2=['Joshua']
arr3=arr1+arr2
print(arr3)
print(thisday.strftime('%d/%B/%Y'))

# myInp=input('Input your DOB here: ')
# DOB=datetime.datetime.strptime(myInp,'%d,%m,%Y')
# DOBJ=DOB.date()
# print(DOBJ)
# print(DOB)
now=datetime.datetime.now()
print(now.minute)
# diff=DOBJ-now
# print(diff.days)
# total=input('write a data here: ')

# if 3==3 or (4==5 and 6==4) :
#     print('yesssssss')

# area=input('Please input you location here:  ').upper()
# price=float(input('Pls input the price of you goods here: '))
# if area=='NIGERIA':
#     print("You'll be charge for this service ooo")
#     zones=input('Which regions from Nigeria?').upper()
#     if zones=='NORTH':
#         print('Good day my fellow Hausa')
#         print("You'll be charge 0.05"+' %'+'of the good price as tax')
#         print('goods + Total charges=', (price+(0.05*price)))
#         print('Nice doing businesss with you')
#     if zones=='NORTH':     
#         print('Good day my fellow Igbo')
#         print("You'll be charge 0.15"+' %'+'of the good price as tax')
#         print('goods + Total charges=', (price+(0.13*price)))
#         print('Nice doing businesss with you')
        
#     if zones=='WEST':
        
#         print('Good day my fellow Yoruba')
#         print("You'll be charge 0.05"+' %'+'of the good price as tax'+'and 0.06 %'+' as Oduduwa congress tax')
#         print('goods + Total charges=', (price+(0.11*price)))
#         print('Nice doing businesss with you')
            
         


# else:
#     print('Your package will be delivered soon')
#     print('goods + 0 charges=', price)
#     print('Nice doing businesss with you')


data=input()
if data !='':
    data=int(data)
    print(data)
    print((data-22))
