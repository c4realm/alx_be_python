#understanding the question using while loops and nested for loops to draw a simple text based pattern.

size = int(input("Enter the size of the pattern: "))

#initialize row counter 
row = 0

while row < size:
    for col in range(size):
        print("*", end = "")
    print()
    row += 1
