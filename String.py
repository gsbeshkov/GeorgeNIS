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
    def __eq__(self, other):        
        return Utils.cmp(self.m_data, other.m_data) #compare the two objects, and return True or False
        
    def __lt__(self, other):
        if self.m_data == other:
            pass
        else:
         return self.m_data[0] < other.m_data[0]
        
        
    def find_chr(self, chr): #homework
        pass
            
    def find(self, pat):
        return Utils.find(self.m_data, pat)
    
    def len(self):
        return Utils.len(self.m_data)
    
    
class StringBuilder:
    # builds a complete string from string chunks 
    def __init__(self):
        self.m_data = []
    
    def add(self, st):
        if st is None:
           st = []
        st.append(st)
        #optional - improve add
        # too long or somethig else - be creative
        if len(st) == 0:
            return self
        
        self.m_data.append(st)
        return self
    
    def begin(self):
        #homework - find the problem and design it accordingly
        if len(self.m_data) > 0:
            self.m_data = None
            self.m_data = []
        return self
    
    def build(self): 
        # homework
        # what do we need to do ?
        s = String(" ")
        for a in self.m_data:
            s.m_data += a.m_data
        self.m_data = None
        return s
    


if __name__ == "__main__":
    
    #debug and improve the class     
    sb = StringBuilder()
    
    s1 = sb.begin().add(String("Ken")).add(String("Alice")).add(String("Bob")).build()
    s2 = sb.begin().add(String("Ken")).add(String("Alice")).add(String("Bob")).build()
    s3 = sb.begin().add(String("Ken")).add(String("Alice")).add(String("Bob")). \
        add(String("Ken")).add(String("Alice")).add(String("Bob")).build().build() # is that possible?
    s4 = sb.begin().begin().add(String("Ken")).add(String("Alice")).add(String("Bob")).build().build()
    

    

    
    
    
    


