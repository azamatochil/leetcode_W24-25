

def print_rev(s):
    rev(s, 0, len(s) - 1)
    return s

def rev(s, i, j):
    if i == j:
        return

    temp = s[i]
    s[i] = s[j]
    s[j] = temp

    rev(s, i + 1, j - 1)

print(print_rev(["h","e","l","l","o"]))

