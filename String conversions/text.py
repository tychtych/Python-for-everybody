fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    strip_line = line.rstrip()
    print(strip_line.upper())

