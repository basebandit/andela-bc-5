def reverse(s):
    return s[::-1]

"""Returns the reverse of a string"""


def reversex(s):
    for i in range(len(s) // 2):
        s = list(s)
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

    return "".join(s)


# examples
print reverse("mwas")
print reversex("hello")
