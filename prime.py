def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
num=int(input("Enter a number:"))
print("Is",num,"a prime number?", is_prime(num))