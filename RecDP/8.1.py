# 8.1

def calculate_steps(n):
    if n < 0:
        return 0
    if n == 0 or n == 1 or n == 2:
        return n
    return calculate_steps(n-1) + calculate_steps(n-2) + calculate_steps(n-3)

def calculate_dp_steps(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

def main():
    n = int(input())
    print("Total ways is ", calculate_dp_steps(n))

if __name__ == "__main__":
    main()
