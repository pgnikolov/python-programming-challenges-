# Write a program that reads a string with N integers from the console, separated by a single space,
# and reverses them using a stack. Print the reversed integers on one line, separated by a single space.

from collections import deque

nums = input().split()

print(" ".join(nums[::-1]))
