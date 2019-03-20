fname = input("Enter file name: ")
fh = open(fname)

count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count = count + 1
print(count)


print("Done")



