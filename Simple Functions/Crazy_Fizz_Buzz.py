'''
 * Write a program that prints the integers from 1 to 100 (inclusive).
 * But:
 *  - for multiples of three, print Lub (instead of the number)
 *  - for multiples of five, print Dub (instead of the number)
 *  - for multiples of both three and five, print LubDub (instead of the number)
'''

def FizzBuzzer(i,y): # Takes in two numbers in the range of i and y and then using control flow inserts the lubs and dubs as required.
    for x in range (i,y):
        if x % 3 == 0 and x % 5 == 0:
            print('LubDub')
        elif x % 3 == 0:
            print('Lub')
        elif x % 5 == 0:
            print('Dub')
        else:
            print(x)
            
FizzBuzzer(1,101)
FizzBuzzer(1,1001)
FizzBuzzer(1,10001)
FizzBuzzer(1,100001)
FizzBuzzer(1,1000001)
