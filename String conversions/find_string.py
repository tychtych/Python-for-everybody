def count_substring(string, sub_string):
    if string[0:200]:
        return string.count(sub_string, 0, 200)
    else:
        return "Invalid"

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)