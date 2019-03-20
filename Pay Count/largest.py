largest = None

smallest = None


while True:
    input_str = input("Enter a number: ")
    if input_str == "done":
        break
    try:
        parsed_integer = int(input_str)
        if largest is None or parsed_integer > largest:
            largest = parsed_integer
        if smallest is None or parsed_integer < smallest:
            smallest = parsed_integer
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
