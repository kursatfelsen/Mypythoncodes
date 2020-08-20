"""
Perfect Numbers

Write a function named "perfect_numbers" which takes an integer N and returns a tuple containing three lists. The first list contains "perfect" numbers, the second list contains a list of "deficient" numbers, and the third list contains a list of "abundant" numbers.

    A number is "perfect" if it is equal to the sum of its proper divisors.
    A number is "deficient" if it is less than the sum of its proper divisors.
    A number is "abundant" if it is greater than the sum of its proper divisors.

For instance, 28 is perfect because 28 is equal to 1 + 2 + 4 + 7 + 14.

Sample Run:

>>> perfect_numbers(5)
([], [], [1, 2, 3, 4])
>>> perfect_numbers(8)
([6], [], [1, 2, 3, 4, 5, 7])
>>> perfect_numbers(20)
([6], [12, 18], [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19])
"""

def sumdiv(number):
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    return sum
def perfect_numbers(number):
    perfect=[]
    deficient=[]
    abundant=[]
    for i in range(1,number):
        if sumdiv(i)==i:
            perfect.append(i)
        elif sumdiv(i)>= i:
            deficient.append(i)
        else:
            abundant.append(i)
    result=(perfect,deficient,abundant)
    return result
    
    -------------------------------------------------------------
    """
    2. Pascal's Triangle

Write a function named "pascal" that takes an integer N as argument and returns Pascal's triangle of height N as a nested list.

For instance, Pascal's triangle of height 7 is:

            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5  10   10  5   1
1   6  15   20  15  6   1

Sample Run:

>>> pascal(1)
[[1]]
>>> pascal(3)
[[1], [1, 1], [1, 2, 1]]
>>> pascal(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
>>> pascal(6)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
"""
def lstcon(items):
    liste=[]
    for i in range(len(items)-1):
        liste=liste+[items[i]+items[i+1]]
    return [1]+liste+[1]

def pascal(number):
    if number==1:
        return [[1]]
    if number==2:
        return [[1],[1,1]]
    liste=[[1],[1,1]]
    for i in range(1,number-1):
        liste=liste+[lstcon(liste[i])]
    return liste
    ----------------------------------------
