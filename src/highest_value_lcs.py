import sys

def OPT(values: dict, a: str, b: str) -> list:
    m, n = len(a), len(b)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[a[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def find_sol(dp: list, a: str, b: str) -> str:
    subsequence = []
    i, j = len(a), len(b)

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            subsequence.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()
    return ''.join(subsequence)


def lcs(values: dict, a: str, b: str) -> tuple:
    dp = OPT(values, a, b)
    max_value = dp[len(a)][len(b)]
    subsequence = find_sol(dp, a, b)
    return max_value, subsequence


def main():
    lines = sys.stdin.read().strip().split('\n')

    k = int(lines[0])

    values = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        c = parts[0]
        value = int(parts[1])
        values[c] = value

    a = lines[k + 1]
    b = lines[k + 2]

    max_value, subsequence = lcs(values, a, b)

    print(max_value)
    print(subsequence)


if __name__ == "__main__":
    main()
