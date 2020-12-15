def primes(n):
    prime_list = []
    for pos_prime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(pos_prime ** 0.5) + 1):
            if pos_prime % num == 0:
                isPrime = False
                break
        if isPrime:
            prime_list.append(pos_prime)

    return(prime_list)


def is_prime(m):
    if m >= 2:
        for y in range(2, m):
            if not (m % y):
                return False
    else:
        return False
    return True
