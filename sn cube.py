def cube_sum_of_naturals(n):
    return sum(i ** 3 for i in range(1, n + 1))
n=int(input("Enter a number:"))
print("Cube sum of first",n,"natural numbers:", cube_sum_of_naturals(n))