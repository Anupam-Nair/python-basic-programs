def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))
n=int(input("Enter a number:"))
print("Sum of squares of first",n,"natural numbers:", sum_of_squares(n))