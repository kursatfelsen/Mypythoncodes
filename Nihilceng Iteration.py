 """Write an iterative version of the famous factorial function.

Sample Run:

>>> factorial(4)
24
>>> factorial(5)
120
"""
def factorial(number):
    i=1
    result=1
    while i<(number+1):
        result*=i
        i+=1
    return result
    
    
----------------------------------------------------------------------------------------------------------------------
""" Write a function named "countdown" that takes a number as argument and returns a list composed of numbers smaller than the argument in descending order.

Sample Run:

>>> countdown(2)
[2, 1]
>>> countdown(3)
[3, 2, 1]
"""
def countdown(number):
    list1=[]
    for i in range(number):
        list1.append(i+1)
    return list1[::-1]
----------------------------------------------------------------------------------------------------------------------
"""
 Write a function named "the3N1P" that takes an integer as argument and returns the length of the sequence produced by the following algorithm:

    input n
    if n = 1 then stop
    if n is odd then n = 3n + 1
    else n = n / 2
    goto 2

For example given the input 22, the following sequence of n's will be generated:

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

Sample Run:

>>> the3N1P(5)
6
>>> the3N1P(22)
16

"""
def the3N1P(n):
    x=1
    while n!=1:
        if n%2==1:
            n=3*n+1
        else:
            n/=2
        x+=1
    return x
    
-------------------------------------
"""
 Write a function named "isprime" that determines whether a given integer number is prime or not.

Sample Run:

>>> isprime(2)
True
>>> isprime(3)
True
>>> isprime(4)
False
>>> isprime(5)
True
"""
def isprime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
-----------------------------------------------------------------------------------------
"""
 Write a function named "triangle" that returns a list of strings that compose a triangle. Check the sample run for more information.

Sample Run:

>>> triangle(2)
[' *', '***']
>>> triangle(3)
['  *', ' ***', '*****']
>>> triangle(4)
['   *', '  ***', ' *****', '*******']
>>> print '\n'.join(triangle(5))
    *
   ***
  *****
 *******
*********
"""
def triangle(n):
    list1=[]
    for i in range(1,n+1):
        list1.append((n-i+1//2)*(" ")+((i*2-1)*"*"))
    return list1
------------------------------------------------------------------------------
"""
 Write a function named "lis" that takes a list containing numbers as argument and returns the length of the longest increasing subsequence in the list.

A subsequence [a1, a2, ..., an] is an increasing subsequence of length n if:

ai <= aj for all 1 <= i <= j <= n.

Sample Run:

>>> lis([1, 2, 3, 4, 3, 5, 6])
4
>>> lis([3, 2, 1])
1
>>> lis([1, 1, 2, 3, 4, 5, 1])
6

"""
def lis(items):
    a=1
    list1=[]
    for i in range(len(items)):
        x=i
        a=1
        if x==len(items)-1:
                break
        while items[x]<=items[x+1]:
            a+=1
            x+=1
            if x==len(items)-1:
                break
    	list1.append(a)
    return max(list1)
    
----------------------------------------------------------------------------------------------------
"""
 Write a function named "prime_factors" that returns the prime factors of an integer as a list.

Sample Run:

>>> prime_factors(5)
[5]
>>> prime_factors(15)
[3, 5]
>>> prime_factors(30)
[2, 3, 5]
>>> prime_factors(22)
[2, 11]
>>> prime_factors(66)
[2, 3, 11]

"""
def isprime(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
def prime_factors(n):
    list1=[]
    for i in range(2,n+1):
        if n%i==0:
            if isprime(i):
                list1.append(i)
    return list1
--------------------------------------------------------------------------
"""
 A Pythagorean triplet is a set of three natural numbers, a, b, c, for which,

a^2 + b^2 = c^2

For example,

3^2 + 4^2 = 9 + 16 = 25 = 5^2

Write a function named "triplets" which takes an integer argument N and returns the list of Pythagorean triplets for a, b, c, each less than N.

Sample Run:

>>> triplets(10)
[(3, 4, 5)]
>>> triplets(15)
[(3, 4, 5), (5, 12, 13), (6, 8, 10)]
>>> triplets(20)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]
 A Pythagorean triplet is a set of three natural numbers, a, b, c, for which,

a^2 + b^2 = c^2

For example,

3^2 + 4^2 = 9 + 16 = 25 = 5^2

Write a function named "triplets" which takes an integer argument N and returns the list of Pythagorean triplets for a, b, c, each less than N.

Sample Run:

>>> triplets(10)
[(3, 4, 5)]
>>> triplets(15)
[(3, 4, 5), (5, 12, 13), (6, 8, 10)]
>>> triplets(20)
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15)]

"""

def triplets(N):
    list1=[]
    for i in range(1,N):
        a=i
        for x in range(a+1,N):
            b=(x**2-a**2)**0.5
            if b-int(b)==0:
                if b>a:
                	list1.append((int(b),int(a),int(x)))
    return list1
