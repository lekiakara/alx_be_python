# Prompt user to enter size of pattern

size = int(input("Enter the size of the pattern: "))

# Draw the pattern

row = 0 
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1

