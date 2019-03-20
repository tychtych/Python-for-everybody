fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    words = line.split()
    email_from_line = words[1]
    counts[email_from_line] = counts.get(email_from_line, 0) + 1


bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)