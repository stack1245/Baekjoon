n = int(input())

if n == 1:
    print(0)
else:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n + 1) if is_prime[i]]

    count = 0
    left = 0
    right = 0
    total = 0

    while True:
        if total >= n:
            if total == n:
                count += 1
            total -= primes[left]
            left += 1
        elif right == len(primes):
            break
        else:
            total += primes[right]
            right += 1

    print(count)
