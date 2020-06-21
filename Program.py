from Command import *
from os import popen
from pip._vendor.pyparsing import line

class FileOps:
    # HW: catch all possible pitfalls of missing files, dirs, etc.
    # Be creative and add meaningful ERROR CODES as return type 
    def __init__(self, rootdir):
        self.m_root = str(rootdir)
        self.m_data = []


    def home(self):
        return  self.chdir(self.m_root)
        
    
    def chdir(self, newdir):
        try:
            os.chdir(newdir) # what will happen if newdir is not found ??? research and fix!!!
            return ErrorCodes.E_DIR_OK
        except:
            pass
        return ErrorCodes.E_DIR_NOT_FOUND

        
    def read(self, fname):
        with open(fname) as fp:
            self.m_data = fp.readlines()
        
    
class Program:
    
    def __init__(self):
        self.m_shell = Command("console")
        self.m_cmd = Command("cmd")
        self.m_fileops = FileOps(os.getcwd())
        self.m_entries = [] # store qt5 related data 


    #Expected:
    def doWorkEx(self, optdir="AssesmentL1"):
        self.m_shell.execute("git clone https://github.com/gsbeshkov/Data.git {}".format(optdir))
        if self.m_fileops.chdir(optdir) == ErrorCodes.E_DIR_NOT_FOUND:
            return False
        self.m_fileops.read('dnfhistory.txt')

        for entry in self.m_fileops.m_data:
            if "qt5" in entry and ("qscintilla" in entry or "python" in entry):
                continue
            elif "qt5" in entry:
                self.m_entries.append(entry)
        
        with open("db.txt", "w") as FP:
            for e in self.m_entries:
                s = e.split("|")
                if "Install" in s[3]:
                    f = "{} installed at {}\r\n".format(s[1], s[2])
                    FP.write(f)
        
        self.m_shell.execute("git add db.txt")
        self.m_shell.execute("git commit -m \" assesment passed, please check!\"")
        self.m_shell.execute("git push")        
        return True



    # too many misses... 
    def doWork(self):
        if self.m_fileops.chdir("AssesmentL1") == ErrorCodes.E_DIR_NOT_FOUND:
            return False
        f = open("dnfhistory.txt", "r")
        print(f.readlines())
        self.m_fileops.read("dnfhistory.txt")
        for line in self.m_fileops:
            if line.__contains__('qt5'):
                self.m_fileops.f = open('updates.txt', 'w')
            
            f.write('Woops! I have deleted the content!')
       
        
        filepath = 'dnfhistory.txt'
        with open('filepath') as fp:
        #line = fp.readline()
            cnt = 1
            while line:
                print("qt5-qtquickcontrols installed at {}: {}".format(cnt, line.strip()))
                line = fp.readlines()
                cnt +=  1    
                    
        return True # better error code  
        


if __name__ == "__main__":
    
    p = Program()
    #p.m_shell.execute("git clone https://github.com/gsbeshkov/Data.git AssesmentL1")
    
    p.doWorkEx()
    pass
    
    