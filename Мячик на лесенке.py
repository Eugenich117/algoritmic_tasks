
def main(n):
    if n == 0:
        print(1)
    elif n == 1:
        print(2)
    else:
        count = [0] * (n + 1)
        count[0] = 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
            if i >= 2:
                count[i] += count[i - 2]
            if i >= 3:
                count[i] += count[i - 3]
        print(count[n])

if __name__ == '__main__':
    n = int(input())
    main(n)

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if i >= 2:
        dp[i] += dp[i - 2]
    if i >= 3:
        dp[i] += dp[i - 3]
print(dp[n])