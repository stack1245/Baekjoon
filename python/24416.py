def fib(n):
    global recursive_call_count

    if n == 1 or n == 2:
        recursive_call_count += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global dp_call_count

    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1

    for i in range(3, n + 1):
        dp_call_count += 1
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input())

recursive_call_count = 0
dp_call_count = 0

fib(n)
fibonacci(n)

print(recursive_call_count, dp_call_count)
