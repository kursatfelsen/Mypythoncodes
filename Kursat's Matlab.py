#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("""****************************************
Welcome to Kursat's Math Lab

Which function you are about to use :

1=Factorial

2=Fibonacci Adder

3=Fibonacci Writer

4=For Exit
****************************************
""")

def factorial(x):
	#Kursat's Factorial calculator func.
	a = list(range(1,x+1))
	fact=1
	for i in a:
		fact *= i
	return fact

def fibonacci_sum(x):
	#Kursat's Fibonacci Adder...When user inputs a value n it will return sum of fibonacci numbers to the nth fibonacci number.
	n=1
	m=1
	Fib_Sum=1
	if x==0:
		return False
	elif x==1:
		Fib_Sum=1
	elif x<0:
		return False
	else:
		while x>1:
			n,m=m,m+n
			Fib_Sum +=n
			x-=1
	return Fib_Sum

def fibonacci(x):
	#Calculates the fibonacci numbers until xth 
	fib1=1
	fib2=1
	counter=2
	fiblist=[1,1]
	while counter <x:
		fib1+=fib2
		fiblist.append(fib1)
		fib1,fib2=fib2,fib1
		counter +=1
	return fiblist

	 

girdi=input()
STOP=1
while STOP==1:
	if girdi==4:
		print("Exiting From Program")
		STOP=2
	
	else:
		if girdi==1:
			F = int(input("Write the value of your number which you want to calculate it's factorial:"))
			print("Factorial of {} is {}".format(F,factorial(F)))
			girdi=input("Choose a process:")

		elif girdi==2:
			K = int(input("Write a positive integer for calculating sum of fibonacci number to the your value:"))
			if K<0:
				print("You entered a wrong value")
				K = int(input("Write a positive integer for calculating sum of fibonacci number to the your value:"))
				print("Sum of from 1st to {}th fibonacci number is {}.".format(K,fibonacci_sum(K)))
			else:
				print("Sum of from 1st to {}th fibonacci number is {}.".format(K,fibonacci_sum(K)))
				girdi=input("Choose a process:")
		elif girdi==3:
			Fi = int(input("Write the a number so it will count fibonacci numbers to the this value's times:"))
			print("Fibonacci Serial is :\n{}".format(fibonacci(Fi)))
			girdi=input("Choose a process:")
