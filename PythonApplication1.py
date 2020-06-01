import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))
thisYear = int(datetime.date.today().strftime("%Y"))
year = str((thisYear - age) + 100)
print(name + " will be 100 years old in the year " + year )

#num = int(input("Enter a number: "))
#mod = num % 2
#if mod > 0:
#    print("You picked an odd number.")
#else:
#    print("You picked an even number")
#
#num = int(input("Give me a number to check: "))
#check = int(input("Give me a number to divide by"))
#
#if num % 4 == 0:
#    print(num, "is a multiple of 4")
#elif num % 2:
#    print(num, "is an even number")
#else:
#    print(num,"is an odd number")
#
#if num % check == 0:
#    print(num,"divides evenly by", check)
#else:
#    print(num, "does not divide evenly by", check)


#string= 'blablalbalbla'
#print(lambda string : print(string))

#A REGULAR FUNCTION
#def guru( funct, *args ):
# funct( *args )
#def printer_one( arg ):
# return print (arg)
#def printer_two( arg ):
# print(arg)
##CALL A REGULAR FUNCTION 
#guru( printer_one, 'printer 1 REGULAR CALL' )
#guru( printer_two, 'printer 2 REGULAR CALL \n' )
##CALL A REGULAR FUNCTION THRU A LAMBDA
#guru(lambda: printer_one('printer 1 LAMBDA CALL'))
#guru(lambda: printer_two('printer 2 LAMBDA CALL'))


