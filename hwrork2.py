from strutils import *

TEST_STR = "12345678910A12345678910B123456789C10123456789D1012345678910"

# define a function that returns N matches in of a substring
# return NONE if no matches
# else return index of last occurence of match
def find_n(str_, pat_, n): 
    pass
           

def find_n2(str_, pat_, n):
    # possible states
    # 1. No matches  - no recursion , no count checks
    # 2. Matches ok. How many? 
    # first entry, second entry, N-th entry... what to do?
    print("Itteration number: ", n) #hint 
    found = Utils.find(str_, pat_)
    if found is not None:
        #we have at least one match 
        find_n2(str_[found+Utils.len(pat_):Utils.len(str_)], pat_, n-1)
    else: #modify states !!!
        return False
    return True # return True or False 


if __name__ == "__main__":
    find_n2(TEST_STR, "123", 3)