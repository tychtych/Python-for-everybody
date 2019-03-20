
def swap_case(s):
    res = ""
    for letter in s:
        if letter == isupper():
            res += letter.lower()
        else:
            res += letter.upper()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)