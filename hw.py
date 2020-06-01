TEST_STR = "123456789"

#write a function that prints contents in a string in a reverse order
#in: "123456789"
#out: "987654321"
def print_reverse(str_):
    #hint: use while loop
<<<<<<< HEAD
   revercedString=[]
   index = len(TEST_STR) #calculate index lenght 
   while index > 0:
       revercedString += TEST_STR[ index - 1 ] #saving the value for the reverced string??? seem wrong 
       index = index - 1 # decrementing by 1
       print(revercedString) # prinitng shit....
 
   pass
=======
    revercedString=[]
    s = str()
    index = len(TEST_STR) #calculate index lenght #---- > use function argument (ex. str_) , not global value TEST_STR
    while index > 0:
        revercedString += TEST_STR[ index - 1 ] #saving the value for the reverced string??? seem wrong 
        index = index - 1 # decrementing by 1
        s += str_[index]
    print(s)

>>>>>>> 114297dd7ca0d3d7b3a8b9cc7fb942fca44cef18


#write a function that prints all odd characters in the test string 
#in: "123456789"
#out: "13579"
def print_odd(str_):
    #hint - see modulo operator - %
    #if i % 2 == 0
    string = "1234567890"#In
    for index in range(len(string)):
        #Check if odd 
        if(index % 2 == 0):
            #print odd characters
            print(string[index])
        


#write a function that cuts a string each time it loops by 1 bytes
#in: "123456789"
#out: 
#1 loop - 123456789
#2 loop - 23456789
#3 loop - 3456789
#...
#last loop - 9
def cut_offn(str_):
    #hint: use array slice [n:m]
    pass



if __name__ == "__main__":
    print_reverse(TEST_STR)
    print_odd(TEST_STR)
    cut_offn(TEST_STR)