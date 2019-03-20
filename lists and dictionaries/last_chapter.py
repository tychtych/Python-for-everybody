fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

counts = dict()

for line in fh:
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    words = line.split()
    timing = words[5]
    exact_timing = timing.split(":")
    hour = exact_timing[0]
    counts[hour] = counts.get(hour, 0) + 1

lst = list()
for k,v in sorted(counts.items()):
    print(k,v)






