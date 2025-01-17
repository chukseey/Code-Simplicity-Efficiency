"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
import itertools

def my_function(X):
    solutions = []
    side1 = [x for x in range(5,X)]
    side2 = [y for y in range(4,X)]
    side3 = [z for z in range(3,X)]
    for x,y,z in itertools.product(side1, side2, side3):
        if (x*x==y*y+z*z):
            solutions.append([x, y, z])
    m = 0
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m
try:
    X = input("What is the maximal length of the triangle side? Enter a number: ")
    answer = my_function(int(X))
except ValueError:
    print("Your input wasn't a number")
else:
    print(f"The longest side possible is {answer}")