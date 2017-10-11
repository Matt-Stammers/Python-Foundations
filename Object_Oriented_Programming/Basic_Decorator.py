'''

The main mode is having a method named main inside a class and should return nothing but should print a line to the standard output with the message Hello World!. 
For Java the main method should receive String array as parameters that can be specified when running from console with the command. 
In many traditional programming languages can be only one main for a whole application since it denotes the application entry point.

'''

# this won't work:

class Solution:
    def main(*args):
        print 'Hello World!'
        
# because the function is not decorated. This will however:

class Solution:
    @staticmethod
    def main(*args):
        print 'Hello World!'
        
# as will this:

class Solution:
    #your code here
    def __init__(self):
        pass
    @staticmethod
    def main(self,arg=None):
        print("Hello World!")

# this will also work but it is much better to use a decorator:

class Solution(object):
    def main(self, *arg):
        print ("Hello World!")
        
Solution = Solution()
