
# def get_super(x):
# 	normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
# 	super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
# 	res = x.maketrans(''.join(normal), ''.join(super_s))
# 	return x.translate(res)
# print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ

# # subscript
# print(u'H\u2082SO\u2084') # H₂SO₄

# # superscript
# print("x\u00b2 + y\u00b2 = 2") # x² + y² = 2


bigMatrix=[]
matrix=int(input('How many test cases do you want: '))
# x=0

for x in range (0,matrix):
    eachMatrixCase={'testCase':x+1,'order':0,'numbers':[]}

    bigMatrix.append(eachMatrixCase)

def declareOrder():

    for x in bigMatrix:
    
        # print(3)
        matrix=int(input("What order do you want for the "+ str(x['testCase'])+' matrix: '))
        x['order']=matrix
    return bigMatrix

def writeNumbers():
    for cases in bigMatrix:
         print('fill in the '+str(cases['testCase'])+' matrix')
         for column in range(0,cases['order']):

             eachrow=[]
             for rows  in range(0,cases['order']):
                
                number=input('fill in the '+str(rows+1)+' item on row '+str(column+1) +' :')
                eachrow.append(number)
             cases['numbers'].append(eachrow)

        #  print(cases['numbers'])
    
    return displayInputs(bigMatrix)
            # print("fill up matrix "+ cases['testCase'])
            #  number=int(input("Input the "+ str(x['testCase'])+' matrix: '))
        

def displayInputs(matrices):
    print('\n')
    print( len(matrices))
    for matrix in matrices:
        print ('Matrix order: '+str(matrix['order']))
        for rows in matrix['numbers']:
            display=''
            for numbers in rows:
                
                display+=str(numbers)
                display+='   '
            print(display)
            # print('\n')
        print('--------------------------------')

def results():
    totalResult=[]
    for matrix in bigMatrix:
        eachResult=[]
        diagonalSum=0
        ij=0
        rowRecurrrence=0
        for rows in matrix['numbers']:
            
            diagonalSum+=int(rows[ij])
            ij+=1
            for number in rows:
              if(rows.count(number))>1:
                  
                  rowRecurrrence+=1
        eachResult.append(diagonalSum)
        eachResult.append(int(rowRecurrrence/2))
        totalResult.append(eachResult)
    return(totalResult)           
  
        


declareOrder()
writeNumbers()
print(results())