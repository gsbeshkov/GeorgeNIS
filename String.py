from strutils import Utils

# howmework:
# add remaining Strutils methods as member functions to class String 
# [HARD] Find a way to compare two Strings using a member function [optional]
class String:
    # 1  - initialization
    # 2 - lifetime (scope)
    # 3 - dereferencing
    # 4 - can be traversed, enumerable, iterable... etc 
    def __init__(self, data):
        self.m_data = data
    
    #design this function as smart as possible 
    def cmp(self, s1, s2):
        return (Utils.len(s1)) != (Utils.len(s2)) #compare the two objects, and return True or False
        
        
    
    def find(self, pat):
        return Utils.find(self.m_data, pat)
    
    def len(self):
        return Utils.len(self.m_data)
    
    def badfoo(self):
        self.m_data = "bad data"
        
    def __del__(self):
        """what is this?"""
        print("~") 

def foo(): #fucntion scope
    #Python difference between __new__ and __init__
    st = String("foo")
    return st

TEST_STR = "123456789A123456789B123456789C"    

if __name__ == "__main__":
    st = foo()
    # 1 research case
    for i in range(0, 10):
        s = String(str(i)) #why __del__ called
    
    f = String(TEST_STR)
    f.badfoo()
    print(f.m_data)
    tmp = f.find("123")
    print("tmp is: ", tmp)
    print (f.len())
    
    f1 = String("123456789A123456789B123456789C")
    f1.badfoo()
    print(f1.m_data)
    tmp1 = f.find("123")
    print("tmp is: ", tmp1)
    print (f1.len())
    
    print(TEST_STR)

    
    
    
    


