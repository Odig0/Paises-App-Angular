def calculate_string_value(t):
    n = len(t)
    max_value = 0

    for i in range(n):
        count = 0
        for j in range(i, n):
            if t[j] == t[i]:
                count += 1
                value = count * (j - i + 1)
                max_value = max(max_value, value)
            else:
                break

    return max_value

# Read the input string
t = "abcabcddd"

# Calculate and print the maximum value of f(s) for all substrings
print(calculate_string_value(t))
