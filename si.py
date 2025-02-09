def simple_interest(principal, rate, time):
    return (p*r*t) / 100
p=int(input("Enter principal amount:"))
r=int(input("Enter rate:"))
t=int(input("Enter time:"))
print("Simple Interest is:", simple_interest(p,r,t))