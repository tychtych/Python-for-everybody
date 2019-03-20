fname = input("Enter file name: ")
fh = open(fname)
count = 0
overall = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.strip()
    parsed_string = float(line[19:])
    overall = overall + parsed_string
    count = count + 1
print("Average spam confidence:", overall / count)




