score = input("Enter Score: ")
x = float(score)

if x >= 0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("D")
elif 0.0 <= x < 0.6:
    print("F")
else:
    print("Invalid score")
