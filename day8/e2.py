def prime_checker(n):
    prime = True
    for i in range(2,n):
        if n %i == 0:
            prime = False
    if prime:
        return True
    else:
        return False

n = int(input("CHeck this number: "))
if prime_checker(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")