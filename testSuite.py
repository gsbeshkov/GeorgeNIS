
from Command import Command
from ErrorCodes import ErrorCodes

class TestSuite(object):
    """description of class"""

    def __init__(self):
        pass


    def testcase1(self):
        """commebts here"""
        allOk = False
        c = Command("test1")
        error = c.execute("dir")
        if error == ErrorCodes.E_ALL_OK:
            tostrr = str(c._stdout)
            #1 find entry with <DIR> 
            #[0][][][][][<DIR>][][][][n-1]
            #2 remove elements with len < 2 
            spl = tostrr.split("\\")
            #[][][<DIR>][][]
            #   [<][D][I][R][>]
            for i in range(0, len(spl)):
                if len(spl[i]) < 2:
                    print ("HIT")
                elif len(spl[i]) >=5:
                    if TestSuite.my_find(spl[i], "<DIR>"):
                        print("FOUND")
                    pass
            pass

        elif error == ErrorCodes.E_COMMAND_EXCEPTION:
            print("Command excepiton")
        elif error == ErrorCodes.E_UNKNOWN:
            print("Unknown data")
        else:
            pass
        return allOk


    def testcase2(self):
        test_len = TestSuite.my_len("1234567890")
        print (test_len)

    def testcase3(self):
        s1 = "abc"
        s2 = "def"
        s3 = "Def"
        print(TestSuite.my_cmp(s1, s2))
        print(TestSuite.my_cmp(s2, s3))

    def testcase4(self):
        orig = "ALicew went into Rabbit's house"
        pat = "went"
        if TestSuite.my_find(orig, pat) is True:
            print ("FOUND")
        else:
            print ("NOT FOUND")


if __name__ == "__main__":
    testsuite = TestSuite()
    #testsuite.testcase1()

    #testsuite.testcase2()

    #testsuite.testcase3()

    #testsuite.testcase4()
    if testsuite.testcase1() is True:
        print("Ready to deploy")
