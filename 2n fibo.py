def nth_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
n=int(input("Enter a number:"))
print(n,"th Fibonacci Number:", nth_fibonacci(n))
print("Last two digit of",nth_fibonacci(n),"is",nth_fibonacci(n)%100)