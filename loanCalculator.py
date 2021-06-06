print('Welcome to Our Money Loan Service')

loanStr=input('How Much do You wanna Borrow: ')
loanInt=float(loanStr)
loanTime=int(input('For how long will you pay the loan/months: '))
loanInteStr=input('please at what rate will you like to borrow the money: ')
loanInteInt=float(loanInteStr)

loanNoPstr=input('How many times will you pay the the money before you will complete the balance: ')
loanNoPInt=float(loanNoPstr)


firstPart=loanInt*(loanInteInt*(1+loanInteInt)*loanNoPInt)
secondPart=(1+loanInteInt)*loanNoPInt-1
AmoutPayBack=firstPart/secondPart
print('Therefore you will pay back {0:f} dollars in {1:d} month'.format(AmoutPayBack,loanTime))