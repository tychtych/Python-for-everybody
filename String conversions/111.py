def swap_case(s):
    res = ""
    for letter in s:
        if letter == letter.upper():
            res += letter.lower()
        else:
            res += letter.upper()
    return res
