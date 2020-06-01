
class Utils:
    @staticmethod
    def len(str_):
        len = 0
        for c in str_: # while(*str++ != '\0') ;
            len +=1
        return len

    @staticmethod
    def cmp(s1, s2):
        if Utils.len(s1) != Utils.len(s2):
            return False
        l = Utils.len(s1)
        for i in range(0, l):
            if s1[i] != s2[i]:
                return False
        return True

    # 10 points
    @staticmethod
    def find(str_, pattern_): 
        if str_ is None or pattern_ is None:
            return None #unexpected usage
        origin_len = Utils.len(str_) #origin size
        patt_len = Utils.len(pattern_)
        #walker...
        for i in range(0, origin_len):
            s = str_[i:i+patt_len] # array slice 
            if Utils.cmp(s, pattern_) is True:
                return i
        return None

    @staticmethod
    def find_chr(str_, chr):
        """finds the index of a chr or returns None"""
        for i in range(0, Utils.len(str_)):
            if str_[i] == chr:
                return i
        return None

    @staticmethod
    def split(str_, delimiter):
        """Return exact match of splits in a string"""
        str_ = Utils.trimall(str_, delimiter)
        s = str() 
        ret = []  # data for storing string arrays - (s)      
        i = 0 
        #?
        if Utils.len(str_) == 0:
            return
        dindex = Utils.find_chr(str_, delimiter)
        if dindex is None: # no more delimiters found!
            while i < Utils.len(str_):
                s += str_[i]
                i += 1
            ret.append(s)
            return ret
        else:
            while i < dindex:
                s += str_[i]
                i += 1
            ret.append(s)
            ret = ret + Utils.split(str_[i+1:Utils.len(str_)], delimiter)
        return ret


    @staticmethod
    def ltrim(str_, pat):
        i = 0
        while str_[i] == pat:
            i+= 1
        return str_[i:Utils.len(str_)]
    
    @staticmethod
    def rtrim(str_, pat):
        i = Utils.len(str_) - 1
        while str_[i] == pat:
            i-=1
        return str_[0:i+1]
    
    @staticmethod
    def trimall(str_, pat):
        return Utils.ltrim(Utils.rtrim(str_, pat), pat)
    

TEST_STR = ",,,123,456,789, 1000,aaaa,,,,"
TEST_STR2 = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f"
if __name__ == "__main__":

#    test = Utils.trimall(TEST_STR, ",")    
    arr2 = Utils.split(TEST_STR2, ",")    
    pylibspl = TEST_STR2.split(",")
    pass