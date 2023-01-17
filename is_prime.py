def is_prime(N):

    for n in range(2,N):
        if N % n == 0:
            return False

    return True


N = 30
if is_prime(N):
    print(f'{N:d} is a prime number')
else:
    print(f'{N:d} is not a prime number')
