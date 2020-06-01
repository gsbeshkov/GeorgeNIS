
GIVE A PROPER NAME 
import os
import subprocess

from class3 import ErrorCodes

'''
https://github.com/gsbeshkov/Data.git
'''

GIT = "C:\\Program Files\\Git\\bin\\git.exe"

class Command:

    def __init__(self, name):
        self._name=name
        self._stdout = None
        self._stderr = None

    # pitfalls???
    def execute(self, cmd, interactive=True): #ask for unused
        if cmd is None: # mark 1
            return ErrorCodes.E_UNKNOWN
        stdout, stderr = None, None
        try:
            #??? stdi=subprocess.PIPE - what is this?
            fp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            (self._stdout, self._stderr) = fp.communicate()
        except:
            return ErrorCodes.E_COMMAND_EXCEPTION

        if not self._stdout:
            return ErrorCodes.E_NO_STDOUT_DATA
        return ErrorCodes.E_ALL_OK


def goto_data(fpath="Data"):
    #problems???
    cwd = str("%s\\%s\\" % (os.getcwd(), fpath))
    os.chdir(cwd)
    print("[%s]" % os.getcwd())
    # git add <file>
    # git commit -m "message" 
    # git push


#unit test
if __name__ == "__main__":
    goto_data() # go to folder ??? are we tehre?
    #print(cwd)
    fp = open(".gitignore", "w")
    fp.close()
    add = Command("adder")
    commit = Command("commiter")
    push = Command("pusher")
    # logic???
    # state machine simple 
    add.excecute("git add .")
    commit.excecute("git commit -m \"init commit\" ")
    push.excecute("git push")
    pass


    



