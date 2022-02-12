from colored import stylize, fg

# decoration
print(stylize("\n---- | Get square root using Newton's method | ----\n", fg("red")))

# user interaction
number = float(input("Enter a number: "))

# function
def square_root(num):
    x = num

    while True:
        root = 0.5 * (x + num / x)

        if abs(root - x) < 0.00001:
            break

        x = root
    return round(root, 5)

# output
output = stylize(square_root(number), fg("red"))
print(f"\nThe square root of {number} is {output}.\n")
