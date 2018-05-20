# from 1 to 100, if the number is divisible by 3, print Fizz, if divisible by 5, print Buzz.
# if divisible by both 3 and 5, print FizzBuzz.
# the number will be printed above the string in this script.
# e.g.:
# 15
# FizzBuzz

import sys;

for num in range(1, 100):
    
    print num;
    
    if (num % 3 == 0):
        sys.stdout.write('Fizz');
        sys.stdout.flush();
    
    if (num % 5 == 0):
        sys.stdout.write('Buzz');
        sys.stdout.flush();

    if (((num % 3) * (num % 5)) == 0):
        print;

print 'finished';
