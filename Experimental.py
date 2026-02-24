#!/usr/bin/env python3

try:
	number = int(input("What's your number: "))
	print(number)
except ValueError:
	print("It's not a number, sorry")
	