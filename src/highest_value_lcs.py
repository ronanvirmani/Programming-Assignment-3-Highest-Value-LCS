import sys

'''
values: c -> v(c)
a: the first string
b: the second string

return: (max_value, subsequence)
'''
def highest_value_lcs(values: dict, a: str, b: str) -> tuple:
    pass


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

    max_value, subsequence = highest_value_lcs(values, a, b)

    print(max_value)
    print(subsequence)


if __name__ == "__main__":
    main()
